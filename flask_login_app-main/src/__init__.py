from flask import Flask, render_template, redirect, request, url_for
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from src.models.ModeloUsuario import ModeloUsuario
from src.models.Usuario import Usuario

app = Flask(__name__)
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.get_id(db, id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        usuario = Usuario(
            None, user, password, None)
        logged_user = ModeloUsuario.login(db, usuario)
        print(logged_user)  # None
        if logged_user != None:
            login_user(logged_user)
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @app.route('/modelo_usuario')
# def modelo():
#     return ModeloUsuario.get_by_id(db, id)


# @app.route('/password/<password>')
# def password(password):
#     password_hash = generate_password_hash(password)
#     # checked = check_password_hash(password_hash, password)
#     return password_hash

def start_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    return app
