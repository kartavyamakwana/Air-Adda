from airline import db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username},'{self.email}','{self.image_file}')"

class Flight(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    take_off_terminal = db.Column(db.Integer)
    take_off_airport = db.Column(db.String(20),nullable=False)
    dest_terminal = db.Column(db.Integer)
    dest_airport = db.Column(db.String(20),nullable=False)
    take_off_time = db.Column(db.DateTime)
    landing_time = db.Column(db.DateTime)
    
class Airport(db.Model):
    airport_id = db.Column(db.String(20),primary_key=True)
    airport_name = db.Column(db.String(20))
    airport_type = db.Column(db.String(20))
    capacity = db.Column(db.Integer)
    no_of_terminals = db.Column(db.Integer)

class Passenger(db.Model):
    pid = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    passport_id = db.Column(db.String(20))
    ticket_id = db.Column(db.String(20),db.ForeignKey('ticket.id'))

class Ticket(db.Model):
    id = db.Column(db.String(20),primary_key=True)
    flight_code = db.Column(db.String(20),db.ForeignKey('flight.id'))
    total_amount = db.Column(db.Integer)
    adult_pass = db.Column(db.Integer)
    child_pass = db.Column(db.Integer,default=0)
    seat_no = db.Column(db.Integer)
    paid_via = db.Column(db.String(20))
    transaction_id = db.Column(db.String(20))