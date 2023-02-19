import logging
from config.boto import session 
import os


class Logging:
    
    def __init__(self, name):
        log_client = session.client(
            'logs',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get("COGNITO_AWS_REGION")
        )
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
    
    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)
        
    def error(self, message):
        self.logger.error(message)
        