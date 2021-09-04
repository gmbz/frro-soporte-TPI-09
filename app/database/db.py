from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..models.models import Base

engine = create_engine('sqlite:///app/database/tpidatabase2.db', connect_args={'check_same_thread': False}, convert_unicode=True)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

try:
    Base.metadata.create_all(engine)
except:
    pass
