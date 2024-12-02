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
            
            # Adiciona um usuário de teste
            usuario_teste = Usuario(email='teste@teste.com', senha='senha123')
            db.session.add(usuario_teste)
            db.session.commit()
        
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

def test_login_credenciais_validas(cliente):
    resposta = cliente.post('/login', json={'email': 'teste@teste.com', 'senha': 'senha123'})
    assert resposta.status_code == 200
    assert resposta.get_json()['mensagem'] == 'Login realizado com sucesso.'
