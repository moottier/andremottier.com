# apache wsgi configuration
import sys
import os
import logging

logging.basicConfig(stream=sys.stderr)

# assumes app located in directory with 'dev' in path
# also assumes we'll never have another non-dev environment with 'dev' in path name for app dir 
print("***CWD PATH: ", os.getcwd(), file=sys.stdout)
if os.getcwd().find('dev') > -1:
    sys.path.insert(0,"/var/www/dev.andremottier.com/")
else:
    sys.path.insert(0,"/var/www/andremottier.com/")

from backend import create_app 
application = create_app()
