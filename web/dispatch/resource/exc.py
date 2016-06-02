# encoding: utf-8

try:
	from webob.exc import HTTPMethodNotAllowed
except ImportError:
	HTTPMethodNotAllowed = RuntimeError


class InvalidMethod(HTTPMethodNotAllowed):
	pass

