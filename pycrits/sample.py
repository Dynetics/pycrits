import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsSample as sam

class Sample(Common):
    '''

    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'samples/'

    _fields = [
        sam.ID,
        sam.ACTIONS,
        sam.BUCKET_LIST,
        sam.CAMPAIGN,
        sam.CREATED,
        sam.FILEDATA,
        sam.FILENAME,
        sam.FILESNAMES,
        sam.LOCATIONS,
        sam.MD5,
        sam.SHA1,
        sam.SHA256,
        sam.SIZE,
        sam.MIMETYPE,
        sam.FILE_FORMAT,
        sam.PASSWORD,
        sam.MODIFIED,
        sam.OBJECTS,
        sam.RELATIONSHIPS,
        sam.RELEASABILITY,
        sam.SCHEMA_VERSION,
        sam.SCREENSHOTS,
        sam.SECTORS,
        sam.SHA1,
        sam.SHA256,
        sam.SIZE,
        sam.SOURCE,
        sam.STATUS,
        sam.SSDEEP,
        sam.TICKETS,

        # Exclusively Post Params
        sam.RELATED_MD5,
        sam.RELATED_ID,
        sam.RELATED_TYPE,
        sam.UPLOAD_TYPE,
        ]

    # For POSTING data to crits (ex .new()):
    # So adding samples can be a little strange. Below is some clarification on the required fields:
    # If UPLOAD_TYPE is 'file', a file must be specified in the call to .new along with the requireds below
    # If UPLOAD_TYPE is 'metadata', a MD5 hash must be specified in params along with the requireds below
    # These checks aren't done by us, so nothing prevents the user from messing this up big time. The
    # web api will return a pretty specific error for the user, though. This is something to look at 
    # in the future. 
    _default_fields = [
        sam.SOURCE,
        sam.UPLOAD_TYPE,  #Must be either 'file' or 'metadata' but not currently checked by us
    ]