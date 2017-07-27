#主要视图，登陆注册主界面

from flask import redirect,render_template,url_for,flash,request,g
from . import app,login_manager
from .model import showdata,CountRightStepDay,User,findUser,AddUser,getUser
from .forms import NameForm,SignForm
from flask_login import login_user,login_required,logout_user,current_user

@app.route('/', methods=['GET','POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        user = findUser(name)
        login_user(user)

        next = request.args.get('next')

        # user = session.query(User).filter_by(username=form.name.data).first()
        if user is not None and user.password == form.password.data:
            return redirect(url_for('main'))
        # else:
        #     flash('Please register first')
    return render_template('./log/login.html',form = form)


@app.route('/signup', methods=['GET','POST'])
def signup():
    form= SignForm()
    user = User(email=form.email.data,username = form.name.data, password = form.password.data)
    if form.validate_on_submit():
        AddUser(user)
        return redirect(url_for('login'))
    return render_template('./log/signup.html',form=form)


@app.route('/main')
@login_required
def main():
    return render_template('main.html')

@login_manager.user_loader
def load_user(userid):
    return getUser(userid)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))




