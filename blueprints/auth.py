from flask import Blueprint,render_template,request,jsonify,redirect,url_for,session
from exts import mail,db
from flask_mail import Message
import string
import random
from models import EmailCaptchaModel,UserModel
from blueprints.forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

bp=Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        form=LoginForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            user=UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在!")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password,password):
                # cookie：
                # cookie中不适合存储太多的数据，只适合存储少量的数据
                # cookie一般用来存放登录授权的东西
                # flask中的session，是经过加密后存储在cookie中的
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误!")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        form=RegisterForm(request.form)
        if form.validate():
            email=form.email.data
            username=form.username.data
            password=form.password.data
            user=UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/captcha")
def get_email_captcha():
    email=request.args.get("email")
    source=string.digits*10
    captcha=random.sample(source,6)
    captcha=''.join(captcha)
    message = Message(subject="问答平台验证码", recipients=[email], body=f"您的验证码是:{captcha}")
    mail.send(message)
    email_captcha=EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    return jsonify({"code":200,"message":"","data":None})

# @bp.route("/mail/test")
# def mail_test():
#     message=Message(subject="邮件测试",recipients=["1939311091@qq.com"],body="这是一条测试邮件！")
#     mail.send(message)
#     return "邮件发送成功！"
