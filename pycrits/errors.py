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

class critsAPIException(Exception):

	'''
	Generic Exception.
	'''

	def __init__(self, message):
		self.message = message

	def __str__(self):
		log_message(self.message)
		return self.message

class critsInputError(critsAPIException):
	'''
	Exception raised for errors in CRITs input.

	Attributes:

		expr -- Input expression in which the error occurred
		msg  -- Explanation of the error
	'''
	#def __init__(self, expr, msg):
	#	self.expr = expr
	#	self.msg = msg


class critsAccessTokenError(critsAPIException):

	'''
	Exception for when we the developer don't set a token before instantiating
	an object.
	'''


class critsFetchError(critsAPIException):

	'''
	Exception for when a GET or POST attempt fails.
	'''


class critsValueError(critsAPIException):

	'''
	Exception for when we are given a value we are not expecting or is invalid.
	'''

class critsAttributeError(critsAPIException):

    """
    Exception for when we are given a value we are not expecting or is invalid.
    """
