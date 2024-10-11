from flask import request, jsonify
from app.usecases.user  import UserUseCase
from app.dto.user import UserDTO
from app.entities.user import UserEntity

class UserController:
    def __init__(self):
        self.user_usecase = UserUseCase()

    def create_user(self):
        data = request.get_json()
        user_dto = UserDTO(**data)
        user = self.user_usecase.create_user(user_dto)
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'photo': user.photo, 'phoneNumber': user.phoneNumber , 'id_login': user.id_login})

    def get_user_by_id(self, user_id):
        user = self.user_usecase.get_user_by_id(user_id)
        if user:
            return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'photo': user.photo, 'phoneNumber': user.phoneNumber , 'id_login': user.id_login})
            
        return jsonify({'message': 'User not found'}), 404

    def get_all_users(self):
        users = self.user_usecase.get_all_users()
        return jsonify([{'id': user.id, 'name': user.name, 'email': user.email, 'photo': user.photo, 'phoneNumber': user.phoneNumber , 'id_login': user.id_login} for user in users])
    
    def update_user(self, user_id):
        data = request.get_json()
        user_dto = UserDTO(**data)
        user = self.user_usecase.update_user(user_id, user_dto)
        if user:
            return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'photo': user.photo, 'phoneNumber': user.phoneNumber , 'id_login': user.id_login})
        return jsonify({'message': 'User not found'}), 404
    
    def delete_user(self, user_id):
        user = self.user_usecase.delete_user(user_id)
        if user:
            return jsonify({'message': 'User deleted'})
        return jsonify({'message': 'User not found'}), 404
