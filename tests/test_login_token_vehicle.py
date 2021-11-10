from base.method import Requests
from utils.operationExcel import OperationExcel, Excel
import pytest
import json

excel = OperationExcel()
obj = Requests()


@pytest.mark.parametrize("datas", excel.runs())
def test_login_vehicle(datas):
	"""
	对参数进行反序列化处理
	:param datas:
	:return:
	"""
	params = datas[Excel.params]
	if len(str(params).strip()) == 0:
		pass
	elif len(str(params).strip()) >= 0:
		print(params)
	# 对请求头进行反序列化处理
	headers = datas[Excel.headers]
	if len(str(headers).strip()) == 0:
		pass
	elif len(str(headers).strip()) >= 0:
		headers = json.loads(headers)
		print(headers)


if __name__ == "__main__":
	pytest.main(["-s", "-v", "test_login_token_vehicle.py", "--alluredir","./report/result"])
	import subprocess

	subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
	subprocess.call('allure open -h 127.0.0.1 -p  8088 ./report/html', shell=True)
