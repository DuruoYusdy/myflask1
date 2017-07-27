#
# import os
#配置文件
class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/new?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'hard to guess myname'

    MAIL_USERNAME = '444372922@qq.com'
    MAIL_PASSWORD = 'your password'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True

