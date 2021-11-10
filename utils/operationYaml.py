import yaml
from common.public import filepath


class OperationYaml:
	"""
	操作yaml文件
	"""

	def readYaml(self):
		"""
		readYaml
		:return:
		"""
		with open(filepath(), 'r', encoding="utf-8") as f:
			return list(yaml.safe_load_all(f))

	def dictYaml(self, fileDir='config', fileName='book.yaml'):
		"""
		获取book.yaml文件的内容为字典
		:return:
		"""
		with open(filepath(fileDir=fileDir, fileName=fileName), 'r', encoding='utf-8') as f:
			return yaml.safe_load(f)


if __name__ == "__main__":
	obj = OperationYaml()
	print(obj.dictYaml())