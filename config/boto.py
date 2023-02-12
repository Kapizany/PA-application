import boto3
import os
from dotenv import load_dotenv


load_dotenv() 

session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get("COGNITO_AWS_REGION")
)