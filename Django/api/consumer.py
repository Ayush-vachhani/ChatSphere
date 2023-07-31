import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer

#database connection 
import pymongo
client = pymongo.MongoClient()  # local instance of MongoDB
db = client.chatapp  # database name
collection = db.groups  # collection name

#channel layers
from asgiref.sync import async_to_sync,sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'test'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        # self.send(text_data=json.dumps({'message': 'Connection successful'}))
        await self.accept()
    
    #disconnect the connection
    async def disconnect(self, code):
        await self.channel_layer.group_discard('test', self.channel_name)
        self.close()
        return super().disconnect(code)

    
    #send the message
    # def send(self, text_data=None):
    #     return super().send(text_data)
    
    #receive the message
    async def receive(self, text_data):
        # Store the message in the database
        message = json.loads(text_data)
        name = message['name']
        text = message['message']
        document = {'name': name, 'message': text}

        if message['type'] == 'delete':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'delete',
                    'message':message
                }
            )
        elif message['type'] == 'chat_message':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message':message
                }
            )
            collection.update_one(
                {},
                {'$push': {'text': document}}
            )

    async def chat_message(self, event):
        # Send the message to all connected clients
        print("Message sent to group")
        message = event['message']
        await self.send(text_data=json.dumps({'type':'chat_message','message': message}))

    async def delete(self, event):
        message = event['message']
        to_del = {"name":message['name'], "message":message['message']}
        print(to_del)
        collection.update_one(
            {},
            {'$pull': {'text': {'message': message['message']}}},
        )
        await self.send(text_data=json.dumps({
            'type': 'delete',
            'message': message
        }))