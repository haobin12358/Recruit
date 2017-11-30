# *- coding:utf8 *-
from flask_restful import Resource
from control.Works import Works as c_work
from common.JudgeData import JudgeData
from common.Result import bad_result
import json

'''
    用于处理招聘岗位的接口
    根据函数名称确认接口方法
    根据apis中的key来判断接口的指向
'''
class Works(Resource):
    def get(self, work):
        judgeData = JudgeData()
        apis = {
            "listworks":"{0}".format(c_work.listworks()),
            "deworks":"{0}".format(c_work.deworks())
        }

        if judgeData.inData(work, apis):
            json_obj = apis[work].replace("\'", "\"")
            json_obj = json.loads(json_obj)
            return json_obj
        return bad_result

    def post(self, work):
        judgeData = JudgeData()
        apis = {
            "deworks":"{0}".format(c_work.pdeworks())
        }

        if judgeData.inData(work, apis):
            json_obj = apis[work].replace("\'", "\"")
            json_obj = json.loads(json_obj)
            return json_obj

        return bad_result