
# Projeto de Qualidade de Software - Flask

Este é um projeto desenvolvido em Python utilizando o framework Flask, com o objetivo de implementar boas práticas de desenvolvimento de software e testes automatizados, utilizando ferramentas como o pytest.

## Pré-requisitos

Para rodar o projeto corretamente, você precisa ter o Python 3 instalado. Além disso, será necessário criar um ambiente virtual e instalar as dependências do projeto. Siga os passos abaixo para configurar o ambiente de desenvolvimento:

## Como rodar o projeto

1. **Clone o repositório:**

   Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/josedarlancarvalho/Projeto_QualidadeDeSoft_Flask
   ```

2. **Crie e ative um ambiente virtual:**

   No diretório do projeto, crie um ambiente virtual:
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

   Instale todas as dependências necessárias do projeto:
   ```bash
   pip install -r requirements.txt
   ```

4. **Rodar os testes:**

   Para rodar os testes automatizados com pytest, execute o seguinte comando:
   ```bash
   python -m pytest --disable-warnings
   ```

   Este comando irá executar os testes definidos no projeto e desabilitar os avisos (warnings).

## Descrição do Projeto

Este projeto tem como objetivo aplicar os conceitos de qualidade de software no desenvolvimento de um aplicativo Flask. A aplicação implementa funcionalidades simples, porém, com foco em boas práticas de codificação, como a utilização de testes unitários e integração com ferramentas de teste automatizado.

### Funcionalidades do Projeto
- Implementação de rotas simples em Flask.
- Testes unitários para validar a funcionalidade da aplicação.
- Uso do pytest para a execução dos testes.

## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para fazer um fork, criar uma branch com suas modificações e enviar um pull request. Certifique-se de que seus commits sigam as convenções do projeto e que os testes estejam funcionando corretamente.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
