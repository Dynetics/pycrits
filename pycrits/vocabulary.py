class CRITs:

    API = 'api/'
    VERSION = 'v1/'
    DEFAULT_LIMIT = 20

    META = 'meta'
    OBJECTS = 'objects'



class CRITsAccessToken:
    # Environment Variables for init()
    CRITS_ACCESS_TOKEN = 'CRITS_ACCESS_TOKEN'
    CRITS_API_URL = 'CRITS_API_URL'
    CRITS_USER_ID = 'CRITS_USER_ID'
    CRITS_API_KEY = 'CRITS_API_KEY'


class MongoOperators:
    """
    These operators can be used to adjust a query as such:
    queryparams = {'CRITsRaw.VERSION' + 'MongoOperators.LTE' : '1.0'}
    """
    GT = '__gt'
    GTE = '__gte'
    LT = '__lt'
    LTE = '__lte'
    IN = '__in'
    NIN = '__nin'


'''
Below are definitions for the different types of records
found in CRITs.
'''
class CRITsCommon(object):
    '''
    Fields common to all TLOs
    '''
    ID = '_id'
    ACTIONS = 'actions'
    BUCKET_LIST = 'bucket_list'
    CAMPAIGN = 'campaign'
    CREATED = 'created'
    LOCATIONS = 'locations'
    MODIFIED = 'modified'
    OBJECTS = 'objects'
    RELATIONSHIPS = 'relationships'
    SCHEMA_VERSION = 'schema_version'
    SCREENSHOTS = 'screenshots'
    SECTORS = 'sectors'
    STATUS = 'status'
    TICKETS = 'tickets'

class CRITsPatchCommon(object):
    '''
    PATCH fields common to all TLOs
    '''
    ACTION_ADD = 'action_add'
    ACTION_UPDATE = 'action_update'
    ACTION_REMOVE = 'action_remove'
    ADD_OBJECT = 'add_object'
    ADD_RELEASABILITY = 'add_releasability'
    DESCRIPTION_UPDATE = 'description_update'
    FORGE_RELATIONSHIP = 'forge_relationship'
    RUN_SERVICE = 'run_service'
    SOURCE_ADD_UPDATE = 'source_add_update'
    SOURCE_REMOVE = 'source_remove'
    STATUS_UPDATE = 'status_update'
    TICKET_ADD = 'ticket_add'
    TICKET_UPDATE = 'ticket_update'
    TICKET_REMOVE = 'ticket_remove'


class CRITsActor(CRITsCommon, CRITsPatchCommon):
    ALIASES = 'aliases'
    DESCRIPTION = 'description'
    IDENTIFIERS = 'identifiers'
    INTENDED_EFFECTS = 'intended_effects'
    MOTIVATIONS = 'motivations'
    NAME = 'name'
    RELEASIBILITY = 'releasability'
    SOPHISTICATIONS = 'sophistications'
    SOURCE = 'source'
    THREAT_TYPES = 'threat_types'

    # Unique POST Parameters:
    IDENTIFIER_TYPE = 'identifier_type'
    IDENTIFIER = 'identifier'

    # Unique Patch Actions
    UPDATE_ACTOR_TAGS = 'update_actor_tags'
    ATTRIBUTE_ACTOR_IDENTIFIER = 'attribute_actor_identifier'
    SET_IDENTIFIER_CONFIDENCE = 'set_identifier_confidence'
    REMOVE_ATTRIBUTION = 'remove_attribution'
    SET_ACTOR_NAME = 'set_actor_name'
    UPDATE_ACTOR_NAME = 'update_actor_name'




## This does not follow the typical pattern (Not a TLO)
## Calling non-TLO's via the API will soon be deprecated
class CRITsActorIdentifier:

    IDENTIFIER_TYPE = 'identifier_type'
    IDENTIFIER = 'identifier'
    SOURCE = 'source'
    REFERENCE = 'reference'
    METHOD = 'method'
    REFERENCE = 'reference'
    TLP = 'tlp'


