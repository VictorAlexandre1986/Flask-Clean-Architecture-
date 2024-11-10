from flask import Blueprint
from app.controllers.user_controller import UserController
from app.controllers.login_controller import LoginController
from app.controllers.login_enterprise_controller import LoginEnterpriseController
from app.controllers.enterprise import EnterpriseController
from flask  import jsonify

api_routes = Blueprint('api_routes', __name__)

user_controller = UserController()

login_controller = LoginController()

login_enterprise_controller = LoginEnterpriseController()

enterprise_controller = EnterpriseController()

#---------------------Rotas Login----------------------------
@api_routes.route('/login', methods=['POST'])
def create_login():
    return login_controller.create_login()

@api_routes.route('/login/<int:login_id>', methods=['GET'])
def get_login_by_id(login_id):
    return login_controller.get_login_by_id(login_id)

@api_routes.route('/login', methods=['GET'])
def get_all_logins():
    return login_controller.get_all_logins()

@api_routes.route('/login/<int:login_id>', methods=['PUT','PATCH'])
def update_login(login_id):
    return login_controller.update_login(login_id)

@api_routes.route('/login/<int:login_id>', methods=['DELETE'])
def delete_login(login_id):
    return login_controller.delete_login(login_id)


#---------------------Rotas User----------------------------
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

#---------------------Rotas Login Enterprise----------------------
@api_routes.route('/loginenterprise', methods=['POST'])
def create_login_enterprise():
    return login_enterprise_controller.create_login()

@api_routes.route('/loginenterprise/<int:login_id>', methods=['GET'])
def get_login_enterprise_by_id(login_id):
    return login_enterprise_controller.get_login_by_id(login_id)

@api_routes.route('/loginenterprise', methods=['GET'])
def get_all_logins_enterprises():
    return login_enterprise_controller.get_all_logins()

@api_routes.route('/loginenterprise/<int:login_id>', methods=['PUT','PATCH'])
def update_login_enterprise(login_id):
    return login_enterprise_controller.update_login(login_id)

@api_routes.route('/loginenterprise/<int:login_id>', methods=['DELETE'])
def delete_login_enterprise(login_id):
    return login_enterprise_controller.delete_login(login_id)

#---------------------Rotas Enterprise----------------------
@api_routes.route('/enterprise', methods=['POST'])
def create_enterprise():
    return enterprise_controller.create_enterprise()

@api_routes.route('/enterprise/<int:enterprise_id>', methods=['GET'])
def get_enterprise_by_id(enterprise_id):
    return enterprise_controller.get_enterprise_by_id(enterprise_id)

@api_routes.route('/enterprise', methods=['GET'])
def get_all_enterprises():
    return enterprise_controller.get_all_enterprises()

@api_routes.route('/enterprise/<int:enterprise_id>', methods=['PUT'])
def update_enterprise(enterprise_id):
    return enterprise_controller.update_enterprise(enterprise_id)

@api_routes.route('/enterprise/<int:enterprise_id>', methods=['DELETE'])
def delete_enterprise(enterprise_id):
    return enterprise_controller.delete_enterprise(enterprise_id)


