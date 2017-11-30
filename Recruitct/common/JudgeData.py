# *- coding:utf8 *-

class JudgeData():

    def inData(self, param, jsonitem):
        for row in jsonitem.keys():
            if row == param:
                return True
        return False