# *- coding:utf8 *-
import pymysql
from service.SQLlist import SQL_FOR_SELECT_PASSWORD_BY_NAME,SQL_FOR_INSERT_USERS
import uuid

class Users():
    #登录时操作数据库，返回密码
    def isLogin(self, name):
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='recruit', charset='utf8')
        cur = conn.cursor()
        try:
            sql = SQL_FOR_SELECT_PASSWORD_BY_NAME.format(name)
            pwd = ''
            print sql
            cur.execute(sql)
            results = cur.fetchall()
            if results is not None:
                for row in results:
                    pwd = row[0]
            cur.close()
            conn.close()
            return pwd
        except:
            print 'error to get password'
            return ''

    #注册时操作数据库，返回是否成功插入数据库
    def isRegister(self, name, password, isCompony):
        conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='recruit',charset='utf8')
        cur = conn.cursor()
        try:
            sql = SQL_FOR_INSERT_USERS.format(uuid.uuid4(),name,password,isCompony)
            print sql
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            return True
        except:
            print 'error to insert Users'
            return False