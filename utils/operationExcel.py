# coding:utf-8
import json

import xlrd

from common.public import filepath


class Excel:
	"""
	调用第几行
	"""
	CassId = "测试用例ID"
	caseModel = "模块"
	caseName = "接口名称"
	caseUrl = "请求地址"
	casePre = "前置条件"
	method = "请求方法"
	paramsType = "请求参数类型"
	params = "请求参数"
	expect = "期望结果"
	isRun = "是否运行"
	headers = "请求头"
	status_code = "状态码"


class OperationExcel:
	"""
	excel类
	"""

	def getSheel(self):
		"""
		方法
		"""
		book = xlrd.open_workbook(filepath("data", "TestCase.xls"))
		return book.sheet_by_index(0)

	def getExcelDates(self):
		"""
		获取表总数据
		:return:
		"""
		dates = list()
		title = self.getSheel().row_values(0)
		# 忽略首行
		for row in range(1, self.getSheel().nrows):
			row_values = self.getSheel().row_values(row)
			dates.append(dict(zip(title, row_values)))
		return dates

	def runs(self):
		"""
		获取可执行的用例
		:return:
		"""
		run_list = []
		for items in self.getExcelDates():
			isRun = items[Excel.isRun]
			# print(isRun)
			if isRun == 'y':
				run_list.append(items)
			else:
				pass
		return run_list

	def case_prev(self, casePrev):
		"""
		依据前置测试条件找到关联的前置测试用例
		:param casePrev:前置测试条件
		:return:
		"""
		for item in self.runs():
			if casePrev in item.values():
				return item
		return None
# def params(self):
# 	"""
# 	对请求参数为空做处理
# 	:return:
# 	"""
# 	params_list = []
# 	for item in self.runs():
# 		params = item[Excel.params]
# 		if len(str(params).strip()) == 0:
# 			pass
# 		elif len(str(params).strip()) >= 0:
# 			# params_list.append(json.loads(params))
# 			print(params)
# return params_list


if __name__ == "__main__":
	obj = OperationExcel()
	obj.getSheel()
	# print(obj.case_prev('login')[Excel.caseUrl])
# print(obj.case_prev())
# print(type(obj.params()))
