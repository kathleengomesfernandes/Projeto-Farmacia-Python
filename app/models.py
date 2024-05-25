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
    
    def json(self):
        return{
            'id': self.id,
            'email':self.email,
            'nome':self.nome,
            'senha':self.senha
        }  
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
    descricao = db.Column(db.String(255), nullable=True)
    insumos = db.Column(db.String(255), nullable=True)
    quantidade = db.Column(db.String(255), nullable=True)
    valor = db.Column(db.String(255), nullable=True)
class produtos(db.Model):
    __tablename__ = "produtos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    qr_code_produto = db.Column(db.String(255), nullable=True)
    observacao = db.Column(db.String(255), nullable=True)
    conservacao = db.Column(db.String(255), nullable=True)
    data_validade = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class notas(db.Model):
    __tablename__ = "notas"
    id = db.Column(db.Integer, primary_key=True)
    num_nf = db.Column(db.String(255), nullable=True)
    valor = db.Column(db.String(255), nullable=True)
    data_emissao = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    descricao = db.Column(db.String(255), nullable=True)
