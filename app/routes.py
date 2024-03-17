from app.models import usuario
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
        return render_template("inicio.html")
    
    @app.route("/nota_fiscal")
    def nota_fiscal():        
        return render_template("nota_fiscal.html")
    
    @app.route("/financeiro")
    def financeiro():        
        return render_template("financeiro.html")
    
    @app.route("/produto")
    def produto():        
        return render_template("produto.html")
    
    @app.route("/cad_prod")
    def cad_prod():        
        return render_template("cad_prod.html")
    
    @app.route("/usuario")
    def usuario():        
        return render_template("usuario.html")
    
    @app.route("/cad_user")
    def cad_user():        
        return render_template("cad_user.html")
    
    @app.route("/cad_financeiro")
    def cad_financeiro():        
        return render_template("cad_financeiro.html")
    
    @app.route("/atualiza_user")
    def atualiza_user():        
        return render_template("atualiza_user.html")
    
    @app.route("/atualiza_financeiro")
    def atualiza_financeiro():        
        return render_template("atualiza_financeiro.html")
    
    
    