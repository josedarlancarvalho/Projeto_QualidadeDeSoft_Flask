import pytest
from app import app, db
from app.models import Usuario

@pytest.fixture
def cliente():
    # Configura o ambiente de teste
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco de dados temporário
    with app.test_client() as cliente:
        with app.app_context():
            db.create_all()  # Cria tabelas para o teste
        yield cliente
        with app.app_context():
            db.session.remove()
            db.drop_all()  # Remove tabelas após o teste

def test_cadastro_sem_email_ou_senha(cliente):
    resposta = cliente.post('/cadastro', json={'email': '', 'senha': 'senha123'})
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Email e senha são obrigatórios.'

def test_cadastro_senha_curta(cliente):
    resposta = cliente.post('/cadastro', json={'email': 'teste@teste.com', 'senha': '123'})
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'A senha deve ter pelo menos 8 caracteres.'

def test_cadastro_email_duplicado(cliente):
    cliente.post('/cadastro', json={'email': 'teste@teste.com', 'senha': 'senha123'})
    resposta = cliente.post('/cadastro', json={'email': 'teste@teste.com', 'senha': 'senha1234'})
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Email já cadastrado.'

def test_login_sem_email_ou_senha(cliente):
    resposta = cliente.post('/login', json={'email': '', 'senha': ''})
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Email e senha são obrigatórios.'

def test_login_credenciais_invalidas(cliente):
    resposta = cliente.post('/login', json={'email': 'naoexiste@teste.com', 'senha': 'senha123'})
    assert resposta.status_code == 401
    assert resposta.get_json()['erro'] == 'Credenciais inválidas.'

@app.route('/cadastro', methods=['POST'])
def cadastro():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')

    if not email or not senha:
        return jsonify({'erro': 'Email e senha são obrigatórios.'}), 400

    if len(senha) < 8:
        return jsonify({'erro': 'A senha deve ter pelo menos 8 caracteres.'}), 400

    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return jsonify({'erro': 'Email já cadastrado.'}), 400

    novo_usuario = Usuario(email=email, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso.'}), 201
