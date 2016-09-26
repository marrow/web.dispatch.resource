# encoding: utf-8

from webob import Request
from web.core import Application


class Rig(object):
	def do(self, verb, path='/', host="http://localhost", **data):
		app = Application(self.root)
		
		req = Request.blank(host + path)
		req.method = verb
		
		if data:
			req.content_type = 'application/json'
			req.json = data
		
		return req.get_response(app)

