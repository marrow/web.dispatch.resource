# clear; echo "generic.py" | entr -c python3 generic.py

__import__('cinje')

from sys import argv, exit
from os import environ, getcwd, getenv, path
from re import sub

from marrow.package.host import PluginManager

from web.core import Application
from web.db.mongo import MongoDBConnection  # From external dependency: marrow.mongo
from web.dispatch.resource import Collection, Resource  # From external dependency: web.dispatch.resource
from web.ext.annotation import AnnotationExtension
from web.ext.db import DatabaseExtension  # From external dependency: web.db
from web.ext.local import ThreadLocalExtension
from web.ext.serialize import SerializationExtension
from web.ext.template import TemplateExtension

if __debug__: from web.ext.debug import DebugExtension  # Conditional on diagnostic execution.



class Account(Resource):
	def get(self):
		return "GET"
	
	def post(self):
		return "POST"
	
	def configure(self):
		return "Got resource configuration."


class Root(Collection):
	__resource__ = Account
	
	def get(self):
		return "got"
	
	def configure(self):
		return "Got collection configuration."
	
	def __getitem__(self, identifier):
		return {'identifier': identifier, 'sample': "data"}


app = Application(Root, extensions=[DebugExtension()], logging={
		'version': 1,
		'root': {'level': 'DEBUG' if __debug__ else 'INFO', 'handlers': ['console']},
		'loggers': {'web': {'level': 'DEBUG' if __debug__ else 'INFO', 'handlers': ['console'], 'propagate': False}},
		'formatters': {'json': {'()': 'marrow.mongo.util.logger.JSONFormatter'}},
		'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'json', 'level': 'DEBUG', 'stream': 'ext://sys.stdout'}},
	})


context = app._Application__context._promote('ShellContext')


def main(*args):
	"""Primary application execution."""
	
	command = args[0] if args else 'serve'
	
	if command == 'shell':
		pass
	
	elif command == 'serve':
		try:
			app.serve('waitress', host='0.0.0.0', port='8080', threads=20)
		except:
			app.serve('wsgiref', host='127.0.0.1', port='8080')
	
	elif command == 'test':
		from pytest import main as testmain
		argv[0] = sub(r'(-script\.pyw|\.exe)?$', '', argv[0])
		argslist = set(args) - {'test'}
		argv[1:] = ['-W', 'ignore::DeprecationWarning:uri.bucket:', '-W', 'ignore::DeprecationWarning:uri.qso:'] + list(argslist)
		exit(testmain())
	
	return 0


if __name__ == '__main__':
	exit(main(*argv[1:]))