class CRITsBackdoor(CRITsCommon, CRITsPatchCommon):
    
    ALIASES = 'aliases'
    NAME = 'name'
    RELEASABILITY = 'releasability'
    SOURCE = 'source'
    VERSION = 'version'
    DESCRIPTION = 'description'

    # Unique POST Parameters:
    # NONE

    # Unique Patch Actions:
    # NONE


class CRITsCampaign(CRITsCommon, CRITsPatchCommon):
    
    ACTIVE = 'active'
    ACTOR_COUNT = 'actor_count'
    ALIASES = 'aliases'
    BACKDOOR_COUNT = 'backdoor_count'
    DESCRIPTION = 'description'
    DOMAIN_COUNT = 'domain_count'
    EMAIL_COUNT = 'email_count'
    EVENT_COUNT = 'event_count'
    EXPLOIT_COUNT = 'exploit_count'
    INDICATOR_COUNT = 'indicator_count'
    IP_COUNT = 'ip_count'
    NAME = 'name'
    PCAP_COUNT = 'pcap_count'
    RELEASABILITY = 'releasability'
    SAMPLE_COUNT = 'sample_count'
    TTPS = 'ttps'

    # Unique POST Parameters:
    # NONE

    # Unique Patch Actions:
    # NONE

class CRITsCertificate(CRITsCommon, CRITsPatchCommon):
    DESCRIPTION = 'description'
    FILEDATA = 'filedata'
    FILENAME = 'filename'
    FILETYPE = 'filetype'
    MD5 = 'md5'
    RELEASABILITY = 'releasability'
    SIZE = 'size'
    SOURCE = 'source'


    # Unique POST Parameters:
    RELATED_ID = 'related_id'
    RELATED_MD5 = 'related_md5'
    RELATED_TYPE = 'related_type'
    RELATIONSHIP = 'relationship'

    # Unique Patch Actions:
    # NONE



## This can only be called via POST
## This does not follow the typical pattern (Not a TLO)
## Calling non-TLO's via the API will soon be deprecated
class CRITsComment:

    COMMENT = 'comment'
    OBJECT_ID = 'object_id'
    OBJECT_TYPE = 'object_type'


class CRITsDomain(CRITsCommon, CRITsPatchCommon):

    ANALYST = 'analyst'
    DOMAIN = 'domain' # If this does not have a url suffix (.com, etc), this WILL fail (currently without error)
    RELEASABILITY = 'releasability'
    SOURCE = 'source'
    TYPE = 'type'
    WATCHLISTENABLED = 'watchlistEnabled' 

    # Unique POST Parameters:
    ADD_INDICATORS = 'add_indcators'
    ADD_IP = 'add_ip'
    IP_TYPE = 'ip_type'
    IP_SOURCE = 'ip_source'
    IP_METHOD = 'ip_method'
    IP_REFERENCE ='ip_reference'
    SAME_SOURCE  = 'same_source'

    # Unique Patch Actions:
    # NONE


class CRITsEmail(CRITsCommon, CRITsPatchCommon):

    BOUNDARY = 'boundary'
    CC = 'cc'
    DATE = 'date'
    FROM = 'from'
    HELO = 'helo'
    ISODATE = 'isodate'
    MESSAGE_ID = 'message_id'
    ORIGINATING_IP = 'originating_ip'
    RAW_BODY = 'raw_body'
    RAW_HEADERS = 'raw_headers'
    RELEASABILITY = 'releasability'
    REPLY_TO = 'reply_to'
    SENDER = 'sender'
    SOURCE = 'source'
    SUBJECT = 'subject'
    TO = 'to'
    UNSUPPORTED_ATTRS = 'unsupported_attrs'
    X_MAILER = 'x_mailer'
    X_ORIGINATING_IP = 'x_originating_ip'

    # Unique POST Parameters:
    UPLOAD_TYPE = 'upload_type'
    FILEDATA = 'filedata'
    EMAIL_ID = 'email_id'
    PASSWORD = 'password'
    DATE = 'date'
    FROM_ADDRESS = 'from_address'
    RAW_HEADER = 'raw_header'

    # Unique Patch Actions:
    # NONE


