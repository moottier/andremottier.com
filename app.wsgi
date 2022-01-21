# apache wsgi configuration
import sys
import os
import logging

logging.basicConfig(stream=sys.stderr)

# assumes dev app located in directory with 'dev' in path
# also assumes we'll never have another non-dev environment with 'dev' in path name for app dir 
if __file__.find('dev') > -1:
    sys.path.insert(0,"/var/www/dev.andremottier.com/")
    from andremottier.config import DevelopmentConfig as Config
else:
    sys.path.insert(0,"/var/www/andremottier.com/")
    from andremottier.config import ProductionConfig as Config

from andremottier import create_app
application = create_app(Config())
