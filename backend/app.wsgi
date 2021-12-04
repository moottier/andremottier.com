# apache wsgi configuration
import sys
import os
import logging

logging.basicConfig(stream=sys.stderr)

# assumes dev app located in directory with 'dev' in path
# also assumes we'll never have another non-dev environment with 'dev' in path name for app dir 
if __file__.find('dev') > -1:
    sys.path.insert(0,"/var/www/dev.andremottier.com/")
else:
    sys.path.insert(0,"/var/www/andremottier.com/")

from backend import create_app 
application = create_app()
