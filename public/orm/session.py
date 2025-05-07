from sqlalchemy.orm import sessionmaker
from public.orm.sql_engine import SQLEngine

engine = SQLEngine()
Session = sessionmaker(bind=engine.get_engine())
session = Session()
