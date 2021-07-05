from WeconBiochem import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))



class Usuario(database.Model, UserMixin):
    # Cada atributo de classe corresponde a uma coluna de tabela de database, uma nova informação:
    # Criarei a relação de um (Usuário) para muitos (Post), na variável posts:
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    # o parâmetro abaixo backref corresponde ao nome de quem cria o post, já o lazy passa todas as informações do
    # autor, ao invés de termos que buscar cada informação individualmente:
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)


# Quando armazenamos um texto muito grande, não utilizamos o parâmetro String, sim o text, por poder conter mais
# caracteres, conforme exemplo abaixo, no corpo da classe Post():
# Para o atributo data_criacao, utilizamos o datetime.utcnow sem os parênteses da função, pois somente dessa forma o
#   cálculo é realizado e transformado em objeto, caso contrário, seria exibido o horário em que o código foi criado.
class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    # No parâmetro do chave estrangeira (ForeignKey()), devemos passar sempre o nome da classe(sempre em minúsculo)
    # + o atributo no qual queremos utilizar como FK, ex: database.ForeignKey('usuario.id'):
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
