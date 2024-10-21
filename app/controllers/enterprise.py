from flask import request, jsonify
from app.usecases.enterprise  import EnterpriseUseCase
from app.dto.enterprise import EnterpriseDTO

class EnterpriseController:
    def __init__(self):
        self.enterprise_usecase = EnterpriseUseCase()

    def create_login(self):
        data = request.get_json()
        login_dto = EnterpriseDTO(**data)
        login = self.enterprise_usecase.create_login(login_dto)
        return jsonify({'id': login.id,
                         'name': login.name,
                         'email': login.email,
                         'phoneNumber': login.phoneNumber,
                         'id_login': login.id_login,
                         'address': login.address,
                         'city': login.city,
                         'state': login.state,
                         'cep': login.cep,
                         'number': login.number,
                         'complement': login.complement,
                         'cnpj': login.cnpj,
                         'status': login.status,
                         })

    def get_login_by_id(self, login_id):
        login = self.enterprise_usecase.get_login_by_id(login_id)
        if login:
            return jsonify({'id': login.id,
                         'name': login.name,
                         'email': login.email,
                         'phoneNumber': login.phoneNumber,
                         'id_login': login.id_login,
                         'address': login.address,
                         'city': login.city,
                         'state': login.state,
                         'cep': login.cep,
                         'number': login.number,
                         'complement': login.complement,
                         'cnpj': login.cnpj,
                         'status': login.status,
                         })

        return jsonify({'message': 'Login not found'}), 404

    def get_all_logins(self):
        logins = self.enterprise_usecase.get_all_logins()
        return jsonify([{'id': login.id,
                         'name': login.name,
                         'email': login.email,
                         'phoneNumber': login.phoneNumber,
                         'id_login': login.id_login,
                         'address': login.address,
                         'city': login.city,
                         'state': login.state,
                         'cep': login.cep,
                         'number': login.number,
                         'complement': login.complement,
                         'cnpj': login.cnpj,
                         'status': login.status,} for login in logins])
    
    def update_login(self, user_id):
        data = request.get_json()
        login_dto = EnterpriseDTO(**data)
        login = self.enterprise_usecase.update_login(user_id, login_dto)
        if login:
            return jsonify({'id': login.id,
                         'name': login.name,
                         'email': login.email,
                         'phoneNumber': login.phoneNumber,
                         'id_login': login.id_login,
                         'address': login.address,
                         'city': login.city,
                         'state': login.state,
                         'cep': login.cep,
                         'number': login.number,
                         'complement': login.complement,
                         'cnpj': login.cnpj,
                         'status': login.status,
                         })
        return jsonify({'message': 'Login not found'}), 404
    
    def delete_login(self, login_id):
        login = self.enterprise_usecase.delete_user(login_id)
        if login:
            return jsonify({'message': 'Login deleted'})
        return jsonify({'message': 'Login not found'}), 404
