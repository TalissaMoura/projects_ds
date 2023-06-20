import os
from pymongo import MongoClient
from news.models import MongoJSONEncoder
from flask import Flask
from urllib.parse import quote_plus

#call python
app = Flask(__name__)
app_secret_key = open(os.environ["FLASK_APP_SECRET_KEY_FILE"],"r").read()
app.secret_key = app_secret_key
app.json_encoder = MongoJSONEncoder

#get user and password info
user_mdb = open(os.environ["MONGODB_USER_FILE"],"r").read()
password_mdb = open(os.environ["MONGODB_PASSWORD_FILE"],"r").read()

#connecting to mongo
user = quote_plus(user_mdb)
password = quote_plus(password_mdb)
database_name = "newsdatabase"
client = MongoClient(f"mongodb+srv://{user}:{password}@cluster1.rqsrosp.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("newsdatabase")


from news import routes