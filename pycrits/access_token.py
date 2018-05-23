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
import os

from .errors import critsAccessTokenError
from .vocabulary import CRITsAccessToken as at


__ACCESS_TOKEN = None
# File level global


def _read_token_file(token_file):
	'''
	Read a token file. Separated out for easy mocking during unit testing.

	Args:
		token_file (str): The full path and filename of the access token file.
	
	Returns:
		str: The first line of the token file
	
	Raises:
		critsAccessTokenError
	'''

	try:
		with open(token_file, 'r') as infile:
			return infile.readline().strip()
	except IOError as e:
		raise critsAccessTokenError(str(e))

def get_api_params():
	'''
	'''

	global __ACCESS_TOKEN

	if not __ACCESS_TOKEN:
		access_token()

	if not __ACCESS_TOKEN:
		raise critsAccessTokenError('Must access_token() before instantiating')

	return {'username': __ACCESS_TOKEN.split('|')[1], 'api_key': __ACCESS_TOKEN.split('|')[2]}


def get_access_token():
	'''
	Returns:
		str: Returns the existing access token if access_token() has been called.
			 Will attempt to access_token() in the case that there is no access token.

	Raises:
		critsAccessTokenError
	'''

	global __ACCESS_TOKEN

	if not __ACCESS_TOKEN:
		access_token()

	if not __ACCESS_TOKEN:
		raise critsAccessTokenError('Must access_token() before instantiating')

	return __ACCESS_TOKEN

def get_api_url():
	'''
	Returns:
		str: The fully qualified URL for the CRITs API.

	Raises:
		critsAccessTokenError
	'''

	token = get_access_token()
	try:
		return token.split('|')[0]
	except:
		raise critsAccessTokenError('Could not derive the crits URL from the token')

def get_user_id():
	'''
	Returns:
		str: The user_id.

	Raises:
		critsAccessTokenError
	'''

	token = get_access_token()
	try:
		return token.split('|')[1]
	except:
		raise critsAccessTokenError('Could not derive user-id from token')


def _find_token_file():
	'''
	Returns:
		str: The full path to the CRITS API token file

	'''

	for loc in [os.curdir, os.path.expanduser('~')]:
		filepath = os.path.join(loc, '.crits')
		if os.path.exists(filepath):
			return filepath

	return None


def access_token(crits_url=None, user_id=None, api_key=None, token_file=None):
	'''
	Use the user_id and api_key to store the access_token globally for all
	instantiated objects to leverage.

	There are many ways to specify the user_id and api_key. In order, we will try:
	 1. Use the value of the 'CRITS_ACCESS_TOKEN' environment variable.
	 2. Use the concatenation of the 
	 		'CRITS_API_URL', 'CRITS_USER_ID' and 'CRITS_API_KEY' environment variables.
	 3. Use the first line of the file '$PWD/.crits' or ~/.crits'
	 4. Use the concatenation of the user_id and api_key parameters
	 5. Use the first line of the file 'token_file'

	Args:
		user_id (str, optional): The user id to use
		api_key (str, optional): The api key to use
		token_file (str, optional): The full path to the CRITS API token file

	Raises:
		critsAccessTokenError
	'''

	global __ACCESS_TOKEN

	# 1. Use the concatenation of the user_id and api_key parameters
	if crits_url and user_id and api_key:
		__ACCESS_TOKEN = crits_url + '|' + user_id + '|' + api_key
		return

	# 2. Use the value of the 'CRITS_ACCESS_TOKEN' environment variable.
	__ACCESS_TOKEN = os.environ.get(at.CRITS_ACCESS_TOKEN, None)
	if __ACCESS_TOKEN:
		return

	# 3. Use the concatenation of the 'CRITS_USER_ID' and 'CRITS_API_KEY' environment variables.
	env_crits_url = os.environ.get(at.CRITS_API_URL, None)
	env_user_id = os.environ.get(at.CRITS_USER_ID, None)
	env_api_key = os.environ.get(at.CRITS_API_KEY, None)
	if env_crits_url and env_user_id and env_api_key:
		__ACCESS_TOKEN = env_crits_url + '|' + env_user_id + '|' + env_api_key
		return

	# 4. Use the first line of the file 'token_file'
	if token_file:
		__ACCESS_TOKEN = _read_token_file(token_file)
		return

	raise critsAccessTokenError('Unable to set access token.')