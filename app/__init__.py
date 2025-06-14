from flask import Flask, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    print(f"Token recebido: {jwt_payload}")
    return False  # Não revogar tokens por enquanto

@jwt.unauthorized_loader
def missing_token_callback(error):
    print(f"Erro de autorização: {error}")
    return jsonify({"msg": "Missing Authorization Header"}), 401

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    app.config['JWT_SECRET_KEY'] = app.config.get('JWT_SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.materia import materia_bp
    from app.routes.atividade import atividade_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(materia_bp, url_prefix='/api/materias')
    app.register_blueprint(atividade_bp, url_prefix='/api/atividades')
    
    return app