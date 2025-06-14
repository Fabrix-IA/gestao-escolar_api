from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app import db
from app.models import Usuario
from flask_jwt_extended import create_access_token
import logging

# Configurar sistema de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registrar', methods=['POST'])
def registrar():
    logger.info("Recebida solicitação de registro")
    data = request.json
    logger.debug(f"Dados recebidos: {data}")
    
    # Campos obrigatórios
    required_fields = ['email', 'senha', 'nome', 'tipo']
    if not data or any(field not in data for field in required_fields):
        logger.warning("Dados incompletos no registro")
        return jsonify({'erro': 'Dados incompletos'}), 400
    
    # Verificar se email já existe
    existing_user = Usuario.query.filter_by(email=data['email']).first()
    if existing_user:
        logger.warning(f"Email já cadastrado: {data['email']}")
        return jsonify({'erro': 'Email já cadastrado'}), 400
    
    # Criar novo usuário
    novo_usuario = Usuario(
        nome=data['nome'],
        email=data['email'],
        tipo=data['tipo']
    )
    novo_usuario.senha = data['senha']
    
    try:
        db.session.add(novo_usuario)
        db.session.commit()
        logger.info(f"Usuário criado com sucesso: ID {novo_usuario.id}, Email {novo_usuario.email}")
        return jsonify({
            'mensagem': 'Usuário criado com sucesso',
            'id': novo_usuario.id,
            'email': novo_usuario.email,
            'tipo': novo_usuario.tipo
        }), 201
    except Exception as e:
        logger.error(f"Erro ao criar usuário: {str(e)}")
        db.session.rollback()
        return jsonify({'erro': 'Erro interno no servidor'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    logger.info("Recebida solicitação de login")
    data = request.json
    logger.debug(f"Dados recebidos: {data}")
    
    if not data or 'email' not in data or 'senha' not in data:
        logger.warning("Credenciais incompletas no login")
        return jsonify({'erro': 'Credenciais necessárias'}), 400
    
    usuario = Usuario.query.filter_by(email=data['email']).first()
    
    if not usuario:
        logger.warning(f"Usuário não encontrado: {data['email']}")
        return jsonify({'erro': 'Email ou senha inválidos'}), 401
    
    if not usuario.verificar_senha(data['senha']):
        logger.warning(f"Senha incorreta para o usuário: {data['email']}")
        return jsonify({'erro': 'Email ou senha inválidos'}), 401
    
    try:
        token = create_access_token(identity=str(usuario.id))
        logger.info(f"Login bem-sucedido para: {usuario.email}")
        logger.debug(f"Token gerado: {token}")
        return jsonify({
            'access_token': token,
            'tipo': usuario.tipo,
            'id': usuario.id,
            'email': usuario.email
        }), 200
    except Exception as e:
        logger.error(f"Erro ao gerar token: {str(e)}")
        return jsonify({'erro': 'Erro interno no servidor'}), 500