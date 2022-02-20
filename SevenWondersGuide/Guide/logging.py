import logging
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '%(asctime)s [%(module)s:%(funcName)s:%(lineno)d] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    }
}

def logging_setup():
    logging.config.dictConfig(LOGGING)
