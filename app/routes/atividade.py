from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Atividade, Materia, Usuario

atividade_bp = Blueprint('atividade', __name__)


@atividade_bp.route('/', methods=['POST'])
@jwt_required()
def criar_atividade():
    # Obtém o ID do usuário do token
    current_user_id = get_jwt_identity()
    # Busca o usuário no banco
    current_user = Usuario.query.get(int(current_user_id))

    if not current_user or current_user.tipo != 'professor':
        return jsonify({'erro': 'Acesso negado'}), 403

    data = request.json
    if not data or 'titulo' not in data or 'aluno_id' not in data or 'materia_id' not in data:
        return jsonify({'erro': 'Dados incompletos'}), 400

    materia = Materia.query.get(data['materia_id'])
    if not materia or materia.professor_id != current_user.id:
        return jsonify({'erro': 'Matéria inválida'}), 400

    aluno = Usuario.query.get(data['aluno_id'])
    if not aluno or aluno.tipo != 'aluno' or aluno not in materia.alunos:
        return jsonify({'erro': 'Aluno inválido'}), 400

    atividade = Atividade(
        titulo=data['titulo'],
        descricao=data.get('descricao'),
        data_entrega=data.get('data_entrega'),
        nota=data.get('nota'),
        aluno_id=data['aluno_id'],
        materia_id=data['materia_id']
    )
    db.session.add(atividade)
    db.session.commit()

    return jsonify({
        'id': atividade.id,
        'titulo': atividade.titulo,
        'aluno_id': atividade.aluno_id,
        'materia_id': atividade.materia_id
    }), 201


@atividade_bp.route('/', methods=['GET'])
@jwt_required()
def listar_atividades():
    # Obtém o ID do usuário do token
    current_user_id = get_jwt_identity()
    # Busca o usuário no banco
    usuario = Usuario.query.get(int(current_user_id))

    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    if usuario.tipo == 'aluno':
        atividades = usuario.atividades
    else:
        # Professor: atividades de suas matérias
        atividades = Atividade.query.join(Materia).filter(
            Materia.professor_id == usuario.id
        ).all()

    return jsonify([{
        'id': a.id,
        'titulo': a.titulo,
        'materia': a.materia.nome,
        'aluno': a.aluno.nome,
        'nota': a.nota
    } for a in atividades]), 200


@atividade_bp.route('/<int:id>/nota', methods=['PUT'])
@jwt_required()
def atualizar_nota(id):
    # Obtém o ID do usuário do token
    current_user_id = get_jwt_identity()
    # Busca o usuário no banco
    current_user = Usuario.query.get(int(current_user_id))

    if not current_user or current_user.tipo != 'professor':
        return jsonify({'erro': 'Acesso negado'}), 403

    data = request.json
    if not data or 'nota' not in data:
        return jsonify({'erro': 'Nota é obrigatória'}), 400

    atividade = Atividade.query.get(id)
    if not atividade:
        return jsonify({'erro': 'Atividade não encontrada'}), 404

    if atividade.materia.professor_id != current_user.id:
        return jsonify({'erro': 'Você não pode atualizar esta atividade'}), 403

    atividade.nota = data['nota']
    db.session.commit()

    return jsonify({'mensagem': 'Nota atualizada com sucesso'}), 200