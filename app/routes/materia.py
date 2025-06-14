from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Materia, Usuario

materia_bp = Blueprint('materia', __name__)


@materia_bp.route('/', methods=['POST'])
@jwt_required()
def criar_materia():
    # Obtém o ID do usuário do token
    current_user_id = get_jwt_identity()
    # Busca o usuário no banco
    current_user = Usuario.query.get(int(current_user_id))

    if not current_user or current_user.tipo != 'professor':
        return jsonify({'erro': 'Acesso negado'}), 403

    data = request.json
    if not data or 'nome' not in data:
        return jsonify({'erro': 'Nome da matéria é obrigatório'}), 400

    materia = Materia(
        nome=data['nome'],
        professor_id=current_user.id
    )
    db.session.add(materia)
    db.session.commit()

    return jsonify({
        'id': materia.id,
        'nome': materia.nome,
        'professor_id': materia.professor_id
    }), 201


@materia_bp.route('/', methods=['GET'])
@jwt_required()
def listar_materias():
    # Obtém o ID do usuário do token
    current_user_id = get_jwt_identity()
    # Busca o usuário no banco
    usuario = Usuario.query.get(int(current_user_id))

    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    if usuario.tipo == 'professor':
        materias = Materia.query.filter_by(professor_id=usuario.id).all()
    else:
        materias = usuario.materias

    return jsonify([{
        'id': m.id,
        'nome': m.nome,
        'professor': m.professor.nome if m.professor else None
    } for m in materias]), 200


@materia_bp.route('/<int:id>/matricular/<int:aluno_id>', methods=['POST'])
@jwt_required()
def matricular_aluno(id, aluno_id):
    # Obtém o ID do usuário do token
    current_user_id = get_jwt_identity()
    # Busca o usuário no banco
    current_user = Usuario.query.get(int(current_user_id))

    if not current_user or current_user.tipo != 'professor':
        return jsonify({'erro': 'Acesso negado'}), 403

    materia = Materia.query.get(id)
    if not materia:
        return jsonify({'erro': 'Matéria não encontrada'}), 404

    if materia.professor_id != current_user.id:
        return jsonify({'erro': 'Você não é o professor desta matéria'}), 403

    aluno = Usuario.query.get(aluno_id)
    if not aluno or aluno.tipo != 'aluno':
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    if aluno in materia.alunos:
        return jsonify({'erro': 'Aluno já matriculado'}), 400

    materia.alunos.append(aluno)
    db.session.commit()

    return jsonify({'mensagem': 'Aluno matriculado com sucesso'}), 200