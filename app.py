from __future__ import unicode_literals       #UTF-8 encoded bytes
from flask import Flask                       #importing flask module
import os                                     #allows interfacing with the underlying operating system that Python is running on(Windows,Linux)


app = Flask(__name__)                      


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'              #location to store file from user 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.isdir(app.config['UPLOAD_FOLDER']):                                   #if not present create it
        os.mkdir(app.config['UPLOAD_FOLDER'])


DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'          #location to store output file
#DOWNLOAD_FOLDER = 'C:/down_loads'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

if not os.path.isdir(app.config['DOWNLOAD_FOLDER']):                                #if not present create it
        os.mkdir(app.config['DOWNLOAD_FOLDER'])


