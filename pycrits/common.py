'''

This file is heavily derived from the project ThreatExchange. The license for
ThreatExchange (https://github.com/facebook/ThreatExchange) is as follows: 


BSD License

For ThreatExchange software

Copyright (c) 2017, Mike Goffin. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

 * Neither the name Facebook nor the names of its contributors may be used to
   endorse or promote products derived from this software without specific
   prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
SOFTWARE.

'''
from .request import Broker

from .vocabulary import CRITsCommon as c

from .errors import (
	critsAttributeError,
	critsValueError
)


class class_or_instance_method(object):

	'''
	Custom decorator. This binds to the class if no instance is available,
	otherwise it will bind to the instance.

	This allows us to use a single method which can take both "self" and "cls"
	as the first argument.
	'''

	def __init__(self, func):
		self.func = func

	def __get__(self, instance, cls=None):
		if instance is None:
			return classmethod(self.func).__get__(None, cls)
		return self.func.__get__(instance, cls)


class Common(object):

	_internal = [
		'_DETAILS',
		'_RELATED',
		'_changed',
		'_new',
		'_access_token',
		c.ID
	]

	_changed = []
	_new = True

	def __init__(self, **kwargs):
		'''
		Initialize the object. Set any attributes that were provided.
		'''

		for name, value in kwargs.items():
			self.__setattr__(name, value)


	def __getattr__(self, attr):
		'''
		Get an attribute. If the attribute does not exist, return None
		'''
		
		if attr not in self._fields:
			raise critsAttributeError('%s is not a valid attribute' % attr)

		try:
			return object.__getattribute__(self, attr)
		except:
			return None

	def set(self, name, value):
		'''
		Wrapper around __setattr__ making it easier to use the vocabulary to set
		class attributes.

		:param name: The name of the attribute to set.
		:type name: str
		:param value: The value to set the attribute to.
		:type value: None, int, str, bool
		'''

		return self.__setattr__(name, value)

	def get(self, attr):
		'''
		Wrapper around __getattr__ making it easier to use the vocabulary to get
		class attributes.

		:param attr: The name of the attribute to get.
		:type attr: str
		'''

		return self.__getattr__(attr)

	def populate(self, attrs):
		'''
		Given a dictionary, populate self with the keys as attributes.

		:param attrs: A dictionary used as attributes and values.
		:type attrs: dict
		'''

		for k, v in attrs.iteritems():
			self.set(k, v)

	def to_dict(self):
		'''
		Convert this object into a dictionary.

		:returns: dict
		'''

		d = dict(
			(n, getattr(self, n, None)) for n in self._fields
		)
		return d

	@classmethod
	def objects(cls,
				query = {},
				returnfields = [],
				useor = False,
				useregex=False,
				__raw__ = None,
				full_response=False,
				dict_generator=False,
				request_dict=False,
				retries=None,
				headers=None,
				proxies=None,
				verify=False,):
		
		'''
		This function should be called when an individual wants to get objects from crits
		When called with no params, this will return every item in that particular crits index


		:param query: Contains key:pair values (dict) of fields that should 
					  be filtered upon where the key is the name of the value
					  defined in "vocabularly.py" and key is the desired value
	    :type query: dict
	    :param returnfields: List that contains all fields that should
	    					 be returned by objects; Use to trim unnecessary data
	    					 NOTE: This will also return all required fields (ex. id, created date,etc)
		:type returnfields: list[string]
		:param useor: CRITs uses ANDs in all fields by default; Make this true to disable that
		:type useor: bool
		:param regex: Switch simple text filtering to custom regex filtering
		:type regex: bool
		:param __raw__: Provide a dictionary to force as GET parameters.
						Overrides all other arguments.
		:type __raw__: dict
		:param full_response: Return the full response instead of the generator.
							  Takes precedence over dict_generator.
		:type full_response: bool
		:param dict_generator: Return a dictionary instead of an instantiated
							   object.
		:type dict_generator: bool
		:param request_dict: Return a request dictionary only.
		:type request_dict: bool
		:param retries: Number of retries to fetch a page before stopping.
		:type retries: int
		:param headers: header info for requests.
		:type headers: dict
		:param proxies: proxy info for requests.
		:type proxies: dict
		:param verify: verify info for requests.
		:type verify: bool, str
		:returns: Generator, dict (using json.loads()), str
		'''

		objectfields = cls._fields

		if query:
			if not (isinstance(query, dict)):
				raise critsValueError('query must be of type dict')

		if returnfields:
			if not (isinstance(returnfields, list)):
				raise critsValueError('returnfields must be of type list')



		if not __raw__:
			params = Broker.build_get_parameters(
			objectfields = objectfields,
			query = query,
			returnfields = returnfields,
			useor = useor,
			useregex = useregex,
			)

		if request_dict:
			return Broker.request_dict('GET',
									   cls._URL,
									   params=params)
		if full_response:
			return Broker.get(cls._URL,
							  params=params,
							  retries=retries,
							  headers=headers,
							  proxies=proxies,
							  verify=verify)
		else:
			return Broker.get_generator(cls,
										cls._URL,
										to_dict=dict_generator,
										params=params,
										retries=retries,
										headers=headers,
										proxies=proxies,
										verify=verify)


	@classmethod
	def new(cls,
			params,
			file = None,
			request_dict=False,
			retries=None,
			headers=None,
			proxies=None,
			verify=False):
		'''
		Create a new object in CRITs

		:param params: The parameters to submit.
		:type params: dict
		:param file: Path to the file that should be uploaded
		:type file: str
		:param request_dict: Return a request dictionary only.
		:type request_dict: bool
		:param retries: Number of retries to submit before stopping.
		:type retries: int
		:param headers: header info for requests.
		:type headers: dict
		:param proxies: proxy info for requests.
		:type proxies: dict
		:param verify: verify info for requests.
		:type verify: bool, str
		:returns: dict (using json.loads()), str
		'''


		# Lets ensure that the user hasn't specified any strange parameter
		for key in params:
			if key not in cls._fields:
				raise critsValueError("Invalid paramater " + key)


		# So if we're here we know the user has valid paramaters. But...
		# Do they have the required params? Lets check:
		for field in cls._default_fields:
			if field not in params:
				raise critsValueError("Required paramater not found " + field)



		# Handling if the user submitted a file --> This block is confusing. Can we simplify?
		filedata = {}
		validfileuploadclasses = ['PCAP', 'Certificate', 'Sample', 'Raw', 'Screenshot']

		# If the user gives a file but they are not using a class that accepts files
		if file and cls.__name__ not in validfileuploadclasses:
			raise critsValueError(str(cls.__name__) +" does not accept file uploads")

		## Commented this because some classes can use files but not required
		## Devise a better solution
		# Else if the user does not give a file but is using a class that requires a file
		#elif not file and cls.__name__ in validfileuploadclasses:
			#raise critsValueError(str(cls.__name__) + " requires a file upload, but none was given")

		# If users args pass both checks and they are using a file, handle properly
		elif file:
			filedata = {'filedata':open(file,'rb')}



		if request_dict:
			return Broker.request_dict('POST',
									   cls._URL,
									   body=params)
		else:
		    return Broker.post(cls._URL,
						       params=params,
						       files=filedata,
						       retries=retries,
						       headers=headers,
						       proxies=proxies,
						       verify=verify)




	@class_or_instance_method
	def update(cls,
			   id,
			   data,
			   params=None,
			   retries=None,
			   headers=None,
			   proxies=None,
			   verify=False):
		'''
		This function utilizies the PATCH request to
		update data on a record already in CRITS.
		See the wiki for more info

		:param id: The ID (in crits) of the object.
		:type id: string
		:param data: The data containing information regarding
					 what to update on this specific object
					 (see wiki for more info).
		:type data: dict 
		:param headers: header info for requests.
		:type headers: dict
		:param proxies: proxy info for requests.
		:type proxies: dict
		:param verify: verify info for requests.
		:type verify: bool, str
		:returns: dict (using json.loads()), str

		'''



		_url = cls._URL + "/" + id + "/"

		return Broker.patch(_url,
							params=params,
							data=data,
							retries=retries,
							headers=headers,
							proxies=proxies,
							verify=verify)


	## Not yet working - I believe the authenticated API
	## is not ready to accept delete requests yet
	def delete(cls,
			   id,
               params=None,
               retries=None,
               headers=None,
               proxies=None,
               verify=False):

		_url = cls._URL + "/" + id + "/"

		return Broker.delete(_url,
				 			params=params,
    					 	retries=retries,
    					 	headers=headers,
    					 	proxies=proxies,
    					 	verify=verify)

