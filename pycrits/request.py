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
import json
import requests
import urllib

from requests.packages.urllib3.util import Retry

from .access_token import get_access_token, get_api_params, get_api_url
from .connection import get_headers, get_proxies, get_verify
from .logger import do_log, log_message

from .vocabulary import CRITs as c
from .vocabulary import Paging as p

from .vocabulary import Response as R

from .errors import (
    critsFetchError,
    critsValueError
)


class Broker(object):

    '''
    The Broker handles validation and submission of requests as well as
    consumption and returning of the result. It is leveraged by the other
    classes.

    Since the Broker takes care of the entire request/response cycle, it can be
    used on its own to interact with the ThreatExchange API without the need for
    the other classes if a developer wishes to use it.
    '''

    @staticmethod
    def get_new(klass, attrs):
        '''
        Return a new instance of klass.

        :param klass: The class to create a new instance of.
        :type klass: :class:
        :param attrs: The attributes to set for this new instance.
        :type attrs: dict
        :returns: new instance of klass
        '''

        n = klass(**attrs)
        n._new = False
        n._changed = []
        return n


    @staticmethod
    def handle_results(resp):
        '''
        Handle the results of a request.

        :param resp: The HTTP response.
        :type resp: response object
        :returns: dict (using json.loads())
        '''
        if resp.status_code != 200:
            error = json.loads(resp.text).get(R.ERROR, None)
            response = {}
            response['status_code'] = resp.status_code
            response['url'] = resp.url
            if error:
                response[R.MESSAGE] = error.get(R.MESSAGE, None)
                response[R.TYPE] = error.get(R.TYPE, None)
                response[R.CODE] = error.get(R.CODE, None)
                response[R.FBTRACE_ID] = error.get(R.FBTRACE_ID, None)
            raise critsFetchError(response)    
        try:
            results = json.loads(resp.text)
        except:
            raise critsFetchError('Unable to convert response to JSON.')
        return results



    @classmethod
    def build_get_parameters(cls,
                             objectfields = [],
                             query = {},
                             returnfields = [],
                             useor = False,
                             useregex = False,
                             ):

        params = {}

        ## only add items to the query dictionary if they match a searchable field by that object
        if query:
            for key in query:
                if key in objectfields:
                    # Append a "c-" infront of each value; Required by crits to query web api
                    params[("c-" + key)] = query[key]
                else:
                    raise critsValueError(key + " is not a field this type")
        
        ## Fields to return must be passed to crits as a comma-delimited string 
        if returnfields:
            fieldstoreturn = ""
            for item in fieldstoreturn:
                if item in objectfields:
                    fieldstoreturn = fieldstoreturn + item + ','
            fieldstoreturn = fieldstoreturn[:-1]
            params['only'] = fieldstoreturn


        ## These two cannot be valid if no other information is present in params
        if useor:
            if not params: 
                raise critsValueError("OR operator cannot be used without other data")
            params['or'] = '1'

        if useregex:
            if not params:
                raise critsValueError("REGEX operator cannot be used without other data")
            params['regex'] = '1'


        # Finally, update params to include our api key & username
        params.update(get_api_params())

        return params

    @classmethod
    def build_session(cls, retries=None):
        '''
        Build custom requests session with retry capabilities.

        :param retries: Number of retries before stopping.
        :type retries: int
        :returns: requests session object
        '''

        if retries is None:
            retries = 0
        session = requests.Session()
        session.mount('https://',
                      requests.adapters.HTTPAdapter(
                          max_retries=Retry(total=retries,
                                            status_forcelist=[500, 503]
                                            )
                      ))

        return session


    @classmethod
    def request_dict(cls,
                     type_,
                     url,
                     params=None,
                     body=None):
        '''
        Return a dictionary with the request type, URL, and optionally a body.

        :param type_: The request type.
        :type type_: str
        :param url: The request URL.
        :type url: str
        :param params: The parameters to submit.
        :type params: dict
        :param body: The body to submit.
        :type body: str
        :returns: dict
        '''

        request = requests.Request(type_, url, params=params)
        prep = request.prepare()
        full_url = prep.url
        if body:
            body = urllib.urlencode(body)
        return {'type': type_,
                'url': full_url,
                'body': body}





    @classmethod
    def get(cls,
            url,
            params=None,
            retries=None,
            headers=None,
            proxies=None,
            verify=False):
        '''
        Send a GET request.

        :param url: The URL to send the GET request to.
        :type url: str
        :param params: The GET parameters to send in the request.
        :type params: dict
        :param retries: Number of retries before stopping.
        :type retries: int
        :param headers: header info for requests.
        :type headers: dict
        :param proxies: proxy info for requests.
        :type proxies: dict
        :param verify: verify info for requests.
        :type verify: bool, str
        :returns: dict (using json.loads())
        '''

        if not params:
            params = dict()
        if headers is None:
            headers = get_headers()
        if proxies is None:
            proxies = get_proxies()
        if verify is None:
            verify = get_verify()

        #params.update(get_api_params())

        session = cls.build_session(retries)
        resp = session.get(url,
                           params=params,
                           headers=headers,
                           proxies=proxies,
                           verify=verify)
        return cls.handle_results(resp)




    @classmethod
    def patch(cls,
              url,
              data,
              params=None,
              retries=None,
              headers=None,
              proxies=None,
              verify=False):
        '''
        Send a PATCH request.

        :param url: The URL to send the GET request to.
        :type url: str
        :param data: Data to send to the URL.
        :type data: dict
        :param params: The parameters to send in the request.
        :type params: dict
        :param retries: Number of retries before stopping.
        :type retries: int
        :param headers: header info for requests.
        :type headers: dict
        :param proxies: proxy info for requests.
        :type proxies: dict
        :param verify: verify info for requests.
        :type verify: bool, str
        :returns: dict (using json.loads())
        '''

        if not params:
            params = dict()
        if headers is None:
            headers = get_headers()
        if proxies is None:
            proxies = get_proxies()
        if verify is None:
            verify = get_verify()

        params.update(get_api_params())
        session = cls.build_session(retries)

        resp = session.patch(url,
                             data=json.dumps(data),
                             params=params,
                             headers=headers,
                             proxies=proxies,
                             verify=verify)

        return cls.handle_results(resp)





    @classmethod
    def post(cls,
             url,
             files=None,
             params=None,
             retries=None,
             headers=None,
             proxies=None,
             verify=False):
        '''
        Send a POST request.

        :param url: The URL to send the POST request to.
        :type url: str
        :param files: File object pointing to desired file to upload
        :type files: file
        :param params: The POST parameters to send in the request.
        :type params: dict
        :param retries: Number of retries before stopping.
        :type retries: int
        :param headers: header info for requests.
        :type headers: dict
        :param proxies: proxy info for requests.
        :type proxies: dict
        :param verify: verify info for requests.
        :type verify: bool, str
        :returns: dict (using json.loads())
        '''

        if not params:
            params = dict()
        if headers is None:
            headers = get_headers()
        if proxies is None:
            proxies = get_proxies()
        if verify is None:
            verify = get_verify()


        params.update(get_api_params())
        session = cls.build_session(retries)

        resp = session.post(url,
                            data=params,   ## Church: Changed this from params=params to data=params and it actually works now
                            files=files,   ## If user never specified a file, this will be null. Python handles this accordingly
                            headers=headers,
                            proxies=proxies,
                            verify=verify)
        return cls.handle_results(resp)




    @classmethod
    def delete(cls,
               url,
               params=None,
               retries=None,
               headers=None,
               proxies=None,
               verify=None):
        '''
        Send a DELETE request.

        :param url: The URL to send the DELETE request to.
        :type url: str
        :param params: The DELETE parameters to send in the request.
        :type params: dict
        :param retries: Number of retries before stopping.
        :type retries: int
        :param headers: header info for requests.
        :type headers: dict
        :param proxies: proxy info for requests.
        :type proxies: dict
        :param verify: verify info for requests.
        :type verify: bool, str
        :returns: dict (using json.loads())
        '''

        if not params:
            params = dict()
        if headers is None:
            headers = get_headers()
        if proxies is None:
            proxies = get_proxies()
        if verify is None:
            verify = get_verify()

        params.update(get_api_params())
        session = cls.build_session(retries)
        resp = session.delete(url,
                              params=params,
                              headers=headers,
                              proxies=proxies,
                              verify=verify)
        return cls.handle_results(resp)

    @classmethod
    def get_generator(cls,
                      klass,
                      url,
                      to_dict=False,
                      params=None,
                      retries=None,
                      headers=None,
                      proxies=None,
                      verify=None):
        '''
        Generator for managing GET requests. For each GET request it will yield
        the next object in the results until there are no more objects. If the
        GET response contains a 'next' value in the 'paging' section, the
        generator will automatically fetch the next set of results and continue
        the process until the total limit has been reached or there is no longer
        a 'next' value.

        :param klass: The class to use for the generator.
        :type klass: class
        :param url: The URL to send the GET request to.
        :type url: str
        :param to_dict: Return a dictionary instead of an instantiated class.
        :type to_dict: bool
        :param params: The GET parameters to send in the request.
        :type params: dict
        :param retries: Number of retries before stopping.
        :type retries: int
        :param headers: header info for requests.
        :type headers: dict
        :param proxies: proxy info for requests.
        :type proxies: dict
        :param verify: verify info for requests.
        :type verify: bool, str
        :returns: Generator
        '''
        if not klass:
            raise critsValueError('Must provide a valid object to query.')
        if not params:
            params = dict()
        if headers is None:
            headers = get_headers()
        if proxies is None:
            proxies = get_proxies()
        if verify is None:
            verify = get_verify()
        next_ = True
        while next_:
            results = cls.get(url,
                              params=params,
                              retries=retries,
                              headers=headers,
                              proxies=proxies,
                              verify=False)
            if do_log():
                try:
                    has_paging = results.get(c.META, None)
                    prevlink = ''
                    nextlink = ''
                    if has_paging is not None:
                        prevlink = results[c.META][p.PREVIOUS]
                        nextlink = results[c.META][p.NEXT]

                    count = len(results[c.OBJECTS])
                    log_message(
                        'Cursor: PREVIOUS: %s, NEXT: %s, LEN: %d' % (prevlink,
                                                                    nextlink,
                                                                    count
                                                                    )
                    )
                except Exception as e:
                    log_message('Missing key in response: %s' % e)

            #for data in results[t.DATA]:
            for data in results[c.OBJECTS]:
                if to_dict:
                    yield data
                else:
                    yield cls.get_new(klass, data)
            try:
                #next_ = results[t.PAGING][t.NEXT]
                next_ = get_api_url() + results[c.META][p.NEXT]
                ## Remove these prints in produciton - much faster
                print next_
                print '\n\nGETTING NEXT\n\n'
                print '\n\n'
            except:
                log_message('No next in Pager to follow.')
                next_ = False
            if next_:
                url = next_
                params = {}
