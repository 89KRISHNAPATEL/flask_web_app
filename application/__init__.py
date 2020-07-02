from flask import Flask
from config import config
from flask_mongoengine import MongoEngine

app = Flask(__name__,template_folder='templetes')
app.config.from_object(config)

db = MongoEngine()
db.init_app(app)

from application import routes

