from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Modelo de usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)  

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha) 

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)  

