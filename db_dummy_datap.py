from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setupp import Base, Category, Item
import time
engine = create_engine('sqlite:///restaurantmenup.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session  = DBSession()
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(10):
       c = Category(name=a[i])
       session.add(c)
       session.commit()
       time.sleep(0.5)
       for j in range(5):
              it = Item(title=a[i]*3,description=(a[i]+str(i))*10,category_id=i+1)
              session.add(it)
              session.commit()
              time.sleep(0.1)