from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Modelo de usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha_hash = db.Column(db.String(150), nullable=False)

    # Define senha de forma segura
    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    # Verifica a senha
    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
