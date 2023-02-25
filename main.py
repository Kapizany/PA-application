from config.api import app, apm
from api.Resources import users
from api.utils import error_handling
from elasticapm.handlers.logging import LoggingHandler
from dotenv import load_dotenv
import os

load_dotenv() 

debug = os.environ.get('DEBUG', 'false') == 'true'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=debug)