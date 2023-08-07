import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer

#database connection 
import pymongo
client = pymongo.MongoClient()  # local instance of MongoDB
db = client.chatapp  # database name
collection = db.groups  # collection name

from api.models import Chat
from asgiref.sync import sync_to_async,async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat, self.created = None, None
    async def connect(self):
        await self.accept()
    
    #disconnect the connection
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        self.close()
        return super().disconnect(code)

    #receive the message
    async def receive(self, text_data):
        # Store the message in the database
        message = json.loads(text_data)
        print(message['type'])
        
        if message['type'] == 'join':
            users = message['room_name']
            self.room_name = '_'.join(sorted(users)).encode('ascii', 'ignore').decode('ascii').replace(' ', '_')
            self.room_group_name = f'chat_{self.room_name}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,
            )
            user1_name, user2_name = sorted(users)
            self.chat, self.created = await sync_to_async(Chat.objects.get_or_create)(user1_name=user1_name, user2_name=user2_name)
            print(self.room_group_name)

        elif message['type'] == 'delete':
            sender = message['sender']
            message = message['message']

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'delete',
                    'sender':sender,
                    'message':message
                }
            )
            self.chat.messages = [msg for msg in self.chat.messages if msg['sender'] != sender or msg['message'] != message]
            await sync_to_async(self.chat.save)()

        elif message['type'] == 'chat_message':
            print(message['sender'],message['message'])
            sender = message['sender']
            message = message['message']
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'sender':sender,
                    'message':message
                }
            )
            self.chat.messages.append({'sender': sender, 'message': message})
            await sync_to_async(self.chat.save)()

    async def chat_message(self, event):
        # Send the message to all connected clients
        print("Message sent to group")
        message = event['message']
        sender = event['sender']
        await self.send(text_data=json.dumps({'type':'chat_message','context':{'sender':sender,'message':message}}))

    async def delete(self, event):
        message = event['message']
        sender = event['sender']
        await self.send(text_data=json.dumps({
            'type': 'delete',
            'context': {'sender':sender,'message':message}
        }))