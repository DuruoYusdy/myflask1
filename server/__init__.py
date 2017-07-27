import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)    #也可以在应用程序配置的时候设置你的实例，通过使用 init_app 方法
login_manager.login_view = 'login'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)     #邮件是通过一个 Mail 实例进行管理
oid = OpenID(app,os.path.join('./tmp'))

import server.views
import server.model
import server.viewchart
import server.forms
import server.viewerror
import server.sender.mail