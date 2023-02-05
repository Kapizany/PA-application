from datetime import datetime
import os
from uuid import uuid4
from werkzeug.exceptions import BadRequest

from config.s3 import s3
from api.Models.user import UserModel
from config.api import db

class UserService:
    
    @staticmethod
    def retrieve_by_id(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            raise BadRequest("User not found!")
        return user

    @staticmethod
    def create(user_args):
        new_user = UserModel(
            username = user_args.get('username'),
            email = user_args.get('email'),
            avatar_path = f"{uuid4()}/{str(datetime.now())}-{user_args['avatar'].filename}",
        )
        
        s3.upload_fileobj(
            user_args['avatar'],
            os.getenv("AWS_BUCKET_NAME"),
            new_user.avatar_path,
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return new_user
        