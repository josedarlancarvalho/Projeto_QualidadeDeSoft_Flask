from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from app import app, db
from app.models import Usuario
from sqlalchemy.exc import IntegrityError

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form.get('username')  # Captura do campo username
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not username or not email or not senha:
            return render_template('cadastro.html', mensagem_erro='Todos os campos são obrigatórios.')

        if len(senha) < 8:
            return render_template('cadastro.html', mensagem_erro='A senha deve ter pelo menos 8 caracteres.')

        if Usuario.query.filter_by(email=email).first():
            return render_template('cadastro.html', mensagem_erro='Email já cadastrado.')

        novo_usuario = Usuario(username=username, email=email)
        novo_usuario.set_senha(senha)

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            return render_template('login.html', mensagem_sucesso='Cadastro realizado com sucesso!')
        except IntegrityError:
            db.session.rollback()  # Desfaz a transação em caso de erro
            return render_template('cadastro.html', mensagem_erro='Nome de usuário já existe. Tente outro.')

    return render_template('cadastro.html', mensagem_erro=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Validar se os campos foram preenchidos
        if not email or not senha:
            return render_template('login.html', mensagem_erro='Email e senha são obrigatórios.')

        # Procurar usuário no banco
        usuario = Usuario.query.filter_by(email=email).first()

        # Verificar credenciais
        if not usuario or not usuario.check_senha(senha):
            return render_template('login.html', mensagem_erro='Credenciais inválidas.')

        # Login bem-sucedido
        return render_template('login.html', mensagem_sucesso=f'Bem-vindo, {email}!')

    return render_template('login.html', mensagem_erro=None)
