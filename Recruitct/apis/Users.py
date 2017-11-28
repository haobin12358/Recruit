# *- coding:utf8 *-
from flask_restful import Resource
from flask import request
from control.Users import User
import json

class Login(Resource):
    '''
        用户登录功能，post方法
        需要提供含有name和password的body体
    '''
    def post(self):
        form = request.data
        form = json.loads(form)
        #根据control层数据处理进行判断
        if User().isLogin(form):
            result = {
                "status_code":200,
                "message":"ok"
            }

        else:
            result = {
                "status_code":404001,
                "message":"error"
            }
        return result

class Resgiter(Resource):
    '''
        用户注册功能，post方法
        需要提供含有name和password、isCompony的body体
    '''
    def post(self):
        print 1
        return {}

class Test(Resource):
    '''
        测试用接口
    '''
    def get(self):
        return 'hello world'

