# encoding: utf-8

import pytest

from web.dispatch.resource.helper import Collection


class TestCollection(object):
	def test_dispatcher(self):
		assert Collection.__dispatch__ == 'resource'
	
	def test_resource(self):
		assert Collection.__resource__ is None
	
	def test_getitem_failure(self):
		coll = Collection(None)
		
		with pytest.raises(NotImplementedError):
			coll[27]

