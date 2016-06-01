# encoding: utf-8

"""An example WebCore application utilizing resource dispatch."""

from web.core import Application



class Person(object):
	"""A class representing a singular resource.
	
	A resource may have additional sub-collections assigned as named attributes, similar to object dispatch, and may
	itself represent a collection by including a `__resource__` reference to a child resource class. (Defining
	`__resource__` enables the `__getitem__` logic for semi-automatic child resource instantiation.)
	
	Two HTTP verbs have special-casing: `HEAD` and `OPTIONS`.  `HEAD` requests are automatically internally redirected
	to the `get` method, if present, with the response body thrown away. (Using a deferred body iterator such as a
	cinje template means you skip the template processing time when serving `HEAD` responses.)  You may still wish to
	override behaviour on this, so any resource-defined `head` method takes precedence.
	
	The default `OPTIONS` handler returns a list of non-underscore-prefixed methods, upper-cased, as available verbs.
	This, too, can be overridden if needed. (For the purists there is no need to subclass to benefit from these
	defaults.)
	
	Non-prefixed attributes that are classes are treated in roughly the same way as object dispatch: if the next path
	element matches the name of the attribute, it will be returned as an intermediary or dispatch midpoint and
	dispatch will defer back to the framework to determine the next steps for processing. (This lets you easily
	transition from a resource tree into non-resource-based object dispatch or registered routes as dispatch
	descends.)
	"""
	
	__dispatch__ = 'resource'
	
	def __init__(self, context, collection, record):
		"""Initialize a singular resource.
		
		Resources are passed a copy of the processing (request) context, a reference to the contianing collection, and
		the record loaded via parent `__getitem__`. If you subclass the `Resource` helper class this method is
		provided for you, implemented as you see below.
		
		The full "dispatch path", including collection and resource references, is provided in `context.path` as part
		of standard WebCore dispatch processing. This is extremely useful to build "breadcrumb" navigation lists, as
		one possible example.
		
		Since one resource may contain several others, the `record` argument may actually be `None` if it represents
		an attachment like this, and "collection" will actually be the enclosing resource. (Arguments are passed
		positionally, so you may name the argument more appropriately in those cases.)
		"""
		
		self._ctx = context
		self._collection = collection
		self._record = record
	
	def get(self):
		"""GET handler.
		
		HTTP verbs are methods of resources. Any method defined without a leading underscore is assumed to be a verb.
		"""
		return "I'm a person named " + self._record
	
	def post(self, name):
		return "You updated " + self._record
	
	def put(self):
		return "You replaced " + self._record
	
	def delete(self):
		return "You deleted " + self._record


class People(object):  # No subclassing is strictly necessary.
	__dispatch__ = 'resource'  # Inform WebCore that we wish to use resource dispatch for this handler.
	__resource__ = Person  # This is the Resource to instantiate for members of this collection.
	
	_members = ['alice', 'bob', 'eve']  # We mock this, but it'd probably come from your database.
	
	def get(self):
		return "List of people: " + ", ".join(self._members)
	
	def post(self):
		return "Create a new person."
	
	def put(self):
		return "Replace all people."
	
	def delete(self):
		return "Delete all people."
	
	def __getitem__(self, identifier):
		"""Load a record for the given identifier, raising KeyError on lookup failure.
		
		This is called when there are additional path elements to consume after the collection level and the result is
		passed as a second argument to the resource class' constructor, after the context.
		
		It's not uncommon to use mix-ins to provide this method, as lookup from different database types is fairly
		uniform within that database type, for example, marrow.mongo provides MongoDBCollection and GridFSCollection
		mix-ins.
		"""
		
		if identifier not in self._members:
			raise KeyError()
		
		return identifier


app = Application(People)


if __name__ == '__main__':
	app.serve('wsgiref')

