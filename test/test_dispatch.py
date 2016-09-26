# encoding: utf-8

import pytest
from webob import Request

from web.core import Application
from web.dispatch.resource import ResourceDispatch


class Rig(object):
	def do(self, verb, path='/', host="http://localhost", **data):
		app = Application(self.root)
		
		req = Request.blank(host + path)
		req.method = verb
		
		if data:
			req.content_type = 'application/json'
			req.json = data
		
		return req.get_response(app)



class TestResourceDispatchExtras(object):
	def test_repr(self):
		assert repr(ResourceDispatch()).startswith('ResourceDispatch(0x')
	
	def test_head_calls_get(self):
		class Foo(object):
			def get(self):
				raise NotImplementedError()
		
		disp = ResourceDispatch()
		
		with pytest.raises(NotImplementedError):
			disp.head(Foo())
	
	def test_head_returns_none(self):
		class Foo(object):
			def get(self):
				return 27
		
		disp = ResourceDispatch()
		
		assert disp.head(Foo()) is None
	
	def test_options_behaviour(self):
		disp = ResourceDispatch()
		
		assert disp.options(None) is None









