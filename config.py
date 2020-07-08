#!/usr/bin/env python3

import os, logging, sys, redis

# base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))

# setting root log format and level
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Config(object):
    SECRET_KEY = os.environ.get('APPLICATION_SECRET') or b'\xbd1\x7f&d5\xcf\x1f\x94\x13\x18Q\x05\x14\xb4\xfa'
    
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
  
    MONGODB_SETTINGS = { 
        'db' : os.environ.get('MONGODB_DATABASE_NAME')
    }

    # redis config
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
    SESSION_KEY_PREFIX = os.environ.get('SESSION_KEY_PREFIX')
    
    if os.environ.get('REDIS_HOST'):
        SESSION_REDIS = redis.StrictRedis(
                host=os.environ.get('REDIS_HOST'), 
                port=os.environ.get('REDIS_PORT'), 
                db=os.environ.get('REDIS_DB'), 
                password=os.environ.get('REDIS_PASSWORD')
            )