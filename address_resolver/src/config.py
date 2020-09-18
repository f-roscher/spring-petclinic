import os


class Config(object):
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL','localhost:9200')
    ELASTICSEARCH_USER = os.getenv('ELASTICSEARCH_USER','elastic')
    ELASTICSEARCH_PASSWORD = os.getenv('ELASTICSEARCH_PASSWORD', 'changeme')
    ELASTICSEARCH_VALIDATE_CERTS = os.getenv('ELASTICSEARCH_VALIDATE_CERTS', 'false')
    ADDRESSES_PER_PAGE=int(os.getenv('ADDRESSES_PER_PAGE','25'))
    ADDRESS_INDEX = os.getenv('ADDRESS_INDEX','address')
    ELASTIC_APM = {
        'SERVICE_NAME': os.getenv('ELASTIC_APM_SERVICE_NAME','address-finder'),
        'SERVER_URL': os.getenv('ELASTIC_APM_SERVER_URL','http://localhost:8200'),
        'SERVICE_VERSION': os.getenv('ELASTIC_APM_SERVER_URL','1.0'),
        'COLLECT_LOCAL_VARIABLES': os.getenv('ELASTIC_APM_COLLECT_LOCAL_VARIABLES','all'),
        'SOURCE_LINES_ERROR_APP_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_ERROR_APP_FRAMES','10'),
        'SOURCE_LINES_ERROR_LIBRARY_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_ERROR_LIBRARY_FRAMES','10'),
        'SOURCE_LINES_SPAN_APP_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_SPAN_APP_FRAMES','5'),
        'SOURCE_LINES_SPAN_LIBRARY_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_SPAN_LIBRARY_FRAMES','5'),
        'CAPTURE_BODY': os.getenv('ELASTIC_APM_CAPTURE_BODY','all'),
        'SPAN_FRAMES_MIN_DURATION': os.getenv('ELASTIC_APM_SPAN_FRAMES_MIN_DURATION','-1'),
        'TRANSACTION_SAMPLE_RATE': os.getenv('ELASTIC_APM_TRANSACTION_SAMPLE_RATE','1.0'),
        'DEBUG': os.getenv('ELASTIC_APM_DEBUG', False)
    }
