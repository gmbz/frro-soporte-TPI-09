from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..models.models import Base

engine = create_engine('sqlite:///app/database/tpidatabase.db',
                       connect_args={'check_same_thread': False},
                       convert_unicode=True)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()

Base.metadata.create_all(engine)
