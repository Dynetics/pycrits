import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsIP as ip

class IP(Common):
    '''
    '''

    _URL = '/' + c.API + c.VERSION + 'ips/'

    _fields = [
        ip.ID,
        ip.ACTIONS,
        ip.BUCKET_LIST,
        ip.CAMPAIGN,
        ip.CREATED,
        ip.DESCRIPTION,
        ip.IP,
        ip.LOCATIONS,
        ip.MODIFIED,
        ip.OBJECTS,
        ip.REFERENCE,
        ip.RELATIONSHIPS,
        ip.RELEASABILITY,
        ip.SCHEMA_VERSION,
        ip.SCREENSHOTS,
        ip.SECTORS,
        ip.SOURCE,
        ip.STATUS,
        ip.TICKETS,
        ip.TYPE,

        # Exclusively Post Params
        ip.ADD_INDICATOR,
        ip.INDICATOR_REFERENCE,
        ip.IP_TYPE,

        ]

    _default_fields = [
        ip.IP,
        ip.IP_TYPE,  #Must be one of the types outline in the gui
        ip.SOURCE,
    ]