class CRITsEvent(CRITsCommon, CRITsPatchCommon):

    DESCRIPTION = 'description'
    EVENT_ID = 'event_id'
    EVENT_TYPE = 'event_type' # Must be one of the types detailed in UI selection 
    RELEASABILITY = 'releasability'
    SOURCE = 'source'
    TITLE = 'title' 
    
    # Unique POST Parameters:
    DATE = 'date'

    # Unique Patch Actions:
    # NONE


class CRITsExploit(CRITsCommon, CRITsPatchCommon):

    CVE = 'cve'
    DESCRIPTION = 'description'
    NAME = 'name'
    RELEASABILITY = 'releasability'
    SOURCE = 'source'

    # Unique POST Parameters:
    # NONE

    # Unique Patch Actions:
    # NONE



class CRITsIndicator(CRITsCommon, CRITsPatchCommon):

    ACTIVITY = 'activity'
    ATTACK_TYPES = 'attack_types'
    DESCRIPTION = 'description'
    IMPACT = 'impact'
    LOWER = 'lower'
    RELEASABILITY = 'releasability'
    SOURCE = 'source'
    THREAT_TYPES = 'threat_types'
    TYPE = 'type'
    UNSUPPORTED_ATTRS = 'unsupported_attrs'
    VALUE = 'value' 

    # Unique POST Parameters:
    ADD_DOMAIN = 'add_domain'
    ADD_RELATIONSHIP = 'add_relationship'  
    INDICATOR_CONFIDENCE = 'indicator_confidence'
    INDICATOR_IMPACT = 'indicator_impact'
    THREAT_TYPE = 'threat_type' #not threats type
    ATTACK_TYPE = 'attack_type' #not attacks type


    # Unique Patch Actions:
    ACTIVTY_ADD = 'activity_add'
    ACTIVITY_REMOVE = 'activity_remove'
    ACTIVITY_UPDATE = 'activity_update'
    CI_UPDATE = 'ci_update'
    SET_INDICATOR_ATTACK_TYPE = 'set_indicator_attack_type'
    SET_INDICATOR_THREAT_TYPE = 'set_indicator_threat_type'


class CRITsIP(CRITsCommon, CRITsPatchCommon):
    
    DESCRIPTION = 'description'
    IP = 'ip' 
    RELEASABILITY = 'releasability'
    SOURCE = 'source'
    TYPE = 'type'

    # Unique POST Parameters:
    ADD_INDICATOR = 'add_indicator'
    INDICATOR_REFERENCE = 'indicator_reference'
    IP_TYPE = 'ip_type' #Must be one of the types outline in the gui

    # Unique Patch Actions:
    # NONE



class CRITsPCAP(CRITsCommon, CRITsPatchCommon):

    CONTENTTYPE = 'contentType'  #Odd that this cointains a capital letter
    DESCRIPTION = 'description'
    FILEDATA = 'filedata'
    FILENAME = 'filename'
    LENGTH = 'length'
    MD5 = 'md5'
    RELEASABILITY = 'releasability'
    SOURCE = 'source'

    # Unique POST Parameters:
    RELATED_ID = 'related_id'
    RELATED_MD5 = 'related_md5'
    RELATED_TYPE = 'related_type'
    RELATIONSHIP = 'relationship'

    # Unique Patch Actions:
    # NONE


class CRITsRaw(CRITsCommon, CRITsPatchCommon):

    DATA = 'data'
    DATA_TYPE = 'data_type'
    DESCRIPTION = 'description'
    HIGHLIGHTS = 'highlights'
    INLINES = 'inlines'
    LINK_ID = 'link_id'
    MD5 = 'md5'
    RELEASABILITY = 'releasability'
    SOURCE = 'source'
    TITLE = 'title'
    TOOL = 'tool'
    VERSION = 'version'

    # Unique POST Parameters:
    UPLOAD_TYPE = 'upload_type'  ## Must be metadata or file This is NOT checked by us
    COPY_RELATIONSHIPS = 'copy_relationships'
    TOOL_DETAILS = 'tool_details'
    TOOL_NAME = 'tool_name'
    TOOL_VERSION = 'tool_version'

    # Unique Patch Actions:
    # NONE


