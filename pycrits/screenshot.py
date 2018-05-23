import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsScreenshot as scr

class Screenshot(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'screenshots/'

    _fields = [

        scr.ID,
        scr.ANALYST,
        scr.CREATED,
        scr.FILENAME,
        scr.HEIGHT,
        scr.MD5,
        scr.MODIFIED,
        scr.SCHEMA_VERSION,
        scr.SCREENSHOT,
        scr.SOURCE,
        scr.TAGS,
        scr.THUMB,
        scr.WIDTH,

        # Exclusively Post Params
        scr.UPLOAD_TYPE,
        scr.SCREENSHOT_IDS,
        scr.OID,
        scr.OTYPE,
        scr.DESCRIPTION,
    ]


    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type Screenshot
    _default_fields = [
        scr.UPLOAD_TYPE,
        scr.SOURCE,
        scr.OID,
        scr.OTYPE,
        # Also requires either SCREENSHOT_IDS or a file upload but not checked by us
    ]