import db
from werkzeug.security import check_password_hash, generate_password_hash
from app import app

def populate_users(amount=10):
    with app.app_context():
        for i in range(amount):
            username = f"user{i}"
            password = f"pass{i}"
            password_hash = generate_password_hash(password)
            sql = "INSERT INTO users (username, password_hash, isAdmin) VALUES (?, ?, ?)"
            db.execute(sql, [username, password_hash, 0])

populate_users(10)