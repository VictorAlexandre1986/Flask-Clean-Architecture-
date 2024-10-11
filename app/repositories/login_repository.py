from app.models.login import LoginUser,get_db


class LoginRepository:
    def create(self, login_data):
        db = get_db()
        login = LoginUser(username=login_data.username, password=login_data.password, email=login_data.email)
        db.session.add(login)
        db.session.commit()
        return login

    def get_by_id(self, login_id):
        return LoginUser.query.get(login_id)
    
    def get_all(self):
        return LoginUser.query.all()
    
    def update(self, login_id, login_data):
        db = get_db()
        login = LoginUser.query.get(login_id)
        if login:
            login.username = login_data.username
            login.password = login_data.password
            login.email = login_data.email
            db.session.commit()
        return login
    
    def delete(self, login_id):
        db = get_db()
        login = LoginUser.query.get(login_id)
        if login:
            db.session.delete(login)
            db.session.commit()
        return login