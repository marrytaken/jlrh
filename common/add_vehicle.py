# from base.method import *
# from utils.operationExcel import OperationExcel
import requests
import pytest
import json
import xlrd


def test_getVehicle(path, sheet):
	with xlrd.open_workbook(path, 'rb') as book:  # 打开excel表
		table = book.sheet_by_name(sheet)  # 找到sheet页

		# 获取总行数总列数
		row_num = table.nrows
		col_num = table.ncols
		xlsx_list = []
		key = table.row_values(0)  # 这是第一行数据，返回一个列表，作为字典的key值
		if row_num <= 1:
			print("excel为空")
		else:
			j = 1  # 从第二行获取
			for i in range(row_num - 1):  # 有多少行，读多少行
				xlsx_dict = {}
				values = table.row_values(j)
				for x in range(col_num):  # 有多少列，赋值多少次
					xlsx_dict[key[x]] = values[x]
				j += 1
				xlsx_list.append(xlsx_dict)
			return xlsx_list


#
if __name__ == '__main__':
	read_xlsx0 = test_getVehicle(path="C:\\Users\\Administrator\\Desktop\\车辆类型信息.xls", sheet="vechileType")
	print(read_xlsx0)

