ENV = 'development'
DEBUG = True

SECRET_KEY = "asdfasdfjasdfjasd;lf"
# 数据库配置信息
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "yourusername"
PASSWORD ='yourpwd'
DATABASE = "wenda"
DB_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI=DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "example@163.com"
MAIL_PASSWORD = "yourpwd"
MAIL_DEFAULT_SENDER = "example@163.com"

