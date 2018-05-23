import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsDomain as dom

class Domain(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'domains/'

    _fields = [
        dom.ID,
        dom.ACTIONS,
        dom.ANALYST,
        dom.BUCKET_LIST,
        dom.CAMPAIGN,
        dom.CREATED,
        dom.DOMAIN,
        dom.LOCATIONS,
        dom.MODIFIED,
        dom.OBJECTS,
        dom.RELATIONSHIPS,
        dom.RELEASABILITY,
        dom.SCHEMA_VERSION,
        dom.SCREENSHOTS,
        dom.SECTORS,
        dom.SOURCE,
        dom.STATUS,
        dom.TICKETS,
        dom.TYPE,
        dom.WATCHLISTENABLED,

        # POST-Specific fields
        dom.ADD_INDICATORS,
        dom.ADD_IP,
        dom.IP_TYPE,
        dom.IP_SOURCE,
        dom.IP_METHOD,
        dom.IP_REFERENCE,
        dom.SAME_SOURCE,
    ]

    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type DOMAIN
    _default_fields = [
        dom.DOMAIN, # If this does not have a url suffix (.com, etc), this WILL fail (currently without error)
        dom.SOURCE,

    ]