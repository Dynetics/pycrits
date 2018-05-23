import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsEmail as ema

class Email(Common):
    '''
    
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'emails/'

    _fields = [
        ema.ID,
        ema.ACTIONS,
        ema.BUCKET_LIST,
        ema.CAMPAIGN,
        ema.CC,
        ema.CREATED,
        ema.DATE,
        ema.FROM,
        ema.HELO,
        ema.ISODATE,
        ema.LOCATIONS,
        ema.MESSAGE_ID,
        ema.MODIFIED,
        ema.OBJECTS,
        ema.ORIGINATING_IP,
        ema.RAW_BODY,
        ema.RAW_HEADERS,
        ema.RELATIONSHIPS,
        ema.RELEASABILITY,
        ema.REPLY_TO,
        ema.SCHEMA_VERSION,
        ema.SCREENSHOTS,
        ema.SECTORS,
        ema.SENDER,
        ema.SOURCE,
        ema.STATUS,
        ema.SUBJECT,
        ema.TICKETS,
        ema.TO,
        ema.UNSUPPORTED_ATTRS,
        ema.X_MAILER,
        ema.X_ORIGINATING_IP,

        # POST-Specific fields
        ema.UPLOAD_TYPE,
        ema.FILEDATA,
        ema.EMAIL_ID,
        ema.PASSWORD,
        ema.DATE,
        ema.FROM_ADDRESS,
        ema.RAW_HEADER,
        ]

    # Fields that are REQUIRED to be provided by the user
    # when creating a new object of type EMAIL
    # This is odd because a name or any info bout the email
    # isnt actually required...
    _default_fields = [
        ema.SOURCE,
        ema.DATE,
    ]