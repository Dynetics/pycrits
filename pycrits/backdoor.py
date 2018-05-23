import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsBackdoor as bac

class Backdoor(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'backdoors/'

    _fields = [
        bac.ID,
        bac.ACTIONS,
        bac.ALIASES,
        bac.BUCKET_LIST,
        bac.CAMPAIGN,
        bac.CREATED,
        bac.LOCATIONS,
        bac.MODIFIED,
        bac.NAME,
        bac.OBJECTS,
        bac.RELATIONSHIPS,
        bac.RELEASABILITY,
        bac.SCHEMA_VERSION,
        bac.SCREENSHOTS,
        bac.SECTORS,
        bac.SOURCE,
        bac.STATUS,
        bac.TICKETS,
        bac.VERSION,
        bac.DESCRIPTION,

        # POST-Specific fields
        # None
        ]


    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type Backdoor
    _default_fields = [
        bac.NAME,
        bac.SOURCE,
    ]