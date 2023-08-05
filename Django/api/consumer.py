import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer

#database connection 
import pymongo
client = pymongo.MongoClient()  # local instance of MongoDB
db = client.chatapp  # database name
collection = db.groups  # collection name


class ChatConsumer(AsyncWebsocketConsumer):
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
        try:
            name = message['name']
            text = message['message']
            document = {'name': name, 'message': text}
        except:
            pass
        print(message['type'])

        if message['type'] == 'join':
            self.room_name = message['room_name']
            self.room_group_name = f'chat_{self.room_name}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name,
            )
            print(self.room_group_name)

        elif message['type'] == 'delete':
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