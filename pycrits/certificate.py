import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsCertificate as cer

class Certificate(Common):
    '''     
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'certificates/'

    _fields = [
        cer.ID,
        cer.ACTIONS,
        cer.BUCKET_LIST,
        cer.CAMPAIGN,
        cer.CREATED,
        cer.DESCRIPTION,
        cer.FILEDATA,
        cer.FILENAME,
        cer.FILETYPE,
        cer.LOCATIONS,
        cer.MD5,
        cer.MODIFIED,
        cer.OBJECTS,
        cer.RELATIONSHIPS,
        cer.RELEASABILITY,
        cer.SCHEMA_VERSION,
        cer.SCREENSHOTS,
        cer.SECTORS,
        cer.SIZE,
        cer.SOURCE,
        cer.STATUS,
        cer.TICKETS,


        # POST-Specific fields
        cer.RELATED_ID,
        cer.RELATED_MD5,
        cer.RELATED_TYPE,
        cer.RELATIONSHIP,
        ]

    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type CAMPAIGN
    _default_fields = [
        cer.SOURCE,
    ]