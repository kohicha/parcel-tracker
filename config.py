# Local settings
import os
DEBUG = False
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'tracker')
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN')
