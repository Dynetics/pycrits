import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsComment as com
class Comment(Common):
    '''
    This can only be called via POST;
    Can't be used to do something like
    iterate through all comments. 
    ONLY used to add comment to a specific
    record
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'comments/'

    _fields = [
        com.COMMENT,
        com.OBJECT_ID,
        com.OBJECT_TYPE,
    ]


    _default_fields = [
        com.COMMENT,
        com.OBJECT_ID,
        com.OBJECT_TYPE,
    ]