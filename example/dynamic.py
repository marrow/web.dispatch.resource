"""An example WebCore application utilizing resource dispatch."""

from web.core import Application
from web.dispatch.resource import Collection, Resource



class Person(Resource):
	def get(self):
		return "I'm a person named " + self._record
	
	def post(self, name):
		return "You updated " + self._record
	
	def put(self):
		return "You replaced " + self._record
	
	def delete(self):
		return "You deleted " + self._record


class People(Collection):
	__resource__ = Person
	
	def __init__(self, context, collection=None, record=None):
		self._ctx = context
	
	def get(self):
		return "List of people: " + ", ".join(self._members)
	
	def post(self):
		return "Create a new person."
	
	def put(self):
		return "Replace all people."
	
	def delete(self):
		return "Delete all people."
	
	def __getitem__(self, identifier):
		return identifier


app = Application(People, logging=dict(level='debug'))


if __name__ == '__main__':
	app.serve('wsgiref')


