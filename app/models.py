from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# Tabela de associação
usuario_materia = db.Table('usuario_materia',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('materia_id', db.Integer, db.ForeignKey('materia.id'), primary_key=True)
)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'aluno' ou 'professor'
    
    materias = db.relationship('Materia', secondary=usuario_materia, back_populates='alunos')
    atividades = db.relationship('Atividade', back_populates='aluno')
    materias_lecionadas = db.relationship('Materia', back_populates='professor')

    @property
    def senha(self):
        raise AttributeError('senha não é um atributo legível')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

class Materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
    professor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    professor = db.relationship('Usuario', back_populates='materias_lecionadas')
    alunos = db.relationship('Usuario', secondary=usuario_materia, back_populates='materias')
    atividades = db.relationship('Atividade', back_populates='materia')

class Atividade(db.Model):
    __tablename__ = 'atividade'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_entrega = db.Column(db.DateTime)
    nota = db.Column(db.Float)
    
    aluno_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)
    
    aluno = db.relationship('Usuario', back_populates='atividades')
    materia = db.relationship('Materia', back_populates='atividades')