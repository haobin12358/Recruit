# *- coding:utf8 *-
from flask_restful import Resource

'''
    用于处理发布项目s的接口
    根据函数名称确认接口方法
    根据apis中的key来判断接口的指向
'''
class Items(Resource):
    def get(self):

        apis = {
            "listitems":"{0}",
            "deitems":"{0}"
        }
        pass
    def post(self):

        apis = {
            "deitems":"{0}"
        }
        pass