import sys

from sqlalchemy import Column, ForeignKey,Integer,String,DateTime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

import datetime

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	name = Column(String(80), nullable = False)
	email = Column(String(80), nullable = False)
	picture = Column(String(250))
	id = Column(Integer,primary_key=True)

class Category(Base):
	__tablename__ = 'category'
	name = Column(String(80), nullable = False)
	id = Column(Integer,primary_key=True)
	user_id = Column(Integer,ForeignKey('user.id'))
	category = relationship(User)

class Item(Base):
	__tablename__ = 'item'
	id = Column(Integer,primary_key=True)
	title = Column(String(250))
	description = Column(String(25000))
	created_date = Column(DateTime, default=datetime.datetime.utcnow())
	updated_date = Column(DateTime, default=datetime.datetime.utcnow())
	user_id = Column(Integer,ForeignKey('user.id'))
	category = relationship(User)

engine = create_engine('sqlite:///restaurantmenup.db')

Base.metadata.create_all(engine)