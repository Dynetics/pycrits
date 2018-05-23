import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc



from .vocabulary import CRITsActor as a

class Actor(Common):
	'''
	'''

	_URL = get_api_url() + '/' + c.API + c.VERSION + 'actors/'

	_fields = [
		a.ID,
		a.ACTIONS,
		a.ALIASES,
		a.BUCKET_LIST,
		a.CAMPAIGN,
		a.CREATED,
		a.DESCRIPTION,
		a.IDENTIFIERS,
		a.INTENDED_EFFECTS,
		a.LOCATIONS,
		a.MODIFIED,
		a.MOTIVATIONS,
		a.NAME,
		a.OBJECTS,
		a.RELATIONSHIPS,
		a.RELEASIBILITY,
		a.SCHEMA_VERSION,
		a.SCREENSHOTS,
		a.SECTORS,
		a.SOPHISTICATIONS,
		a.SOURCE,
		a.STATUS,
		a.THREAT_TYPES,
		a.TICKETS,	

	    #POST-Specific fields
   		a.IDENTIFIER_TYPE,
    	a.IDENTIFIER,	
	]

	# Fields that are REQUIRED to be provided by the user
	# when creating a new object of type ACTOR
	_default_fields = [
		a.NAME,
		a.SOURCE,
	]






from .vocabulary import CRITsActorIdentifier as actid
class ActorIdentifier(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'actoridentifiers/'

    _fields = [
        actid.IDENTIFIER_TYPE,
        actid.IDENTIFIER,
        actid.SOURCE,
        actid.REFERENCE,
        actid.METHOD,
        actid.REFERENCE,
        actid.TLP,
        ]


    _default_fields = [
        actid.IDENTIFIER_TYPE,
        actid.IDENTIFIER,
        actid.SOURCE,
    ]