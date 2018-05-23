import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsRaw as raw

class Raw(Common):
    '''
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'raw_data/'

    _fields = [
        raw.ID,
        raw.ACTIONS,
        raw.BUCKET_LIST,
        raw.CAMPAIGN,
        raw.CREATED,
        raw.DATA,
        raw.DATA_TYPE,
        raw.DESCRIPTION,
        raw.HIGHLIGHTS,
        raw.INLINES,
        raw.LINK_ID,
        raw.LOCATIONS,
        raw.MD5,
        raw.MODIFIED,
        raw.OBJECTS,
        raw.RELATIONSHIPS,
        raw.RELEASABILITY,
        raw.SCHEMA_VERSION,
        raw.SCREENSHOTS,
        raw.SECTORS,
        raw.SOURCE,
        raw.STATUS,
        raw.TICKETS,
        raw.TITLE,
        raw.TOOL,
        raw.VERSION,

        # Exclusively Post Params
        raw.UPLOAD_TYPE,   # Must be metadata or file
        raw.COPY_RELATIONSHIPS,
        raw.TOOL_DETAILS,
        raw.TOOL_NAME,
        raw.TOOL_VERSION,
        ]

    # For POSTING data to crits (ex .new()):
    # If UPLOAD_TYPE is 'file', a file must be specified in the call to .new along with the requireds below
    # If UPLOAD_TYPE is 'metadata', data must be specified
    # These checks aren't done by us, so nothing prevents the user from messing this up big time. The
    # web api will return a pretty specific error for the user, though. This is something to look at 
    # in the future. 
    _default_fields = [
        raw.SOURCE,
        raw.UPLOAD_TYPE,
        raw.DATA_TYPE, #<--------- one of json or text
        raw.TITLE,
        # raw.DATA <------ only required if upload type is metadata
    ]