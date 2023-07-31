from django.apps import AppConfig
import pymongo


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        self.collection = None
        self.client = None

    def ready(self):
        client = pymongo.MongoClient()  # local instance of MongoDB
        db = client.chatapp  # database name
        collection = db.todo  # collection name

        self.client = client
        self.collection = collection
