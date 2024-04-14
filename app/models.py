from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return usuario.query.get(user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255),nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())     
class clientes(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    empresa = db.Column(db.String(255), nullable=True)

class pedidos(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    num_pedido = db.Column(db.String(255), nullable=True)
    materia_prima = db.Column(db.String(255), nullable=True)
class produtos(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    qr_code_produto = db.Column(db.String(255), nullable=True)
    reacao = db.Column(db.String(255), nullable=True)
    conservacao = db.Column(db.String(255), nullable=True)
    data_validade = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

