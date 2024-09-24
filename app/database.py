from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

load_dotenv()

mongo = None
db = None

def init_db(app):
    global mongo, db
    app.config["MONGO_URI"] = os.environ.get('DATABASE_URI')
    mongo = PyMongo(app)
    db = mongo.db
