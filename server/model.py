#对数据库的操作

from . import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, TIMESTAMP,Text,DateTime
from sqlalchemy import ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine,func
STEPMINCOUNT = 12000  #达到合格需要走的最少步数


db.create_all()
engine=create_engine('mysql+pymysql://root:password@localhost:3306/runeye?charset=utf8',encoding='utf-8')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    role_id = Column(Integer,ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


    def is_administrator(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True


class Role(Base):
    __tablename__='roles'

    id = Column(Integer, primary_key=True,autoincrement=True)
    rolename = Column(String(64), nullable=False, index=True)
    users=relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r>' % self.rolename

class Data(Base):
    __tablename__='datas'

    id = Column(Integer,primary_key=True)
    time = Column(Integer)
    runtime = Column(Integer)
    stepnum = Column(Integer)
    pushup = Column(Integer)
    weight = Column(Integer)

class Post(Base):
    __tablename__='posts'

    id = Column(Integer,primary_key=True)
    post = Column(Text)
    # mood = Column(String(24))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


#返回所有数据
# def showdata():
#     ret = session.query(Data).all()
#     session.commit()
#     return ret

#返回特定条目的数据
def showdata(num = 30):
    ret = session.query(Data).filter(Data.id <= num)
    session.commit()
    return ret


#返回某一条数据
def getnewdata(id):
    ret = session.query(Data).filter(Data.id==id).all()
    session.commit()
    return ret


#求出步数合格的天数的百分比
def CountRightStepDay():
    ret =  session.query(func.count('*')).filter(Data.stepnum > STEPMINCOUNT).scalar()
    total = session.query(func.count(Data.id)).scalar()
    percentage = (int)((ret/total) * 100)
    session.commit()
    return  percentage


#寻找数据库中是否有这个用户
def findUser(name):
    ret = session.query(User).filter_by(username = name).first()
    session.commit()
    return ret

#获得特定id的用户
def getUser(id):
    ret = session.query(User).get(id)
    session.commit()
    return ret


#添加用户
def AddUser(user):
    session.add(user)
    session.commit()

#添加用户的随笔，心情与意见
def AddPost(text):
    post = Post(post=text)
    session.add(post)
    session.commit()

#展示随笔
def ShowPost():
    ret = session.query(Post).all()
    session.commit()
    return ret