class CRITsSample(CRITsCommon, CRITsPatchCommon):

    DESCRIPTION = 'description'
    FILEDATA = 'filedata'
    FILENAME = 'filename'
    FILESNAMES = 'filenames'
    MD5 = 'md5'
    SHA1 = 'sha1'
    SHA256 = 'sha256'
    SIZE = 'size'
    PASSWORD = 'password'
    FILE_FORMAT = 'file_format'
    MIMETYPE = 'mimetype'
    RELEASABILITY = 'releasability'
    SHA1 = 'sha1'
    SHA256 = 'sha256'
    SIZE = 'size'
    SOURCE = 'source'
    SSDEEP = 'ssdeep'

    # Unique POST Parameters:
    UPLOAD_TYPE = 'upload_type'   ## Must be metadata or file This is NOT checked by us
    RELATED_MD5 = 'related_md5'
    RELATED_ID = 'related_id'
    RELATED_TYPE = 'related_type'

    # Unique Patch Actions:
    # NONE



## This can only be called via POST
## This does not follow the typical pattern (Not a TLO)
## Calling non-TLO's via the API will soon be deprecated
class CRITsScreenshot():
    
    ID = '_id'
    ANALYST = 'analyst'
    CREATED = 'created'
    DESCRIPTION = 'description'
    FILENAME = 'filename'
    HEIGHT = 'height'
    MD5 = 'md5'
    MODIFIED ='modified'
    SCHEMA_VERSION = 'schema_version'
    SCREENSHOT = 'screenshot'
    SOURCE = 'source'
    TAGS = 'tags'
    THUMB = 'thumb'
    WIDTH = 'width'

    # Unique POST Parameters:
    UPLOAD_TYPE='upload_type' # One of 'ids' or 'screenshot'
    SCREENSHOT_IDS = 'screenshot_ids'
    OID = 'oid'
    OTYPE = 'otype'

    # Unique Patch Actions:
    # NONE

class CRITsSignature(CRITsCommon, CRITsPatchCommon):

    DATA = 'data'
    DATA_TYPE = 'data_type'
    DATA_TYPE_DEPENDENCY = 'data_type_dependency'
    DATA_TYPE_MAX_VERSION = 'data_type_max_version'
    DATA_TYPE_MIN_VERSION = 'data_type_min_version'
    DESCRIPTION = 'description'
    LINK_ID = 'link_id'
    MD5 = 'md5'
    RELEASABILITY = 'releasability'
    SCHEMA_VERSION = 'schema_version'
    SCREENSHOTS = 'screenshots'
    SOURCE = 'source'
    TITLE = 'title'
    VERSION = 'version'

    # Unique POST Parameters:
    COPY_RELATIONSHIPS = 'copy_relationships' #Requires Link ID


    # Unique Patch Actions:
    UPDATE_DEPENDENCY = 'update_dependency'
    UPDATE_MAX_VERSION = 'update_max_version'
    UPDATE_MIN_VERSION = 'update_min_version'
    UPDATE_SIGNATURE_DATA = 'update_signature_data'
    UPDATE_SIGNATURE_TYPE = 'update_signature_type'
    UPDATE_TITLE = 'update_title'



class CRITsTarget(CRITsCommon, CRITsPatchCommon):

    EMAIL_ADDRESS = 'email_address'
    EMAIL_COUNT = 'email_count'
    RELEASABILITY = 'releasability'
    SCREENSHOTS = 'screenshots'

    # Unique POST Parameters:
    FIRSTNAME = 'firstname'
    LASTNAME = 'lastname'
    DIVISION = 'division'
    DEPARTMENT ='department'
    ORGANIZATION_ID = 'organization_id'
    TITLE = 'title'
    NOTE = 'note'



