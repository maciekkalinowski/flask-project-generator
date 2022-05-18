from os.path import exists
from flask import render_template
from .DB import createDB
from app import app
import os


### CONFIG ##################################################
#

apiBasePath = '/api/app/v1'
basePath = '/app/v1'

PORT = os.getenv("PORT") or '5000'
PROTOCOL = os.getenv("PROTOCOL") or 'http'
HOST = os.getenv("HOST") or 'localhost'
API_URL = PROTOCOL + '://' + HOST + ':' + PORT + apiBasePath
WEB_URL = PROTOCOL + '://' + HOST + ':' + PORT + basePath
print('API: ' + API_URL)
print('WEB: ' + WEB_URL)
print('WELCOME: ' + WEB_URL + '/test')


dataBaseFile = 'DB.sqlite'



if not exists(dataBaseFile):
#if not os.path.isfile('PyDB.sqlite'):
    print ("Can't find database PyDB, creating one")
    createDB()
    print('Done')
else:
    print('Found a database: ' + dataBaseFile)

#
### CONFIG ##################################################


### TST ##################################################
#
@app.route(basePath + "/test")
def test():
    return render_template('test.html')

#
### TST ##################################################
