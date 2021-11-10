from base.method import Requests
from utils.operationYaml import OperationYaml
from utils.operationExcel import OperationExcel
import pytest
import json
from common.public import *


class TestVehicleType:
	"""
	车辆类型管理测试
	"""
	excel = OperationExcel()
	obj = Requests()

	def result(self, row, r):
		"""
		断言（实际结果和预期结果进行判断是否匹配）
		:param r:
		:param row:
		:return:
		"""
		assert r.status_code == 200
		assert self.excel.getExpect(row=row) in json.dumps(r.json(), ensure_ascii=False)

	def test_VehicleType_001(self):
		"""
		获取所有车辆的信息
		:return:
		"""
		r = self.obj.get(url=self.excel.getUrl(row=1))
		self.result(r=r, row=1)

	def test_VehicleType_002(self):
		"""
		添加车辆类型
		:return:
		"""
		r = self.obj.post(url=self.excel.getUrl(row=2))
		self.result(r=r, row=2)


if __name__ == "__main__":
	pytest.main(["-s", "-v", "test_vehicleType.py"])
