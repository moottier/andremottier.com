# apache wsgi configuration
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/andremottier.com/")

from backend import create_app 
application = create_app()

from backend import config
