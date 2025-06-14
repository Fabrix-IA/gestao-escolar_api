# 📚 API de Gestão Escolar

API RESTful desenvolvida com **Flask** e **SQLite** para gerenciamento de uma plataforma escolar. O sistema permite o cadastro de usuários (professores e alunos), gerenciamento de matérias, atividades e lançamento de notas. A autenticação é feita por meio de tokens **JWT**, garantindo segurança nas operações protegidas.

SQLite é utilizado como banco de dados por sua leveza, praticidade e integração facilitada com o ambiente Flask.

---

## 🔢 Principais Rotas da API

### Autenticação

* `POST /api/auth/registrar`: Registrar usuário
* `POST /api/auth/login`: Login

### Matérias

* `POST /api/materias`: Criar matéria (apenas professores)
* `GET /api/materias`: Listar matérias
* `POST /api/materias/{id}/matricular/{aluno_id}`: Matricular aluno (apenas professores)

### Atividades

* `POST /api/atividades`: Criar atividade (apenas professores)
* `GET /api/atividades`: Listar atividades
* `PUT /api/atividades/{id}/nota`: Atualizar nota da atividade (apenas professores)

---

## ⚙️ Como Executar o Projeto Localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. \*\*Configure o arquivo \*\***`.env`** com as variáveis:

```env
SECRET_KEY=sua_chave_secreta
JWT_SECRET_KEY=sua_chave_jwt
DATABASE_URL=sqlite:///app.db
```

5. **Inicialize o banco de dados:**

```bash
flask db init
flask db migrate
flask db upgrade
```

6. **Inicie o servidor:**

```bash
flask run
```

---

## 📊 Observações

* Apenas professores podem cadastrar matérias e atividades.
* Alunos podem visualizar matérias e atividades nas quais estão matriculados.
* Para acessar rotas protegidas, envie o token JWT no cabeçalho:

  ```http
  Authorization: Bearer <seu_token_jwt>
  ```

---

## 📁 Estrutura Sugerida do Projeto

```
/project-root
├── app.py
├── models/
├── routes/
├── config.py
├── requirements.txt
└── .env
```

---

## 📅 Licença

Este projeto está licenciado sob os termos da licença **MIT**. Sinta-se livre para utilizar, modificar e contribuir.
