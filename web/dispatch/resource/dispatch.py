# encoding: utf-8

import warnings

if __debug__:
	from collections import deque

from functools import partial
from inspect import isclass, ismethod

from .exc import InvalidMethod


log = __import__('logging').getLogger(__name__)



class ResourceDispatch(object):
	__slots__ = ()
	
	def __init__(self):
		if __debug__:
			log.debug("Resource dispatch ready.", extra=dict(dispatcher=repr(self)))
		
		super(ResourceDispatch, self).__init__()
	
	def __repr__(self):
		return "ResourceDispatch(0x{id})".format(id=id(self), self=self)
	
	def __call__(self, context, obj, path):
		verb = getattr(context, 'environ', context)['REQUEST_METHOD'].lower() if context else None
		
		if __debug__:
			if not isinstance(path, deque):
				warnings.warn(
						"Your code is not providing the path as a deque; this will be cast in development but"
						"will explode gloriously if run in a production environment.",
						RuntimeWarning, stacklevel=1
					)
				
				if isinstance(path, str):
					path = deque(path.split('/')[1 if not path or path.startswith('/') else 0:])
				else:
					path = deque(path)
			
			log.debug("Preparing resource dispatch. " + repr(obj), extra=dict(
					dispatcher = repr(self),
					context = repr(context),
					obj = repr(obj),
					path = list(path),
					verb = verb,
				))
		
		if isclass(obj):
			obj = obj(context, None, None)
			yield None, obj, False  # Announce class instantiation.
		
		consumed = None
		Resource = getattr(obj, '__resource__', None)
		safe = {i for i in dir(obj) if i[0] != '_'} | {'options'}
		if 'get' in safe: safe.add('head')
		
		if 'response' in context:
			context.response.allow = {i.upper() for i in safe if ismethod(getattr(obj, i, None)) or i in {'head', 'options'}}
		
		if path and path[0] in safe:
			consumed = attr = path.popleft()
			attr = getattr(obj, attr, None)
			if not attr and attr in {'head', 'options'}:
				attr = partial(getattr(self, attr), obj)
			
			if isclass(attr):
				yield consumed, attr(context, obj, None), False
				return
			
			yield consumed, attr, True
			return
		
		if path and Resource:
			try:
				obj = Resource(context, obj, obj[path[0]])
			except KeyError:
				return
			else:
				yield path.popleft(), obj, False
		
		print(obj, verb, safe)
		if verb and verb in safe:
			obj = getattr(obj, verb, None)
			if not obj and verb in {'head', 'options'}:
				obj = partial(getattr(self, verb), obj)
			yield None, obj, True
			return
		
		raise InvalidMethod()
	
	def head(self, obj, *args, **kw):
		"""Allow the get method to set headers, but return no content.
		
		This performs an internal GET and strips the body from the response.
		"""
		obj.get(*args, **kw)
		return
	
	def options(self, obj, *args, **kw):
		"""The allowed methods are present in the returned headers."""
		return ''
