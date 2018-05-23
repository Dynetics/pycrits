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
__PROXIES = None
__VERIFY = None
__HEADERS = None


def get_headers():
	'''
	Returns the existing headers setting.
	'''

	global __HEADERS
	return __HEADERS


def get_proxies():
	'''
	Returns the existing proxies setting.
	'''

	global __PROXIES
	return __PROXIES


def get_verify():
	'''
	Returns the existing verify setting.
	'''

	global __VERIFY
	return __VERIFY


def connection(headers=None, proxies=None, verify=None):
	'''
	Configure headers, proxies, and verify settings for requests. This is a
	global setting that all requests calls will use unless overridden on a
	per-call basis.

	:param headers: header info for requests.
	:type headers: dict
	:param proxies: proxy info for requests.
	:type proxies: dict
	:param verify: verify info for requests.
	:type verify: bool, str
	'''
	global __HEADERS
	global __PROXIES
	global __VERIFY

	__HEADERS = headers
	__PROXIES = proxies
	__VERIFY = verify
