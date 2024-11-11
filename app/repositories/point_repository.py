from app.models.point import Point,get_db


class PointRepository:
    def create(self, data):
        db = get_db()
        point = Point(date=data.date, photo=data.photo, id_user=data.id_user, total_hours=data.total_hours, pause=data.pause)
        db.session.add(point)
        db.session.commit()
        return point

    def get_by_id(self, point_id):
        return Point.query.get(point_id)
    
    def get_all(self):
        return Point.query.all()
    
    def update(self, point_id, data):
        db = get_db()
        point = Point.query.get(point_id)
        if point:
            point.date = data.date
            point.photo = data.photo
            point.id_user = data.id_user
            point.total_hours = data.total_hours
            point.pause = data.pause
            db.session.commit()
        return point
    
    def delete(self, point_id):
        db = get_db()
        point = Point.query.get(point_id)
        if point:
            db.session.delete(point)
            db.session.commit()
        return point