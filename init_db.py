from app import app, db

# app.app_context().push
# db.create_all()

with app.app_context():
    db.create_all()