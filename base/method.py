# coding:utf-8
import requests


class Requests:
	"""
	Request
	"""

	def request(self, url, method, **kwargs):
		"""
		:param url:
		:param method:
		:param kwargs:
		:return:
		"""
		if method == 'get':
			return requests.request(url=url, method=method, **kwargs)
		elif method == 'post':
			return requests.request(method=method, url=url, **kwargs)
		elif method == 'put':
			return requests.request(method=method, url=url, **kwargs)
		elif method == 'delete':
			return requests.request(method=method, url=url, **kwargs)

	def get(self, url, **kwargs):
		"""
		:param url:
		:param kwargs:
		:return:
		"""
		return self.request(url=url, **kwargs)

	def post(self, url, **kwargs):
		"""
		:param url:
		:param kwargs:
		:return:
		"""
		return self.request(url=url, method='post', **kwargs)

	def put(self, url, **kwargs):
		"""
		:param url:
		:param kwargs:
		:return:
		"""
		return self.request(url=url, method='put', **kwargs)

	def delete(self, url, **kwargs):
		"""
		:param url:
		:param kwargs:
		:return:
		"""
		return self.request(url=url, method='delete', **kwargs)


if __name__ == '__main__':
	Requests.request(method='get')
