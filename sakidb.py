# -*- coding: utf-8 -*-

from sqlalchemy import *
from sqlalchemy.dialects.mysql import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
import datetime

dbase = declarative_base()


class data(dbase):
    __tablename__ = 'data'
    probe_number = Column(INTEGER(), primary_key=True, nullable=False)
    temperature = Column(FLOAT(), primary_key=False, nullable=False)
    timestamp = Column(TIMESTAMP(), primary_key=True, nullable=False, default=text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    def __init__(self, probe_number, temperature):
        self.probe_number = probe_number
        self.temperature = temperature
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return "<date(%d, %3.2f, %s)>" % (self.probe_number, self.temperature, str(self.timestamp)) 


Index(u'probe_number', data.probe_number, unique=False)


