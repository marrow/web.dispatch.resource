# encoding: utf-8

from web.dispatch.resource.helper import Resource


class TestResource(object):
	def test_dispatcher(self):
		assert Resource.__dispatch__ == 'resource'
	
	def test_constructor(self):
		res = Resource(1, 2, 3)
		assert res._ctx is 1
		assert res._collection is 2
		assert res._record is 3
	
	def test_constructor_defaults(self):
		res = Resource(1)
		assert res._ctx is 1
		assert res._collection is res._record is None

