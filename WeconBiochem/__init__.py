# Render_Template tem a função de renderizar a página em html, Url_For padroniza os links pela sua função,
# Request tem a função de verificar se existe o conteúdo que queremos dentro de um formulário,
# Flash('texto') tem a função de mostrar uma mensagem de aviso,
# Redirect tem a função de redirecionar o usuário a outra página, após alguma ação:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd5864639c3114d121f9b0f1be3a43dca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wecom.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça o login para continuar.'
login_manager.login_message_category = 'alert-info'


# Importando o arquivo routes da pasta WeconBiochem, para que ele seja executado e que os links do arquivo
# routes.py sejam executados. Este deve ser importado após a criação da variável app, pois depende dela para
# que funcione corretamente.:
from WeconBiochem import routes

