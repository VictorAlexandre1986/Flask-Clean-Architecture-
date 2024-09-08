from flask import Blueprint
from app.controllers.user_controller import UserController
from flask  import jsonify

api_routes = Blueprint('api_routes', __name__)

user_controller = UserController()

@api_routes.route('/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@api_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return user_controller.get_user_by_id(user_id)

@api_routes.route('/users', methods=['GET'])
def get_all_users():
    return user_controller.get_all_users()
   

@api_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update_user(user_id)

@api_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)
