import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import configs
from database.base import Base
from database.models import *

engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
