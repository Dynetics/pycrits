import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsSignature as sig

class Signature(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'signatures/'

    _fields = [
        sig.ID,
        sig.ACTIONS,
        sig.BUCKET_LIST,
        sig.CAMPAIGN,
        sig.CREATED,
        sig.DATA,
        sig.DATA_TYPE,
        sig.DATA_TYPE_DEPENDENCY,
        sig.DATA_TYPE_MAX_VERSION,
        sig.DATA_TYPE_MIN_VERSION,
        sig.DESCRIPTION,
        sig.LINK_ID,
        sig.LOCATIONS,
        sig.MD5,
        sig.MODIFIED,
        sig.OBJECTS,
        sig.RELATIONSHIPS,
        sig.RELEASABILITY,
        sig.SCHEMA_VERSION,
        sig.SCREENSHOTS,
        sig.SECTORS,
        sig.SOURCE,
        sig.STATUS,
        sig.TICKETS,
        sig.TITLE,
        sig.VERSION,


        # Exclusively Post Params
        sig.COPY_RELATIONSHIPS, #Requires Link ID
        ]

    _default_fields = [
        sig.TITLE,
        sig.DATA_TYPE,
        sig.SOURCE,
        sig.DATA,
    ]