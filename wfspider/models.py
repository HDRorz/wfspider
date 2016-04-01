# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String, DateTime, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


BaseModel = declarative_base()


def db_connect():

    return create_engine(URL(**settings.DATABASE))


def create_models(engine):

    BaseModel.metadata.create_all(engine)


class Periodical(BaseModel):

    __tablename__ = "periodical"

    guid = Column('GUID', String(50), primary_key=True)
    datasetid = Column('DatasetID', String(50), nullable=False)
    title = Column('Title', String(1000), nullable=False)
    author = Column('Author', String(1000), nullable=False)
    authoradd = Column('AuthorADD', String(2000), nullable=False)
    abstract = Column('Abstract', String(4000), nullable=False)
    keywords = Column('Keywords', String(2000), nullable=False)
    engtitle = Column('EngTitle', String(2000), nullable=True)
    engkeywords = Column('EngKeywords', String(2000), nullable=False)
    engabstract = Column('EngAbstract', String(4000), nullable=True)
    engauthor = Column('EngAuthor', String(1000), nullable=True)
    engauthoradd = Column('EngAuthorADD', String(2000), nullable=True)
    language = Column('language', String(50), nullable=False)
    issn = Column('ISSN', String(50), nullable=True)
    doi = Column('DOI', String(200), nullable=True)
    classification = Column('Classification', String(150), nullable=True)
    journalname = Column('JournalName', String(255), nullable=False)
    engjournalname = Column('EngjournalName', String(255), nullable=True)
    year = Column('Year', String(20), nullable=False)
    volume = Column('Volume', String(50), nullable=True)
    period = Column('period', String(20), nullable=True)
    page = Column('Page', String(255), nullable=True)
    lastmodified = Column('LastModified', TIMESTAMP)


class Thesis(BaseModel):

    __tablename__ = "Thesis"

    guid = Column('GUID', String(50), primary_key=True)
    datesetid = Column('DatasetID', String(50), nullable=False)
    title = Column('Title', String(1000), nullable=False)
    author = Column('Author', String(1000), nullable=False)
    abstract = Column('Abstract', String(4000), nullable=False)
    keywords = Column('Keywords', String(2000), nullable=False)
    engtitle = Column('EngTitle', String(2000), nullable=True)
    engkeywords = Column('EngKeywords', String(2000), nullable=False)
    engabstract = Column('EngAbstract', String(4000), nullable=True)
    classification = Column('Classification', String(150), nullable=True)
    degree = Column('Degree', String(20), nullable=False)
    major = Column('Major', String(200), nullable=False)
    subject = Column('Subject', String(200), nullable=False)
    university = Column('University', String(200), nullable=False)
    submitdate = Column('SubmitDate', String(20), nullable=False)
    quliaficationdate = Column('QuliaficationDate', String(20), nullable=True)
    supervisor = Column('Supervisor', String(20), nullable=False)
    supervisoraffiliation = Column('SupervisorAffiliation', String(255), nullable=False)
    language = Column('language', String(50), nullable=False)
    lastmodified = Column('LastModified', TIMESTAMP)


class Conference(BaseModel):

    __tablename__ = "Conference"

    guid = Column('GUID', String(50), primary_key=True)
    datesetid = Column('DatasetID', String(50), nullable=False)
    title = Column('Title', String(1000), nullable=False)
    author = Column('Author', String(1000), nullable=False)
    abstract = Column('Abstract', String(4000), nullable=False)
    keywords = Column('Keywords', String(2000), nullable=False)
    engauthor = Column('EngAuthor', String(1000), nullable=True)
    engauthoradd = Column('EngAuthorADD', String(2000), nullable=True)
    engtitle = Column('EngTitle', String(2000), nullable=True)
    engkeywords = Column('EngKeywords', String(2000), nullable=False)
    engabstract = Column('EngAbstract', String(4000), nullable=True)
    classification = Column('Classification', String(150), nullable=True)
    conferencesname = Column('ConferencesName', String(200), nullable=False)
    year = Column('Year', String(20), nullable=False)
    page = Column('Page', String(255), nullable=True)
    publisher = Column('Publisher', String(200), nullable=True)
    language = Column('language', String(50), nullable=False)
    lastmodified = Column('LastModified', TIMESTAMP)

