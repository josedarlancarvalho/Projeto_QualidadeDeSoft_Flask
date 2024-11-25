from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria o banco de dados e tabelas se não existirem
    app.run(debug=True)
