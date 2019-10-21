import pymysql

# 创建数据库连接，主机，端口，用户，密码，库名
db = pymysql.connect(
    host="localhost",# 主机名
    port=3306,# 端口名
    user="root",# 用户名
    password="123456",# 数据库密码
    db="werewolf",# 数据库名字
)
# 拿到游标
cursor = db.cursor()
# 要执行的sql语句
sql = """
    create table player(id int,addr char(32),name char(16),number int,alive_status int,info char(16));
"""
# 执行sql语句
cursor.execute(sql)
# 提交操作
db.commit()
# 关闭连接
db.close()