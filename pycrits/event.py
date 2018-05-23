import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsEvent as eve

class Event(Common):
    '''
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'events/'

    _fields = [
        eve.ID,
        eve.ACTIONS,
        eve.BUCKET_LIST,
        eve.CAMPAIGN,
        eve.CREATED,
        eve.DESCRIPTION,
        eve.EVENT_ID,
        eve.EVENT_TYPE,
        eve.LOCATIONS,
        eve.MODIFIED,
        eve.OBJECTS,
        eve.RELATIONSHIPS,
        eve.RELEASABILITY,
        eve.SCHEMA_VERSION,
        eve.SCREENSHOTS,
        eve.SECTORS,
        eve.SOURCE,
        eve.STATUS,
        eve.TICKETS,
        eve.TITLE,

        #Exclusive post params
        eve.DATE,
        ]

    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type EVENT
    _default_fields = [
        eve.TITLE,
        eve.EVENT_TYPE,
        eve.SOURCE,
        eve.DESCRIPTION,
    ]