import os


def filepath(fileDir='data', fileName='login.yaml'):
	"""
	:param fileDir:目录
	:param fileName:要操作的文件名称
	"""
	return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)


def writeContent(content):
	"""
	写入车辆类型ID至文件中
	:param content:
	:return:
	"""
	with open(filepath(fileDir='data', fileName='tableId'), 'w') as f:
		f.write(str(content))


writeContent(1)

# print(filepath('config', 'config.yaml'))
