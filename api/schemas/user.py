from config.api import api
from flask_restx import fields, reqparse
from werkzeug.datastructures import FileStorage


create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username', type=str, location='form')
create_user_parser.add_argument('email', type=str, location='form')
create_user_parser.add_argument('avatar', type=FileStorage, location='files')

login_user_input = api.model('LoginUserInput', {
    "username": fields.String(),
    "password": fields.String(),
})

responser_user = api.model('ResponseUser', {
    "id": fields.Integer(),
    "username": fields.String(),
    "email": fields.String(),
    "avatar_path": fields.String(),
})

confirm_user_input = api.model('ConfirmUserInput', {
    "username": fields.String()
})

response_login = api.model('ResponseLogin', {
    "AccessToken": fields.String(),
    "ExpiresIn": fields.String(),
    "TokenType": fields.String(),
    "RefreshToken": fields.String(),
    
})

token_input_parser = reqparse.RequestParser()
token_input_parser.add_argument('Authorization', location='headers')