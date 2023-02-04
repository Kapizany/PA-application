from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from config.db import SQLALCHEMY_DATABASE_URI, db


app = Flask(__name__)
api = Api(
    app=app,
    doc='/docs',
    prefix='/api',
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db.init_app(app)
migrate = Migrate(app, db)