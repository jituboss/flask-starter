import os

class Config(object):
    SECRET_KEY = os.environ.get('APPLICATION_SECRET') or b'\xbd1\x7f&d5\xcf\x1f\x94\x13\x18Q\x05\x14\xb4\xfa'
    
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
  
    MONGODB_SETTINGS = { 
        'db' : 'UTA_Enrollment' 
    }


    