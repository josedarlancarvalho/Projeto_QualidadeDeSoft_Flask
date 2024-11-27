from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Certifica-se de que as tabelas foram criadas
    app.run(debug=True)
