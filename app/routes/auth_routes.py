from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from app import app, db
from app.models import Usuario
from sqlalchemy.exc import IntegrityError

@app.route('/cadastro', methods=['POST'])
def cadastro():
    """Processa o cadastro de usuário"""
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    senha = data.get('senha')

    # Validação de campos obrigatórios
    if not username or not email or not senha:
        return jsonify({'erro': 'Email, senha e username são obrigatórios.'}), 400

    # Validação do tamanho da senha
    if len(senha) < 8:
        return jsonify({'erro': 'A senha deve ter pelo menos 8 caracteres.'}), 400

    # Validação de email duplicado
    if Usuario.query.filter_by(email=email).first():
        return jsonify({'erro': 'Email já cadastrado.'}), 400

    # Criação do novo usuário
    novo_usuario = Usuario(username=username, email=email)
    novo_usuario.set_senha(senha)

    try:
        db.session.add(novo_usuario)
        db.session.commit()
        return jsonify({'mensagem': 'Cadastro realizado com sucesso!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'erro': 'Nome de usuário já existe. Tente outro.'}), 400

@app.route('/login', methods=['POST'])
def login():
    """Processa o login de usuário"""
    data = request.get_json()

    email = data.get('email')
    senha = data.get('senha')

    # Validação de campos obrigatórios
    if not email or not senha:
        return jsonify({'erro': 'Email e senha são obrigatórios.'}), 400

    # Procurar usuário no banco
    usuario = Usuario.query.filter_by(email=email).first()

    # Verificação de credenciais
    if not usuario or not usuario.check_senha(senha):
        return jsonify({'erro': 'Credenciais inválidas.'}), 401

    # Login bem-sucedido
    return jsonify({'mensagem': 'Login realizado com sucesso.'}), 200
