from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
#from flask_bootstrap import Bootstrap

app = Flask(__name__,template_folder="views",static_folder="../public")

db = SQLAlchemy()
login_manager = LoginManager()
#bootstrap = Bootstrap()

def create_app():    
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://username:password@localhost/db_name'
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/palmaflex'    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/rh_online'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = 'secret'
    app.config['JWT_SECRET_KEY'] = 'secret'
    app.config['JWT_BLACKLIST_ENABLE'] = True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False #Token sem expiração
    
    
    db.init_app(app)
    login_manager.init_app(app)
    #bootstrap.init_app(app)

    from app import routes
    routes.init_app(app)

    return app




