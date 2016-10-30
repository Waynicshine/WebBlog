from app.models import Category,Post,Comment

from app import db

# java = Category('Java')
# python = Category('Python')
#
# db.session.add(java)
# db.session.add(python)
#
#
# doge=Post(1,'2016-10-24','doge','waynic',1,1,'2016-10-24')
# db.session.add(doge)
comment=Comment(1,'Waynic','So cool',1)

db.session.commit()
