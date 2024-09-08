from app.models.user import User,get_db


class UserRepository:
    def create(self, user_data):
        db = get_db()
        user = User(name=user_data.name, email=user_data.email)
        db.session.add(user)
        db.session.commit()
        return user

    def get_by_id(self, user_id):
        return User.query.get(user_id)
    
    def get_all(self):
        return User.query.all()
    
    def update(self, user_id, user_data):
        db = get_db()
        user = User.query.get(user_id)
        if user:
            user.name = user_data.name
            user.email = user_data.email
            db.session.commit()
        return user
    
    def delete(self, user_id):
        db = get_db()
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
