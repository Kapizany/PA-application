from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create the extension
db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI=f"postgresql+psycopg2://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASS')}@{os.environ.get('POSTGRES_HOST')}/{os.environ.get('POSTGRES_DB')}"
