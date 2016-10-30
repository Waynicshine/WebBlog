#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db
from sqlalchemy.schema import CreateSchema
from app.models import User
import hashlib
db.engine.execute(CreateSchema('flaskblog'))
db.create_all()

admin = User('admin', '123456')
db.session.add(admin)
db.session.commit()

# create admin user
#
# m = hashlib.md5()
# line='123456'
# m.update(line)
# line.encode('utf-8')
#
# pwd = m.hexdigest()
#
# admin = User('admin', pwd)
# db.session.add(admin)
# db.session.commit()