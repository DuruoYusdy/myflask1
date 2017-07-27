#可视化实现，包括展示与处理

from flask import render_template, jsonify, request
from flask_login import login_required
from . import app
from .model import showdata, getnewdata, CountRightStepDay,AddPost,ShowPost
from .sender.mail import send

#展示数据的界面视图
@app.route('/onlydata')
@login_required
def onlydata():
    list = []
    for i in showdata():
        list.append(
            {"time": i.time, "runtime": i.runtime, "stepnum": i.stepnum, "pushup": i.pushup, "weight": i.weight})
    return render_template('onlydata.html',lists=list)


@app.route('/forstep')
@login_required
def forstep():
    percentage = CountRightStepDay()
    if percentage < 50:
        send()        #如何合格的比率小于1/2，则发送邮件,默认为发送电子邮件
    return render_template('forstep.html',percentage = percentage)


@app.route('/forweight')
@login_required
def forweight():
    return render_template('forweight.html')


@app.route('/forelse',methods=["GET","POST"])
@login_required
def forelse():
    if request.method == "GET":
        pass
    if request.method == "POST":
        if request.form['text'] is not None:
            AddPost(request.form['text'])
    else:
        pass
    list = []
    for i in ShowPost():
        list.append({"post": i.post})
    return render_template('forelse.html',lists=list)


#处理数据的可视化视图
@app.route('/dostep',methods=["GET","POST"])
def dostep():
    if request.method == "GET":
        res = showdata(6)
    elif request.method == "POST":
        res = getnewdata(int(request.form['id'])+1)
    else:
        res = showdata()
    return jsonify(id = [x.id for x in res],time = [x.time for x in res], \
                   runtime = [x.runtime for x in res],stepnum = [x.stepnum for x in res],pushup = [x.pushup for x in res],weight = [x.weight for x in res])

