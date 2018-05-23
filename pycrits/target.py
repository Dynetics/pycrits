import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsTarget as tar

class Target(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'targets/'

    _fields = [
        tar.ID,
        tar.ACTIONS,
        tar.BUCKET_LIST,
        tar.CAMPAIGN,
        tar.CREATED,
        tar.EMAIL_ADDRESS,
        tar.EMAIL_COUNT,
        tar.LOCATIONS,
        tar.MODIFIED,
        tar.OBJECTS,
        tar.RELATIONSHIPS,
        tar.RELEASABILITY,
        tar.SCHEMA_VERSION,
        tar.SCREENSHOTS,
        tar.SECTORS,
        tar.STATUS,
        tar.TICKETS,

        # Post params
        tar.FIRSTNAME,
        tar.LASTNAME,
        tar.DIVISION,
        tar.DEPARTMENT,
        tar.ORGANIZATION_ID,
        tar.TITLE,
        tar.NOTE,
        ]


    _default_fields = [
        tar.EMAIL_ADDRESS,
    ]