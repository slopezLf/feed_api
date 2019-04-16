from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

__all__ = [
    'Base',
	'db_session',
	'init_db',
]

engine = create_engine('mysql+pymysql://root:password@localhost/feed_api')
db_session = scoped_session(sessionmaker(
    autoflush=True, bind=engine, expire_on_commit=False))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	from .post import Post
	Base.metadata.create_all(bind=engine)
