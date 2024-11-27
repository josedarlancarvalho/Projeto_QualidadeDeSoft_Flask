from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa o app e o banco de dados
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Banco SQLite local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importa rotas após a criação do app e banco
from app.routes import auth_routes
