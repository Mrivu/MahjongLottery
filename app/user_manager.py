from werkzeug.security import check_password_hash, generate_password_hash
import db
from flask import session, abort, redirect, render_template, url_for
import secrets
import sqlite3
import config

def require_login(request):
    if "userID" not in session:
        abort(403)
    if request.method == "POST":
        token = request.form.get("csrf_token")
        if not token or token != session.get("csrf_token"):
            abort(403)

def require_admin():
    if not session["isAdmin"]:
        abort(403)

def logout():
    session.clear()
    return redirect(url_for('bp.login'))
    
def login(username, password):
    sql_password = "SELECT password_hash FROM users WHERE username = ?"
    password_hash = db.query(sql_password, [username])
    if password_hash:
        password_hash = password_hash[0][0]
        if check_password_hash(password_hash, password):
            session["username"] = username
            getAdminStatus = "SELECT isAdmin FROM users WHERE username = ?"
            isAdmin = db.query(getAdminStatus, [username])
            session["isAdmin"] = isAdmin[0][0]
            getID = db.query("SELECT userID FROM users where username = ?", [session["username"]])
            session["userID"] = getID[0][0]
            session["csrf_token"] = secrets.token_hex(16)
            return True
        
def register_user(username, password1, password2):
    if password1 != password2:
        return 0
    if db.query("SELECT * FROM users WHERE username = ?", [username]):
        return 1
    password_hash = generate_password_hash(password1)
    sql = "INSERT INTO users (username, password_hash, isAdmin) VALUES (?, ?, ?)"
    db.execute(sql, [username, password_hash, 0])
    session["username"] = username
    session["isAdmin"] = 0
    getID = db.query("SELECT userID FROM users where username = ?", [session["username"]])
    session["userID"] = getID[0][0]
    session["csrf_token"] = secrets.token_hex(16)