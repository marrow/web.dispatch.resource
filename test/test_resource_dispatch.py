# encoding: utf-8

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


def test_resource_dispatch_repr():
	assert repr(ResourceDispatch()).startswith('ResourceDispatch(0x')











