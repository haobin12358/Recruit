# *- coding:utf8 *-
from service.Users import Users as sql_user
from flask import request
from common.Result import bad_get
from common.JudgeData import JudgeData
import json

class User():
    def login(self):
        form = request.data
        form = json.loads(form)
        judgeData = JudgeData()
        #先判断是否含有必要参数
        if not judgeData.inData('name',form) or not judgeData.inData('password', form):
            return bad_get
        #根据service层数据处理进行判断
        user = sql_user().isLogin(form['name'])
        if user == form['password']:
            result = {
                "status_code":200,
                "message":"ok"
            }
        else:
            result = {
                "status":404,
                "status_code":404999,
                "message":"error"
            }
        return result
    def resgister(self):
        form = request.data
        form = json.loads(form)
        judgeData = JudgeData()
        #先判断是否含有必要参数
        if not judgeData.inData('name', form) or not judgeData.inData('password', form) \
                or not judgeData.inData('isCompony', form):
            return bad_get
        #进行数据库写入操作
        user = sql_user.isRegister(form['name'], form['password'], form['isCompony'])
        if user:
            result = {
                "status_code":200,
                "message":"注册成功"
            }
        else:
            result = {
                "status":404,
                "status_code":404999,
                "message":"error"
            }

        return result
