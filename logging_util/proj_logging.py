""" This module provides root logging configuration """

import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'level': logging.DEBUG,
    'formatters':{
        'standard': {
            'format': '%(asctime)s %(name)s [%(levelname)s]\t%(message)s',
        },
    },
    'handlers':{
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'debug_haveibeenpawned_file_handler': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'C:\\Users\\akabhati\\Documents\\haveibeenpawned_parent\\log.txt',
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10
        },   
    },
    'loggers': {
        '': { # root logger
            'handlers': ['default', 'debug_haveibeenpawned_file_handler'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
})