from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

# , template_folder='src/templates
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my_secret@localhost/contacts_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:my_secret@localhost/contacts_app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
'''
Los blueprints permiten organizar las rutas de la aplicacion, para llamar a esas rutas
desde el archivo de configuracion registramos la blueprint como se muestra a continuacion
'''

app.register_blueprint(contacts)
