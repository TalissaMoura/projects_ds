import os
from pymongo import MongoClient
from news.models import MongoJSONEncoder
from flask import Flask
from urllib.parse import quote_plus

#call python
app = Flask(__name__)
app.secret_key = os.environ["FLASK_APP_SECRET_KEY"]
app.json_encoder = MongoJSONEncoder

#connecting to mongo
user = "user_talissa"
password = quote_plus(os.environ["MONGODB_PASSWORD"])
database_name = "newsdatabase"
client = MongoClient(f"mongodb+srv://{user}:{password}@cluster1.rqsrosp.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("newsdatabase")


from news import routes