from app.models.login_enterprise import LoginEnterprise,get_db


class LoginEnterpriseRepository:
    def create(self, login_data):
        db = get_db()
        login = LoginEnterprise(username=login_data.username, password=login_data.password, email=login_data.email)
        db.session.add(login)
        db.session.commit()
        return login

    def get_by_id(self, login_id):
        return LoginEnterprise.query.get(login_id)
    
    def get_all(self):
        return LoginEnterprise.query.all()
    
    def update(self, login_id, login_data):
        db = get_db()
        login = LoginEnterprise.query.get(login_id)
        if login:
            login.username = login_data.username
            login.password = login_data.password
            login.email = login_data.email
            db.session.commit()
        return login
    
    def delete(self, login_id):
        db = get_db()
        login = LoginEnterprise.query.get(login_id)
        if login:
            db.session.delete(login)
            db.session.commit()
        return login