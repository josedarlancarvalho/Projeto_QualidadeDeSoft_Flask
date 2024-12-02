from app import app, db
from app.models import Usuario
import pytest

@pytest.fixture
def cliente():
    """Configura o cliente de teste e o banco de dados em memória."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as cliente:
        with app.app_context():
            db.create_all()
            # Criação de um usuário de teste
            usuario_teste = Usuario(username='teste', email='teste@teste.com')
            usuario_teste.set_senha('senha123')
            db.session.add(usuario_teste)
            db.session.commit()

        yield cliente

        # Limpeza após os testes
        with app.app_context():
            db.session.remove()
            db.drop_all()

def setup_test_data():
    if not Usuario.query.filter_by(email='teste@teste.com').first():
        usuario_teste = Usuario(email='teste@teste.com', senha='senha123', username='user_teste')
        db.session.add(usuario_teste)
        db.session.commit()

def test_cadastro_completo(cliente):
    """Testa o cadastro com informações completas e válidas."""
    resposta = cliente.post('/cadastro', json={
        'username': 'novo_user',
        'email': 'novo@teste.com',
        'senha': 'senha1234'
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['mensagem'] == 'Cadastro realizado com sucesso!'

def test_cadastro_sem_email_ou_senha(cliente):
    """Testa o cadastro sem email, senha ou username."""
    resposta = cliente.post('/cadastro', json={
        'username': '',
        'email': '',
        'senha': ''
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Email, senha e username são obrigatórios.'

def test_cadastro_senha_curta(cliente):
    """Testa o cadastro com senha menor que 8 caracteres."""
    resposta = cliente.post('/cadastro', json={
        'username': 'user_curto',
        'email': 'curto@teste.com',
        'senha': '123'
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'A senha deve ter pelo menos 8 caracteres.'

def test_cadastro_email_duplicado(cliente):
    """Testa o cadastro com um email já existente no banco de dados."""
    with app.app_context():
        setup_test_data()
    resposta = cliente.post('/cadastro', json={
        'username': 'darlan',
        'email': 'teste@teste.com',  # Email duplicado
        'senha': 'senha1234'
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Email já cadastrado.'


def test_login_sem_email_ou_senha(cliente):
    """Testa o login sem email e senha."""
    resposta = cliente.post('/login', json={
        'email': '',
        'senha': ''
    })
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Email e senha são obrigatórios.'

def test_login_credenciais_invalidas(cliente):
    """Testa o login com credenciais incorretas."""
    resposta = cliente.post('/login', json={
        'email': 'naoexiste@teste.com',
        'senha': 'senha1234'
    })
    assert resposta.status_code == 401
    assert resposta.get_json()['erro'] == 'Credenciais inválidas.'

def test_login_credenciais_validas(cliente):
    """Testa o login com credenciais corretas."""
    resposta = cliente.post('/login', json={
        'email': 'teste@teste.com',
        'senha': 'senha123'
    })
    assert resposta.status_code == 200
    assert resposta.get_json()['mensagem'] == 'Login realizado com sucesso.'
