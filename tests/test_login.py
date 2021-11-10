import pytest
from base.method import Requests
from utils.operationYaml import OperationYaml
from common.add_vehicle import test_getVehicle


def add_vechicleType():
	"""
	批量添加车辆类型
	"""
	for i in test_getVehicle(path="C:\\Users\\Administrator\\Desktop\\车辆类型信息.xls", sheet="vechileType"):
		print(i)


if __name__ == "__main__":
	add_vechicleType()

# class testLogin:
# 	"""
# 	登录类
# 	"""
# 	obj = Requests()
# 	objYaml = OperationYaml()
#
# 	@pytest.mark.parametrize('data', objYaml.readYaml())
# 	def test_login(self, data):
# 		print(type(data['data']))
# 		r = self.obj.post(url=data['url'], json=data['data'])
# 		print(self.r.json())


# def getToken(self):
# 	"""
# 	获取token
# 	:return:
# 	"""
# 	Token = self.test_login[]


# if __name__ == "__main__":
# 	pytest.main(["-s", "-v", "test_login.py"])
