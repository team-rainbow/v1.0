"""
用户数据库
"""

import pymysql
class Database:
    def __init__(self, host='localhost',
                 port=3306,
                 user='root',
                 paswd='123456',
                 database='project',
                 charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.paswd = paswd
        self.database = database
        self.charset = charset
        self.connect_db()  # 链接数据库

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.paswd,
                                  database=self.database,
                                  charset=self.charset)

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 　关闭数据库
    def close(self):
        self.cur.close()
        self.db.close()

    # 　处理注册
    def chachong(self, user):
        sql = "select * from login where user ='%s'" % user
        self.cur.execute(sql)
        r = self.cur.fetchone()  # 如果查询到结果
        if r:
            return True

    def register(self, user, passwd, phone, email):
        sql = (r'insert into login (user,passwd,phone,email) value (%s,%s,%s,%s)')
        try:
            self.cur.execute(sql, [user, passwd, phone, email])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 处理登录
    def login(self, user, passwd):
        sql = "select * from login where user ='%s' and passwd = '%s'" \
              % (user, passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False

    # 忘记密码
    def forgot_passwd(self, user, phone):
        sql = "select * from login where user ='%s' and phone = '%s'" \
              % (user, phone)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False

    # 修改密码
    def change_passwd(self, user, passwd):
        sql = "update login set passwd = '%s'where user= '%s' " \
              % ( passwd,user)
        self.cur.execute(sql)
        self.db.commit()

    #用户修改信息(uid数据类型问题)
    def write(self,ML):
        sql = "insert into user (uname,passwd,gender,age,email) value(%s,%s,%s,%s,%s)"
        a = open(ML, 'r')
        c = a.readlines()
        d = c[0].split()
        self.cur.execute(sql,d)
        self.db.commit()


    #聊天信息
    def chatting(self,b):
        sql = "insert into chat_message (uname,send_time,content) value(%s,%s,%s)"
        self.cur.execute(sql,b)
        self.db.commit()


if __name__ == "__main__":
    db = Database()
    db.create_cursor()
    c = db.login('mxb', '123')
