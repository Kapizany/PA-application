from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from elasticapm.contrib.flask import ElasticAPM
from dotenv import load_dotenv
from config.db import SQLALCHEMY_DATABASE_URI, db
import os


load_dotenv() 


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['ELASTIC_APM'] = {
  # Set the required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'API',

  'SERVER_URL': os.environ.get('ELASTIC_APM_SERVER_URL'),

  # Set the service environment
  'ENVIRONMENT': os.environ.get('ENVIRONMENT'),
}

api = Api(
    app=app,
    doc='/docs',
    prefix='/api',
)

apm = ElasticAPM(app, logging=True)


db.init_app(app)
migrate = Migrate(app, db)