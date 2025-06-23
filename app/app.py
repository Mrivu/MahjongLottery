from flask import Flask
from flask import Blueprint, redirect, render_template, request, session, url_for
import config
import user_manager

app = Flask(__name__, static_url_path='/mahjonglottery/static', static_folder='static')
app.secret_key = config.secret_key

bp = Blueprint('bp', __name__)

@app.route('/')
def root():
    return redirect(url_for('bp.login'))

@bp.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", message="")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_manager.login(username, password):
            return redirect(url_for('bp.main'))
        return render_template("login.html", message="Incorrect username or password")

@bp.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", message="")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        result = user_manager.register_user(username, password1, password2)
        if result == 0:
            # reg fail nomatch
            return render_template("register.html", message = "The passwords don't match")
        elif result == 1:
            # reg fail taken
            return render_template("register.html", message = f"The username {username} is aready taken")
        return redirect(url_for('bp.main'))
    
@bp.route("/main", methods = ["GET"])
def main():
    if request.method == "GET":
        user_manager.require_login(request)
        return render_template("main.html", message="")

app.register_blueprint(bp, url_prefix='/mahjonglottery/')
