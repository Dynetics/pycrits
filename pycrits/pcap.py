import urlparse

from .common import Common
from .access_token import get_access_token,get_api_url
from .vocabulary import CRITs as c
from .vocabulary import CRITsCommon as cc
from .vocabulary import CRITsPCAP as pca

class PCAP(Common):
    '''
    '''

    _URL = get_api_url() + '/' + c.API + c.VERSION + 'pcaps/'

    _fields = [
        pca.ID,
        pca.ACTIONS,
        pca.BUCKET_LIST,
        pca.CAMPAIGN,
        pca.CONTENTTYPE,
        pca.CREATED,
        pca.DESCRIPTION,
        pca.FILEDATA,
        pca.FILENAME,
        pca.LENGTH,
        pca.LOCATIONS,
        pca.MD5,
        pca.MODIFIED,
        pca.OBJECTS,
        pca.RELATIONSHIPS,
        pca.RELEASABILITY,
        pca.SCHEMA_VERSION,
        pca.SCREENSHOTS,
        pca.SECTORS,
        pca.SOURCE,
        pca.STATUS,
        pca.TICKETS,

        # Exclusively Post Params
        pca.RELATED_ID,
        pca.RELATED_MD5,
        pca.RELATED_TYPE,
        pca.RELATIONSHIP,
        ]

    _default_fields = [
        pca.SOURCE,

    ]