# End CRITs record defs

class Response(object):

    """
    Vocabulary for describing server responses.
    """

    SUCCESS = 'success'
    ID = 'id'
    ERROR = 'error'
    MESSAGE = 'message'
    TYPE = 'type'
    CODE = 'code'
    FBTRACE_ID = 'fbtrace_id'


class Paging(object):

    '''
    Vocabulary for the fields available in a GET response specific to paging.
    '''

    LIMIT = 'limit'
    NEXT = 'next'
    OFFSET = 'offset'
    PREVIOUS = 'previous'
    TOTAL = 'total_count'



class CRITsVocabulary:
    '''
    Define vocabularly that is often referenced by fields in CRITs
    We don't currently use these for anything, however they are great
    to reference when wondering what value should be included for a
    specific field in POST requests. In the future, this should be
    leveraged for better error checking but its just here for now
    '''
    resources = [
        'actors',
        'actoridentifiers',
        'backdoors',
        'campaigns',
        'certificates',
        'comments',
        'domains',
        'emails',
        'events',
        'exploits',
        'indicators',
        'ips',
        'pcaps',
        'raw_data',
        'samples',
        'targets',
    ]

    types = [
        'Actor',
        'AnalysisResult',
        'Backdoor',
        'Campaign',
        'Certificate',
        'Comment',
        'Domain',
        'Email',
        'Event',
        'Exploit',
        'Indicator',
        'IP',
        'Notification',
        'PCAP',
        'RawData',
        'Sample',
        'Screenshot',
        'Signature',
        'Target',
    ]

    type_to_api = {
        'Actor':'actors',
        'Actor Identifier':'actoridentifiers',
        'Backdoor':'backdoors',
        'Campaign':'campaigns',
        'Certificate':'certificates',
        'Comment':'comments',
        'Domain':'domains',
        'Email':'emails',
        'Event':'events',
        'Exploit':'exploits',
        'Indicator':'indicators',
        'Indicator Activity':'indicator_activity',
        'IP':'ips','PCAP':'pcaps',
        'Raw Data':'raw_data',
        'Sample':'samples',
        'Screenshot':'screenshots',
        'Service':'services',
        'Signature':'signatures',
        'Target':'targets',
    }

    relationships = [
        'Compressed From',
        'Compressed Into',
        'Connected From',
        'Connected To',
        'Contains',
        'Contained Within',
        'Created',
        'Created By',
        'Decoded',
        'Decoded By',
        'Decrypted',
        'Decrypted By',
        'Downloaded',
        'Downloaded By',
        'Downloaded From',
        'Downloaded To',
        'Dropped',
        'Dropped By',
        'Installed',
        'Installed By',
        'Loaded From',
        'Loaded Into',
        'Packed From',
        'Packed Into',
        'Received From',
        'Sent To',
        'Registered',
        'Registered To',
        'Related To',
        'Resolved To',
        'Sent',
        'Sent By',
        'Sub-domain Of',
        'Supra-domain Of',
    ]

    confidence = [
        'unknown',
        'low',
        'medium',
        'high'
    ]

    ip_types = [
        'IPv4 Address',
        'IPv4 Subnet',
        'IPv6 Address',
        'IPv6 Subnet',
    ]

    email_upload_types = [
        'eml',
        'msg',
        'raw',
        'yaml',
        'fields',
    ]

    event_types = [
        'Application Compromise',
        'Denial of Service',
        'Distributed Denial of Service',
        'Exploitation',
        'Intel Sharing',
        'Malicious Code',
        'Phishing',
        'Privileged Account Compromise',
        'Scanning',
        'Sensor Alert',
        'Social Engineering',
        'Sniffing',
        'Spam',
        'Strategic Web Compromise',
        'Unauthorized Information Access',
        'Unknown',
        'Website Defacement',
    ]

    indicator_types = [
        'Adjust Token',
        'API Key',
        'AS Number',
        'AS Name',
        'Bank account',
        'Bitcoin account',
        'Certificate Fingerprint',
        'Certificate Name',
        'Checksum CRC16',
        'Command Line',
        'Company name',
        'Cookie Name',
        'Country',
        'CRX',
        'Debug Path',
        'Debug String',
        'Destination Port',
        'Device IO',
        'Document from URL',
        'Domain',
        'Email Boundary',
        'Email Address',
        'Email Address From',
        'Email HELO',
        'Email Message ID',
        'Email Originating IP',
        'Email Reply-To',
        'Email Address Sender',
        'Email Subject',
        'Email X-Mailer',
        'Email X-Originating IP',
        'File Created',
        'File Deleted',
        'File Moved',
        'File Name',
        'File Opened',
        'File Path',
        'File Read',
        'File Written',
        'GET Parameter',
        'HEX String',
        'HTML ID',
        'HTTP Request',
        'HTTP Response Code',
        'IMPHASH',
        'IPv4 Address',
        'IPv4 Subnet',
        'IPv6 Address',
        'IPv6 Subnet',
        'Latitude',
        'Launch Agent',
        'Location',
        'Longitude',
        'MAC Address',
        'Malware Name',
        'MD5',
        'Memory Alloc',
        'Memory Protect',
        'Memory Read',
        'Memory Written',
        'Mutant Created',
        'Mutex',
        'Name Server',
        'Other File Operation',
        'Password',
        'Password Salt',
        'Payload Data',
        'Payload Type',
        'Pipe',
        'POST Data',
        'Process Name',
        'Protocol',
        'Referer',
        'Referer of Referer',
        'Registrar',
        'Registry Key',
        'Registry Key Created',
        'Registry Key Deleted',
        'Registry Key Enumerated',
        'Registry Key Monitored',
        'Registry Key Opened',
        'Registry Key Value Created',
        'Registry Key Value Deleted',
        'Registry Key Value Modified',
        'Registry Key Value Queried',
        'Service Name',
        'SHA1',
        'SHA256',
        'SMS Origin',
        'Source Port',
        'SSDEEP',
        'Telephone',
        'Time Created',
        'Time Updated',
        'Tracking ID',
        'TS End',
        'TS Start',
        'URI',
        'User Agent',
        'User ID',
        'Victim IP',
        'Volume Queried',
        'Webstorage Key',
        'Web Payload',
        'WHOIS Name',
        'WHOIS Address 1',
        'WHOIS Address 2',
        'WHOIS Telephone',
        'XPI',
    ]

    indicator_threat_types = [
        'Bad Actor',
        'Compromised Credential',
        'Command Exec',
        'Malicious Ad',
        'Malicious Content',
        'Malicious Domain',
        'Malicious Inject',
        'Malicious IP',
        'Malicious URL',
        'Malicious URL Chunk',
        'Malware Artifacts',
        'Malware Sample',
        'Malware Victim',
        'Proxy IP',
        'Sinkhole Event',
        'SMS Spam',
        'Unknown',
        'Victim IP Usage',
        'Web Request',
        'Whitelist Domain',
        'Whitelist IP',
        'Whitelist URL',
    ]

    indicator_attack_types = [
        'Access Token Theft',
        'Brute Force',
        'Clickjacking',
        'Email Spam',
        'Fake Accounts',
        'IP Infringement',
        'Malicious App',
        'Malware',
        'Phishing',
        'Self XSS',
        'Share Baiting',
        'Targeted',
        'Unknown',
    ]

    indicator_confidence = [
        'unknown',
        'benign',
        'low',
        'medium',
        'high',
    ]

    indicator_status = [
        'New',
        'Analyzed',
        'Deprecated',
        'In Progress',
    ]

    raw_upload_types = [
        'metadata',
        'file',
    ]

    raw_data_types = [
        'JSON',
        'Text',
    ]

    sample_file_format = [
        'zip',
        'rar',
        'raw',
    ]