from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db

def create_user(name, email, password):
    if User.query.filter_by(email=email).first():
        raise ValueError("Email já cadastrado")
    if len(password) < 8 or not any(char.isdigit() for char in password):
        raise ValueError("A senha deve ter pelo menos 8 caracteres e incluir pelo menos um número")
    
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        raise ValueError("Credenciais inválidas")
    return user
