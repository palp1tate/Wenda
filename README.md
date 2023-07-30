# Wenda
基于flask实现的web问答平台

视频来源：<https://www.bilibili.com/video/BV17r4y1y7jJ/?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=84fc27804252448ba51ef3b6abfd5d36>

下载：
```
git clone https://github.com/uestc-wxy/Wenda.git
```

打开`config.py`

配置以下内容：

```python
SECRET_KEY = "asdfasdfjasdfjasd;lf"   #用于session加密，可随便配置该字符串

# 数据库配置信息
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "yourusername"
PASSWORD ='yourpwd'
DATABASE = "wenda"
DB_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI=DB_URI


#邮箱配置信息
MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "example@163.com"
MAIL_PASSWORD = "yourpwd"
MAIL_DEFAULT_SENDER = "example@163.com"
```

在本地创建数据库`wenda`，然后在项目根目录运行下列命令：
```bash
flask db init
flask db migrate
flask db upgrade
```

最后运行该flask项目：
```bash
python app.py
```

最后访问网址：<http://127.0.0.1:5000> 即可

![image](https://github.com/uestc-wxy/Wenda/assets/120303802/5ea0a511-e94a-446b-b028-6446e8f94690)

![image](https://github.com/uestc-wxy/Wenda/assets/120303802/ab73bf7d-f951-4fa3-a6b3-9d7426cc5b02)

![image](https://github.com/uestc-wxy/Wenda/assets/120303802/18054f91-0bfe-4e55-90cf-e1b1fd774323)

![image](https://github.com/uestc-wxy/Wenda/assets/120303802/3d53cd68-7616-43a8-adea-c3ea14345c58)

![image](https://github.com/uestc-wxy/Wenda/assets/120303802/cb5dcf43-f43d-464f-9db6-a67711931aa0)








