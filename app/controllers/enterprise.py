from flask import request, jsonify
from app.usecases.enterprise  import EnterpriseUseCase
from app.dto.enterprise import EnterpriseDTO

class EnterpriseController:
    def __init__(self):
        self.enterprise_usecase = EnterpriseUseCase()

    def create_enterprise(self):
        data = request.get_json()
        enterprise_dto = EnterpriseDTO(**data)
        enterprise = self.enterprise_usecase.create_enterprise(enterprise_dto)
        return jsonify({'id': enterprise.id,
                         'name': enterprise.name,
                         'email': enterprise.email,
                         'phoneNumber': enterprise.phoneNumber,
                         'id_login': enterprise.id_login,
                         'address': enterprise.address,
                         'city': enterprise.city,
                         'state': enterprise.state,
                         'cep': enterprise.cep,
                         'number': enterprise.number,
                         'complement': enterprise.complement,
                         'cnpj': enterprise.cnpj,
                         'status': enterprise.status,
                         })

    def get_enterprise_by_id(self, enterprise_id):
        enterprise = self.enterprise_usecase.get_enterprise_by_id(enterprise_id)
        if enterprise:
            return jsonify({'id': enterprise.id,
                         'name': enterprise.name,
                         'email': enterprise.email,
                         'phoneNumber': enterprise.phoneNumber,
                         'id_login': enterprise.id_login,
                         'address': enterprise.address,
                         'city': enterprise.city,
                         'state': enterprise.state,
                         'cep': enterprise.cep,
                         'number': enterprise.number,
                         'complement': enterprise.complement,
                         'cnpj': enterprise.cnpj,
                         'status': enterprise.status,
                         })

        return jsonify({'message': 'Enterprise not found'}), 404

    def get_all_enterprises(self):
        enterprises = self.enterprise_usecase.get_all_enterprises()
        return jsonify([{'id': enterprise.id,
                         'name': enterprise.name,
                         'email': enterprise.email,
                         'phoneNumber': enterprise.phoneNumber,
                         'id_login': enterprise.id_login,
                         'address': enterprise.address,
                         'city': enterprise.city,
                         'state': enterprise.state,
                         'cep': enterprise.cep,
                         'number': enterprise.number,
                         'complement': enterprise.complement,
                         'cnpj': enterprise.cnpj,
                         'status': enterprise.status,} for enterprise in enterprises])
    
    def update_enterprise(self, enterprise_id):
        data = request.get_json()
        enterprise_dto = EnterpriseDTO(**data)
        enterprise = self.enterprise_usecase.update_enterprise(enterprise_id, enterprise_dto)
        if enterprise:
            return jsonify({'id': enterprise.id,
                         'name': enterprise.name,
                         'email': enterprise.email,
                         'phoneNumber': enterprise.phoneNumber,
                         'id_login': enterprise.id_login,
                         'address': enterprise.address,
                         'city': enterprise.city,
                         'state': enterprise.state,
                         'cep': enterprise.cep,
                         'number': enterprise.number,
                         'complement': enterprise.complement,
                         'cnpj': enterprise.cnpj,
                         'status': enterprise.status,
                         })
        return jsonify({'message': 'Enterprise not found'}), 404
    
    def delete_enterprise(self, enterprise_id):
        enterprise = self.enterprise_usecase.delete_enterprise(enterprise_id)
        if enterprise:
            return jsonify({'message': 'Enterprise deleted'})
        return jsonify({'message': 'Enterprise not found'}), 404
