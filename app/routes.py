from flask import request, jsonify
from app import app
from app.services import create_user, authenticate_user

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = create_user(data['name'], data['email'], data['password'])
        return jsonify({"message": f"Usuário {user.name} criado com sucesso"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = authenticate_user(data['email'], data['password'])
        return jsonify({"message": f"Bem-vindo, {user.name}"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
