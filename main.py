from flask import Flask, jsonify
from flask_restful import Api
from app import create_app
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from app.recursos import User_modelo
from app.recursos import Users_modelo

app = create_app()
api = Api(app)
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'message': 'Você saiu do sistema.'}), 401

api.add_resource(User_modelo, '/user_api')
api.add_resource(Users_modelo, '/user_api/<string:id>')

if __name__ == "__main__":
    
    app.run(debug=True)