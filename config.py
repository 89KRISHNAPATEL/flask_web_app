import os

class config(object):
     SECRET_KEY = os.environ.get('SELECT_KEY') or "select_string"

     MONGODB_SETTINGS={ 'db':'UTA_Enrollment' }