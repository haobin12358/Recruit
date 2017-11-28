# *- coding:utf8 *-
from service.Users import Users

class User():

    def isLogin(self, form):
        name = form["a"]
        password = form["b"]
        #传递数据库信息，判断数据库处理结果
        if Users.isLogin(name, password):
            return True
        return False
