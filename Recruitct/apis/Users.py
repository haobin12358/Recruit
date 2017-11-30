# *- coding:utf8 *-
from flask_restful import Resource
from common.Result import bad_result
from control.Users import User
from common.JudgeData import JudgeData
import json

'''
    用于处理关于用户的接口
    根据函数名称确认接口方法
    根据apis中的key来判断接口的指向
'''
class Users(Resource):
    def post(self, name):
        user = User()
        judgeData = JudgeData()

        #api列表的定义
        apis = {
            'login':'{0}'.format(user.login()),
            'register':'{0}'.format(user.resgister())
        }
        #将字符串中自动转化的单引号换成双引号，保证json格式，之后loads形成json
        json_obj = apis[name].replace("\'","\"")
        json_obj = json.loads(json_obj)

        #判断是否含有对应的api
        if judgeData.inData(name, apis):
            return json_obj

        return bad_result




