from flask_restful import Resource, reqparse
from app.models import usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from blacklist import BLACKLIST
from app import db

class User_modelo(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('senha')
    
    #@jwt_required()
    def get(self):
        return {'Usuarios': [usuario.json() for usuari in usuario.query.all()]}
    
    def post(self):
        dados = User_modelo.argumetos.parse_args()
        users = usuario(**dados) #ponteiros
        db.session.add(users)
        db.session.commit()
        return users.json(), 201 #acessou a pagina na web esta disponiel

class Users_modelo(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('senha')

    #@jwt_required()
    def get(self, id):
        users = usuario.query.filter_by(id=id).first()
        if users:
            return users.json()
        return {'message': 'Usuario inexistente'}, 404 # web nao existente 
    
    #@jwt_required()
    def put(self, id):
        dados = Users_modelo.argumentos.parse_args()
        users = usuario(**dados)
        user_encontrado = usuario.query.filter_by(id=id).first()
        if user_encontrado:
            user_encontrado.query.filter_by(id=id).update({**dados})
            db.session.commit()
            return user_encontrado.json(), 200
        db.session.add()
        db.session.commit()
        return users.json(), 201
    
    #@jwt_required()
    def delete(self, id):
        users = usuario.query.filter_by(id=id).first()
        if users:
            db.session.delete(users)
            db.session.commit()
            return {'message': 'Usuario excluido com sucesso.'}
        return {'message': 'Usuario inexistente.'}, 404
        
    
    
        
    
    
    
