import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsCampaign as cam

class Campaign(Common):
	'''
	
	'''

	_URL = get_api_url() + '/' + c.API + c.VERSION + 'campaigns/'

	_fields = [
	    cam.ID,
	    cam.ACTIONS,
	    cam.ACTIVE,
	    cam.ACTOR_COUNT,
	    cam.ALIASES,
	    cam.BACKDOOR_COUNT,
	    cam.BUCKET_LIST,
	    cam.CAMPAIGN,
	    cam.CREATED,
	    cam.DESCRIPTION,
	    cam.DOMAIN_COUNT,
	    cam.EMAIL_COUNT,
	    cam.EVENT_COUNT,
	    cam.EXPLOIT_COUNT,
	    cam.INDICATOR_COUNT,
	    cam.IP_COUNT,
	    cam.LOCATIONS,
	    cam.MODIFIED,
	    cam.NAME,
	    cam.OBJECTS,
	    cam.PCAP_COUNT,
	    cam.RELATIONSHIPS,
	    cam.RELEASABILITY,
	    cam.SAMPLE_COUNT,
	    cam.SCHEMA_VERSION,
	    cam.SCREENSHOTS,
	    cam.SECTORS,
	    cam.STATUS,
	    cam.TICKETS,
	    cam.TTPS,
	]


	# Fields that are REQUIRED to be provided by the user
	# when creating a new object of type CAMPAIGN
	_default_fields = [
		cam.NAME,
	]