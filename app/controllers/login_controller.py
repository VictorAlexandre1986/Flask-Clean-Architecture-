from flask import request, jsonify
from app.usecases.login  import LoginUseCase
from app.dto.login import LoginDTO

class LoginController:
    def __init__(self):
        self.login_usecase = LoginUseCase()

    def create_login(self):
        data = request.get_json()
        login_dto = LoginDTO(**data)
        login = self.login_usecase.create_login(login_dto)
        return jsonify({'id': login.id, 'username': login.username, 'password': login.password, 'email': login.email})

    def get_login_by_id(self, login_id):
        login = self.login_usecase.get_login_by_id(login_id)
        if login:
            return jsonify({'id': login.id, 'username': login.username, 'password': login.password, 'email': login.email})
        return jsonify({'message': 'Login not found'}), 404

    def get_all_logins(self):
        logins = self.login_usecase.get_all_logins()
        return jsonify([{'id': login.id, 'username': login.username, 'password': login.password ,'email': login.email} for login in logins])
    
    def update_login(self, user_id):
        data = request.get_json()
        login_dto = LoginDTO(**data)
        login = self.login_usecase.update_login(user_id, login_dto)
        if login:
            return jsonify({'id': login.id, 'username': login.username, 'password': login.password ,'email': login.email})
        return jsonify({'message': 'Login not found'}), 404
    
    def delete_login(self, login_id):
        login = self.user_usecase.delete_user(login_id)
        if login:
            return jsonify({'message': 'Login deleted'})
        return jsonify({'message': 'Login not found'}), 404
