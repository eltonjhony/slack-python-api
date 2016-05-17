import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/nskslackapi/")
 
from FlaskApp import app as application
application.secret_key = 'nskslackapi'
