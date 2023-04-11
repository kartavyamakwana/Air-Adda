from airline import *
def test():
    with app.app_context():
        db.drop_all()
        db.create_all()

test()