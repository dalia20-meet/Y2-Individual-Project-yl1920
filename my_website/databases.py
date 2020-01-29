from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


# replace lecture.db with your own database file
engine = create_engine('sqlite:///databases.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))









 
def save_to_database(e,p):
	user = User(
		email=e,
		password=p)
	session.add(user)
	session.commit()

def queryAllUsers():
	return session.query(User).all()

def check(e,p):
	user=session.query(User).filter_by(email=e).first()
	if user != None:
		if user.password == p :
			c = True
		else:
			c = False
		return c
	else:
		return False	


# print(check)		