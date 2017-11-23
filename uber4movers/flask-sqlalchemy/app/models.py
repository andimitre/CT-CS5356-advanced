from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    user_jobs = db.relationship('Jobs', backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Mover(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100))
    vehicle = db.Column(db.String(200))
    image_url = db.Column(db.String(4000))
    phone = db.Column(db.String(50))
    mover_jobs = db.relationship('Jobs', backref="mover", lazy=True)

    def __repr__(self):
        return '<Mover %r>' % (self.name)

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mover_id = db.Column(db.Integer, db.ForeignKey('mover.id'))
    num_of_rooms = db.Column(db.Integer)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    price = db.Column(db.Float)
    description = db.Column(db.String(4000))
    # mover = db.relationship("Mover", back_populates="mover_jobs")

    def __repr__(self):
        return '<Job %r>' % (self.id)
