from flask import Flask, jsonify, request
from models import db, User  # Importamos el DB y el modelo User

app = Flask(__name__)

# Configurando la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
