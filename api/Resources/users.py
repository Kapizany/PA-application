from flask_restx import Resource
from config.api import api
from api.Services.user import UserService

@api.route('/users/<string:user_id>')
class UserResource(Resource):
    def get(self, user_id):
        return UserService.retrieve_by_id(user_id)