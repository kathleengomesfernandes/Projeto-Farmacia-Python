from app.models import usuario
from app.models import clientes
from app.models import pedidos
from app.models import produtos
from app.models import notas
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def init_app(app):
        
    @app.route("/",methods=["GET", "POST"])
    def index():        
        form = LoginForm()
        
        if form.validate_on_submit():
        #if request.method == "POST":
            user = usuario.query.filter_by(email=form.email.data).first()
            
            if not user:
                flash("Email do usuario incorreto, por favor verifique!")
                return redirect(url_for("index"))
                #return render_template("user_inv.html")
            
            elif not check_password_hash(user.senha, form.senha.data):
                flash("Senha de usuario incorreto, por favor verifique")
                return redirect(url_for("index"))
                #return render_template("user_inv.html")
            
            login_user(user, remember=form.remember.data, duration= timedelta(days=7))
            #login_user(user)
            return redirect(url_for("inicio"))
        
        return render_template("index.html", form=form)  
    
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("index"))  
    
    @app.route("/inicio")
    @login_required
    def inicio():        
        return render_template("/inicio.html", usuarios=db.session.execute(db.select(usuario).order_by(usuario.id)).scalars())
    
    @app.route("/excluir/<int:id>")
    def excluir_user(id):
        delete=usuario.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("inicio"))
    
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
    
    @app.route("/cliente")
    def cliente():        
        return render_template("/cliente.html", client=db.session.execute(db.select(clientes).order_by(clientes.id)).scalars())
    
    @app.route("/excluir_cli/<int:id>")
    def excluir_cli(id):
        delete=clientes.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("cliente"))
        
    @app.route("/atualiza_cliente/<int:id>", methods=["GET", "POST"])
    def atualiza_cliente(id): 
        cli=clientes.query.filter_by(id=id).first() 
        if request.method == "POST":
            nome_clientes = request.form["nome"]
            email_clientes = request.form["email"]
            empresa_clientes = request.form["empresa"]
            
            flash("Dados do cliente alterado com sucesso!")
            cli.query.filter_by(id=id).update({"nome":nome_clientes, "email":email_clientes, "empresa":empresa_clientes})
            db.session.commit()
            return redirect(url_for("cliente"))
        return render_template("atualiza_cliente.html", clients=cli)
    
    @app.route("/cad_cliente", methods=["GET", "POST"])
    def cad_cliente():        
        if request.method =="POST":
            cli = clientes()
            cli.nome = request.form["nome"]
            cli.email = request.form["email"]
            cli.empresa = request.form["empresa"]
            db.session.add(cli)
            db.session.commit()

            flash("Cliente criado com sucesso!")
            return redirect(url_for("cad_cliente"))
        return render_template("cad_cliente.html")
    
    @app.route("/pedido")
    def pedido():        
        return render_template("pedido.html", ped=db.session.execute(db.select(pedidos).order_by(pedidos.id)).scalars())
    
    @app.route("/excluir_pedi/<int:id>")
    def excluir_pedi(id):
        delete=pedidos.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("pedido"))
        
    @app.route("/cad_pedido", methods=["GET", "POST"])
    def cad_pedido():        
        if request.method =="POST":
            pedi = pedido()
            pedi.num_pedido = request.form["num_pedido"]
            pedi.descricao = request.form["descricao"]
            pedi.insumos = request.form["insumos"]
            pedi.quantidades = request.form["quantidade"]
            pedi.valor = request.form["valor"]
            db.session.add(pedi)
            db.session.commit()

            flash("Pedido criado com sucesso!")
            return redirect(url_for("cad_pedido"))
        return render_template("cad_pedido.html")
    
    @app.route("/atualiza_pedido/<int:id>", methods=["GET", "POST"])
    def atualiza_pedido(id): 
        pedi=pedidos.query.filter_by(id=id).first() 
        if request.method == "POST":
            num_pedido_pedidos = request.form["num_pedido"]
            descricao_pedidos = request.form["descricao"]
            insumos_pedidos = request.form["insumos"]
            quantidade_pedidos = request.form["quantidade"]
            valor_pedidos = request.form["valor"]
        
            flash("Dados do pedido alterado com sucesso!")
            pedi.query.filter_by(id=id).update({"num_pedido":num_pedido_pedidos, "descricao":descricao_pedidos, "insumos":insumos_pedidos, "quantidade":quantidade_pedidos, "valor":valor_pedidos})
            db.session.commit()
            return redirect(url_for("pedido"))
        return render_template("atualiza_pedido.html", peds=pedi)
    
    @app.route("/produto")
    def produto():        
        return render_template("produto.html", prod=db.session.execute(db.select(produtos).order_by(produtos.id)).scalars())

    @app.route("/excluir_pdts/<int:id>")
    def excluir_pdts(id):
        delete=produtos.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("produto"))
    
    @app.route("/cad_prod", methods=["GET", "POST"])
    def cad_prod():        
        if request.method =="POST":
            prod = produto()
            prod.nome = request.form["nome"] 
            prod.qr_code_produto = request.form["qr_code_produto"]
            prod.observacao = request.form["observacao"]
            prod.conservacao = request.form["conservacao"]
            prod.data_validade = request.form["data_validade"]
            db.session.add(prod)
            db.session.commit()

            flash("Produto criado com sucesso!")
            return redirect(url_for("cad_prod"))
        return render_template("cad_prod.html")
    
    @app.route("/atualiza_produto/<int:id>", methods=["GET", "POST"])
    def atualiza_produto(id): 
        pdts=produtos.query.filter_by(id=id).first() 
        if request.method == "POST":
            nome_pdts = request.form["nome"]
            qr_code_produto_pdts = request.form["qr_code_produto"]
            observacao_pdts = request.form["observacao"]
            conservacao_pdts = request.form["conservacao"]
            data_validade_pdts = request.form["data_validade"]
        
            flash("Dados do produto alterado com sucesso!")
            pdts.query.filter_by(id=id).update({"nome":nome_pdts, "qr_code_produto":qr_code_produto_pdts, "observacao":observacao_pdts, "conservacao":conservacao_pdts, "data_validade":data_validade_pdts})
            db.session.commit()
            return redirect(url_for("produto"))
        return render_template("atualiza_produto.html", prods=pdts)
    
    @app.route("/nota_fiscal")
    def nota_fiscal():        
        return render_template("/nota_fiscal.html", nota=db.session.execute(db.select(notas).order_by(notas.id)).scalars())
    
    @app.route("/excluir_notaf/<int:id>")
    def excluir_notaf(id):
        delete=notas.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("nota_fiscal"))
    
    @app.route("/cad_nota", methods=["GET", "POST"])
    def cad_nota():        
        if request.method =="POST":
            notaf = notas()
            notaf.num_nf = request.form["num_nf"] 
            notaf.valor = request.form["valor"]
            notaf.data_emissao = request.form["data_emissao"]
            notaf.descricao = request.form["descricao"]   
            db.session.add(notaf)
            db.session.commit()

            flash("Nota fiscal criada com sucesso!")
            return redirect(url_for("cad_nota"))
        return render_template("cad_nota.html")
    
    @app.route("/atualiza_nota/<int:id>", methods=["GET", "POST"])
    def atualiza_nota(id): 
        notaf=notas.query.filter_by(id=id).first() 
        if request.method == "POST":
            num_nf_notas = request.form["num_nf"]
            valor_notas = request.form["valor"]
            data_emissao_notas = request.form["data_emissao"]
            descricao_notas = request.form["descricao"]
            
            flash("Dados da nota fiscal alterado com sucesso!")
            notaf.query.filter_by(id=id).update({"num_nf":num_nf_notas, "valor":valor_notas, "data_emissao":data_emissao_notas, "descricao":descricao_notas})
            db.session.commit()
            return redirect(url_for("nota_fiscal"))
        return render_template("atualiza_nota.html", ntfiscal=notaf)
    
    
    