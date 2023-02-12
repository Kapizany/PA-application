from flask_restx import Resource, fields, reqparse
from werkzeug.datastructures import FileStorage
from config.api import api
from api.Services.user import UserService


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


@api.route('/users/<string:user_id>')
class UserResource(Resource):
    @api.marshal_with(responser_user)
    def get(self, user_id):
        return UserService.retrieve_by_id(user_id)


@api.route('/users')
class UserResource(Resource):
    @api.marshal_with(responser_user)
    @api.expect(create_user_parser)
    def post(self):
        args = create_user_parser.parse_args()
        new_user =  UserService.create(args)
        return {
            "id": new_user.id,
            "email": new_user.email,
            "username": new_user.username,
            "avatar_path": new_user.avatar_path
        }


@api.route('/users/login')
class UserLoginResource(Resource):
    @api.marshal_with(responser_user)
    @api.expect(login_user_input)
    def post(self):
        return UserService.login(api.payload)