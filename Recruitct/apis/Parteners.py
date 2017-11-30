# *- coding:utf8 *-
from flask_restful import Resource

'''
    用于处理应征者的接口
    根据函数名称确认接口方法
    根据apis中的key来判断接口的指向
'''
class Parteners(Resource):
    def get(self):

        apis = {
            "base":"{0}",
            "school":"{0}",
            "work":"{0}",
            "tech":"{0}"
        }
        pass
    def post(self):
        apis = {
            "base": "{0}",
            "school": "{0}",
            "work": "{0}",
            "tech": "{0}"
        }
        pass