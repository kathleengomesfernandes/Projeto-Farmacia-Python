from app.models import usuario
from app.models import clientes
from app.models import pedidos
from app.models import produtos
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def init_app(app):
        
    #@app.route("/")
    #def principal():        
        #return render_template("seu_job/index.html")
    
    @app.route("/")
    def inicio():        
        return render_template("/inicio.html", usuarios=db.session.execute(db.select(usuario).order_by(usuario.id)).scalars())
    
    @app.route("/cliente")
    def cliente():        
        return render_template("/cliente.html", client=db.session.execute(db.select(clientes).order_by(clientes.id)).scalars())
    
    @app.route("/excluir/<int:id>")
    def excluir_user(id):
        delete=usuario.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("inicio"))
    
    @app.route("/excluir_cli/<int:id>")
    def excluir_cli(id):
        delete=clientes.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("cliente"))
    
    @app.route("/pedido")
    def pedido():        
        return render_template("pedido.html", ped=db.session.execute(db.select(pedidos).order_by(pedidos.id)).scalars())
    
    @app.route("/excluir_pedi/<int:id>")
    def excluir_pedi(id):
        delete=pedidos.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("pedido"))
    
    @app.route("/produto")
    def produto():        
        return render_template("produto.html", prod=db.session.execute(db.select(produtos).order_by(produtos.id)).scalars())

    @app.route("/excluir_pdts/<int:id>")
    def excluir_pdts(id):
        delete=produtos.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("produto"))
    
    @app.route("/nota_fiscal")
    def nota_fiscal():        
        return render_template("nota_fiscal.html")
    
    
    
    @app.route("/cad_prod", methods=["GET", "POST"])
    def cad_prod():        
        if request.method =="POST":
            prod = produto()
            prod.nome = request.form["nome"].nome 
            prod.qr_code_produto = request.form["qr_code_produto"]
            prod.reacao = request.form["reacao"].reacao 
            prod.conservacao = request.form["conservacao"]
            db.session.add(prod)
            db.session.commit()

            flash("Produto criado com sucesso!")
            return redirect(url_for("cad_prod"))
        return render_template("cad_prod.html")
    
    @app.route("/cad_cliente")
    def cad_cliente():        
        return render_template("cad_cliente.html")
    
    @app.route("/cad_user", methods=["GET", "POST"])
    def cad_user():        
        if request.method =="POST":
            user = usuario()
            user.email = request.form["email"]
            user.nome = request.form["nome"]
            user.senha = generate_password_hash(request.form["senha"])
            db.session.add(user)
            db.session.commit()

            flash("Usuário criado com sucesso!")
            return redirect(url_for("cad_user"))
        return render_template("cad_user.html")
    
    @app.route("/cad_pedido")
    def cad_pedido():        
        return render_template("cad_pedido.html")
    
    @app.route("/cad_NF")
    def cad_NF():        
        return render_template("cad_NF.html")
    
    
    
    @app.route("/atualiza_user/<int:id>", methods=["GET", "POST"])
    def atualiza_user(id): 
        users=usuario.query.filter_by(id=id).first() 
        if request.method == "POST":
            nome_usuario = request.form["nome"]
            email_usuario = request.form["email"]
            senha_usuario = generate_password_hash(request.form["senha"])
            
            flash("Dados do usuário alterado com sucesso!")
            users.query.filter_by(id=id).update({"nome":nome_usuario, "email":email_usuario, "senha":senha_usuario})
            db.session.commit()
            return redirect(url_for("inicio"))
        return render_template("atualiza_user.html", usua=users)
    
    #@app.route("/atualiza_financeiro")
    #def atualiza_financeiro():        
        #return render_template("atualiza_financeiro.html")
    
    #@app.route("/cad_financeiro")
    #def cad_financeiro():        
        #return render_template("cad_financeiro.html")
    
    
    