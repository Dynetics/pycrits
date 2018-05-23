import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsIndicator as ind

class Indicator(Common):
    '''
    ***NOT YET WORKING FOR POSTS
    Having a hard time with required fields (some nested)
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'indicators/'

    _fields = [
        ind.ID,
        ind.ACTIONS,
        ind.ACTIVITY,
        ind.ATTACK_TYPES,
        ind.BUCKET_LIST,
        ind.CAMPAIGN,
        ind.CREATED,
        ind.DESCRIPTION,
        ind.IMPACT,
        ind.LOCATIONS,
        ind.LOWER,
        ind.MODIFIED,
        ind.OBJECTS,
        ind.RELATIONSHIPS,
        ind.RELEASABILITY,
        ind.SCHEMA_VERSION,
        ind.SCREENSHOTS,
        ind.SECTORS,
        ind.SOURCE,
        ind.STATUS,
        ind.THREAT_TYPES,
        ind.TICKETS,
        ind.TYPE,
        ind.UNSUPPORTED_ATTRS,
        ind.VALUE,

        # Exclusive post params
        ind.ADD_DOMAIN, 
        ind.ADD_RELATIONSHIP,
        ind.INDICATOR_CONFIDENCE,
        ind.INDICATOR_IMPACT,
        ind.THREAT_TYPE,
        ind.ATTACK_TYPE,
        ]
    
    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type INDICATOR
    _default_fields = [
        ind.SOURCE,
        ind.VALUE,  
        ind.TYPE,
    ]