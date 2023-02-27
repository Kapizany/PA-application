from flask_restx import Resource
from config.api import api, app
from api.Services.user import UserService
from config.logs import Logging
from api.schemas.user import *



logger = Logging(__name__)


@api.route('/users/<int:user_id>')
class UserResource(Resource):
    @api.marshal_with(responser_user)
    def get(self, user_id):
        logger.info(f"Getting user id ({user_id})")
        return UserService.retrieve_by_id(user_id)
    


@api.route('/users')
class UserResource(Resource):
    @api.marshal_with(responser_user)
    @api.expect(create_user_parser)
    def post(self):
        args = create_user_parser.parse_args()
        new_user =  UserService.create(args)
        logger.info(f"User created succefully ({new_user.username})")
        return {
            "id": new_user.id,
            "email": new_user.email,
            "username": new_user.username,
            "avatar_path": new_user.avatar_path
        }
    @api.expect(token_input_parser)
    def get(sef):
        args = token_input_parser.parse_args()
        access_token = args.get("Authorization")
        logger.info(UserService.get_user_by_access_token(access_token))
        return {
            "msg": "Token Ok"
        }


@api.route('/users/login')
class UserLoginResource(Resource):
    @api.marshal_with(response_login)
    @api.expect(login_user_input)
    def post(self):
        logger.info(f'Login payload {api.payload}')
        return UserService.login(api.payload)


@api.route('/users/confirm')
class UseConfirmResource(Resource):
    @api.expect(confirm_user_input)
    def post(self):
        username = api.payload.get("username")
        logger.info(f'confirming user {username}')
        UserService.confirm_user(username)

@api.route('/users/error')
class UseConfirmResource(Resource):
    def get(self):
        logger.error('Error')
        raise Exception("Error endpoint!")
