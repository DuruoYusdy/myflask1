#电子邮件支持
from flask import render_template
from flask_mail import Mail,Message
from threading import Thread
from server import mail,app


def send_async_email(app, msg):
        with app.app_context():
            mail.send(msg)


def send():
        msg = Message('Hello', sender="444372922@qq.com", recipients=["444372922@qq.com"])
        msg.body = render_template('./mail/email.txt')
        msg.html = render_template('./mail/email.html')
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()
        return thr


# def sendmail():
#     msg = Message('Hello',sender="444372922@qq.com",recipients=["444372922@qq.com"])
#     msg.body = "hello"
#     msg.html = "<b>testing</b>"
#     mail.send(msg)