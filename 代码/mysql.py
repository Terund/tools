import pymysql


class OperateMysql:
    def __init__(self, host=None, port=None, password=None, db=None, user=None):
        """
        链接数据库
        :param host: 主机ip
        :param port: 端口号
        :param password: 数据库密码
        :param db: 数据库名
        :param user: 数据库用户
        """
        self.db = pymysql.connect(
            host=host,
            port=port,
            password=password,
            db=db,
            user=user
        )

    def operate(self, sql):
        """
        获取数据
        :param sql: 要执行的sql语句
        :return: 返回查询得到的结果
        """
        cursor = self.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db.commit()
        return result

    def __del__(self):
        """
        关闭数据库链接
        :return:无返回值
        """
        self.db.close()
