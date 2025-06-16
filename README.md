# 📚 Gestão Escolar API

![Gestão Escolar API](https://img.shields.io/badge/Version-1.0.0-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Introdução

Este repositório contém uma API RESTful desenvolvida em Python com Flask, voltada para a gestão escolar. A plataforma permite que professores e alunos sejam cadastrados, organiza matérias e atividades, além de facilitar o lançamento de notas. Este projeto busca simplificar a gestão educacional e melhorar a experiência de usuários em instituições de ensino.

Você pode acessar as versões mais recentes da API na seção de [Releases](https://github.com/Fabrix-IA/gestao-escolar_api/releases).

## 📦 Funcionalidades

- **Cadastro de Usuários**: Permite o registro de alunos e professores.
- **Gerenciamento de Matérias**: Organiza e categoriza as matérias oferecidas.
- **Atividades**: Facilita a criação e o acompanhamento de atividades escolares.
- **Lançamento de Notas**: Proporciona um sistema para registrar e visualizar notas dos alunos.
- **Autenticação JWT**: Garante segurança e proteção dos dados através de autenticação baseada em tokens.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para a construção da API.
- **Flask-SQLAlchemy**: ORM para interagir com o banco de dados SQLite.
- **Flask-JWT-Extended**: Para autenticação e gerenciamento de tokens JWT.
- **SQLite**: Banco de dados leve e fácil de usar.

## 📋 Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
gestao-escolar_api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
│
├── config.py
├── requirements.txt
└── run.py
```

### Descrição dos Arquivos

- **app/**: Contém o código principal da aplicação.
  - **__init__.py**: Inicializa a aplicação Flask e configura as extensões.
  - **models.py**: Define os modelos de dados para o banco de dados.
  - **routes.py**: Contém as rotas da API.
  - **utils.py**: Funções utilitárias que suportam a aplicação.
  
- **config.py**: Configurações da aplicação, incluindo variáveis de ambiente.

- **requirements.txt**: Lista de dependências necessárias para o projeto.

- **run.py**: Script para iniciar a aplicação.

## ⚙️ Como Instalar

Para instalar e executar a API, siga os passos abaixo:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Fabrix-IA/gestao-escolar_api.git
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd gestao-escolar_api
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**:
   ```bash
   python run.py
   ```

A API estará disponível em `http://localhost:5000`.

## 📜 Endpoints

A API possui os seguintes endpoints:

### Usuários

- **POST /usuarios**: Cadastra um novo usuário (aluno ou professor).
- **GET /usuarios**: Lista todos os usuários cadastrados.
- **GET /usuarios/<id>**: Obtém os detalhes de um usuário específico.

### Matérias

- **POST /materias**: Adiciona uma nova matéria.
- **GET /materias**: Lista todas as matérias.
- **GET /materias/<id>**: Obtém detalhes de uma matéria específica.

### Atividades

- **POST /atividades**: Cria uma nova atividade.
- **GET /atividades**: Lista todas as atividades.
- **GET /atividades/<id>**: Obtém detalhes de uma atividade específica.

### Notas

- **POST /notas**: Lança uma nova nota para um aluno.
- **GET /notas**: Lista todas as notas.
- **GET /notas/<id>**: Obtém detalhes de uma nota específica.

## 🔑 Autenticação

A API utiliza autenticação JWT. Para obter um token, faça uma requisição `POST` para o endpoint `/login` com as credenciais do usuário. O token retornado deve ser incluído no cabeçalho de autorização em todas as requisições subsequentes.

### Exemplo de Login

```bash
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "usuario", "password": "senha"}'
```

O token de autenticação será retornado em formato JSON.

## 🧪 Testes

Os testes são fundamentais para garantir que a API funcione corretamente. Para executar os testes, você pode usar o framework `pytest`. Certifique-se de ter o `pytest` instalado e execute o seguinte comando:

```bash
pytest
```

Os testes estão localizados no diretório `tests/`.

## 📄 Documentação

A documentação da API pode ser encontrada na seção de [Releases](https://github.com/Fabrix-IA/gestao-escolar_api/releases). Recomenda-se consultar a documentação para detalhes sobre como usar cada endpoint e suas respectivas funcionalidades.

## 📈 Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

1. **Fork o repositório**.
2. **Crie uma nova branch**:
   ```bash
   git checkout -b minha-nova-feature
   ```
3. **Faça suas alterações** e commit:
   ```bash
   git commit -m 'Adicionei uma nova feature'
   ```
4. **Envie para o repositório remoto**:
   ```bash
   git push origin minha-nova-feature
   ```
5. **Abra um Pull Request**.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🌟 Agradecimentos

Agradecemos a todos os colaboradores e à comunidade de desenvolvedores que contribuíram para este projeto. Sua ajuda é fundamental para o sucesso da gestão escolar.

## 📣 Fale Conosco

Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue no repositório ou entrar em contato diretamente.

Para mais informações, visite a seção de [Releases](https://github.com/Fabrix-IA/gestao-escolar_api/releases) para acompanhar as atualizações e novas funcionalidades.