from api.Models.user import UserModel
from werkzeug.exceptions import BadRequest

class UserService:
    
    @staticmethod
    def retrieve_by_id(user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            raise BadRequest("User not found!")