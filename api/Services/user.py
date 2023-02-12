from datetime import datetime
import os
from uuid import uuid4
from werkzeug.exceptions import BadRequest

from config.s3 import s3
from api.Models.user import UserModel
from config.api import db
from config.cognito import cognito


class UserService:
    
    @staticmethod
    def get_user_by_access_token(token):
        response = cognito.get_user(AccessToken=token)
        return response
    
    @staticmethod
    def retrieve_by_id(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            raise BadRequest("User not found!")
        return user

    @staticmethod
    def create(user_args):
        try:
            new_user = UserModel(
                username = user_args.get('username'),
                email = user_args.get('email'),
                avatar_path = f"{uuid4()}/{str(datetime.now())}-{user_args['avatar'].filename}",
            )
            
            cognito.sign_up(
                ClientId=os.getenv("COGNITO_USER_CLIENT_ID"),
                Username=new_user.username,
                Password='123#Password',
                UserAttributes=[
                    {"Name": "email", "Value": new_user.email},
                ],
            )
            
            s3.upload_fileobj(
                user_args['avatar'],
                os.getenv("AWS_BUCKET_NAME"),
                new_user.avatar_path,
            )
            
            db.session.add(new_user)
        except Exception as err:
            db.session.rollback()
        else:
            db.session.commit()
            return new_user
    
    @staticmethod
    def confirm_user(username):
        cognito.admin_confirm_sign_up(
            UserPoolId=os.getenv("COGNITO_POOL_ID"),
            Username=username,
        )
        return
        
        
    @staticmethod
    def login(payload):
        username = payload.get('username')
        password = payload.get('password')
        
        response = cognito.initiate_auth(
                ClientId=os.getenv("COGNITO_USER_CLIENT_ID"),
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password,
                }
        )
        
        return {
            "AccessToken": response["AuthenticationResult"].get("AccessToken"),
            "ExpiresIn": response["AuthenticationResult"].get("ExpiresIn"),
            "TokenType": response["AuthenticationResult"].get("TokenType"),
            "RefreshToken": response["AuthenticationResult"].get("RefreshToken")
        }