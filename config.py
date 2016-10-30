
import os
import pymysql

SRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:gwyshine1996@localhost/flaskblog"


