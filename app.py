from flask import Flask,request
import config
from models.db import initialize_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SHOW_SQLALCHEMY_LOG_MESSAGES'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

initialize_db(app)

from routes.front import front
app.register_blueprint(front)

