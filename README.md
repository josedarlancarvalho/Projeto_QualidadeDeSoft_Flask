Projeto de QUALIDADE DE SOFTWARE 

Alunos: José Darlan de Lima Carvalho – 01466857 

Bruno Belarmino da Silva - 24010424 

Turma: 6NA                 Curso: Sistemas da Informação 

# Projeto de Qualidade de Software - Flask

Este projeto é um exemplo prático de boas práticas no desenvolvimento de software utilizando o framework Flask. Ele incorpora testes automatizados, validação de entradas e uma arquitetura organizada para garantir qualidade e confiabilidade no código.

## Pré-requisitos

- Python 3.x instalado.
- Conhecimento básico sobre Flask e pytest.

## Como rodar o projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/josedarlancarvalho/Projeto_QualidadeDeSoft_Flask
   cd Projeto_QualidadeDeSoft_Flask
   ```

2. **Crie e ative um ambiente virtual:**

   No diretório do projeto:
   ```bash
   python3 -m venv venv
   ```

   Ative o ambiente virtual:
   - **Linux/MacOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Rodar os testes:**

   Use o pytest para executar os testes:
   ```bash
   python -m pytest --disable-warnings
   ```

   Este comando executará todos os testes definidos no arquivo de testes, fornecendo um relatório detalhado do que foi validado e destacando erros ou falhas, se houver.

## Descrição dos Testes

Os testes foram desenvolvidos para garantir o funcionamento correto das rotas de cadastro e login do sistema. Eles simulam cenários reais, como entradas inválidas e duplicação de dados. Abaixo está um resumo das principais verificações:

### Configuração de Testes

- **Fixture `cliente`:** Configura um cliente de teste e um banco de dados em memória, permitindo isolamento e limpeza após cada execução de teste.

### Testes Implementados

1. **Cadastro de Usuário**
   - Cadastro com dados completos e válidos.
   - Tentativa de cadastro com campos obrigatórios ausentes (email, senha ou username).
   - Verificação de validação para senhas curtas (menos de 8 caracteres).
   - Prevenção de cadastro com emails duplicados.

2. **Login de Usuário**
   - Tentativa de login sem fornecer email ou senha.
   - Teste de credenciais inválidas (email ou senha incorretos).
   - Login bem-sucedido com credenciais corretas.

### Estrutura do Arquivo de Testes

O arquivo de testes (`test_app.py`) utiliza o `pytest` para validação. Ele cobre cenários chave para as principais funcionalidades do sistema:
- Uso do `cliente` para simular requisições às rotas `/cadastro` e `/login`.
- Verificações de códigos de status HTTP e mensagens de erro ou sucesso no retorno.

Exemplo de um teste de cadastro bem-sucedido:
```python
def test_cadastro_completo(cliente):
    resposta = cliente.post('/cadastro', json={
        'username': 'novo_user',
        'email': 'novo@teste.com',
        'senha': 'senha1234'
    })
    assert resposta.status_code == 201
    assert resposta.get_json()['mensagem'] == 'Cadastro realizado com sucesso!'
```

## Funcionalidades do Projeto

- Rotas protegidas por validações.
- Testes automatizados para garantir a integridade do código.
- Banco de dados em memória para execução rápida e limpa dos testes.

## Contribuindo

Se você deseja contribuir para este projeto, faça um fork, crie uma branch com suas alterações e envie um pull request. Certifique-se de que suas mudanças passam nos testes antes de enviar.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
