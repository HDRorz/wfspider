# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from lxml import etree
import uuid
import scrapy
from sqlalchemy.orm import sessionmaker
from models import *


class ExportPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_models(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()

        xml = '<?xml version="1.0" encoding="utf-8"?>' \
              '<Bibliographies>' \
              '<BibliographiesCount>1</BibliographiesCount>' + item['notefirst'][0].encode('utf8') + '</Bibliographies>'
        print xml
        tree = etree.fromstring(xml)

        if item['type'] == 'Periodical':

            try:
                session.add(self.prase_periodical(xml))
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

        return item

    def prase_periodical(self, xml):
        print xml
        try:
            tree = etree.fromstring(xml)

            datasetid = tree.xpath('//Url/text()')
            title = tree.xpath('//Title[@Lang="chi"]/text()')
            author = tree.xpath('//Author/Info[@Lang="chi"]/FullName/text()')
            authoradd = tree.xpath('//Author/Info[@Lang="chi"]/Organization/text()')
            abstract = tree.xpath('//Abstract[@Lang="chi"]/text()')
            keywords = tree.xpath('//keyword[@Lang="chi"]/text()')
            engtitle = tree.xpath('//Title[@Lang="eng"]/text()')
            engkeywords = tree.xpath('//keyword[@Lang="eng"]/text()')
            engabstract = tree.xpath('//Abstract[@Lang="eng"]/text()')
            engauthor = tree.xpath('//Author/Info[@Lang="eng"]/FullName/text()')
            engauthoradd = tree.xpath('//Author/Info[@Lang="chi"]/Organization/text()')
            language = tree.xpath('//Language/text()')
            issn = tree.xpath('//ISSN/text()')
            doi = tree.xpath('//DOI/text()')
            classification = tree.xpath('//CLC/text()')
            journalname = tree.xpath('//Media[@Lang="chi"]/text()')
            engjournalname = tree.xpath('//Media[@Lang="eng"]/text()')
            year = tree.xpath('//Year/text()')
            volume = tree.xpath('//Volume/text()')
            period = tree.xpath('//Issue/text()')
            page = tree.xpath('//PageScope/text()')

            periodical = Periodical(
                guid=uuid.uuid1(),
                datasetid=', '.join(datasetid),
                title=', '.join(title),
                author=', '.join(author),
                authoradd=', '.join(authoradd),
                abstract=', '.join(abstract),
                keywords=', '.join(keywords),
                engtitle=', '.join(engtitle),
                engkeywords=', '.join(engkeywords),
                engabstract=', '.join(engabstract),
                engauthor=', '.join(engauthor),
                engauthoradd=', '.join(engauthoradd),
                language=', '.join(language),
                issn=', '.join(issn),
                doi=', '.join(doi),
                classification=', '.join(classification),
                journalname=', '.join(journalname),
                engjournalname=', '.join(engjournalname),
                year=', '.join(year),
                volume=', '.join(volume),
                period=', '.join(period),
                page=', '.join(page)
            )

            return periodical
        except:
            raise
        finally:
            return None


    def prase_thesis(self, xml):
        print xml
        try:
            tree = etree.fromstring(xml)

            datasetid = tree.xpath('//Url/text()')
            title = tree.xpath('//Title/text()')
            author = tree.xpath('//Author/Info/FullName/text()')
            abstract = tree.xpath('//Abstract/text()')
            keywords = tree.xpath('//keyword/text()')
            engtitle = tree.xpath('//Title[@Lang="eng"]/text()')
            engkeywords = tree.xpath('//keyword[@Lang="eng"]/text()')
            engabstract = tree.xpath('//Abstract[@Lang="eng"]/text()')
            classification = tree.xpath('//CLC/text()')
            degree = tree.xpath('//Degree/text()')
            major = tree.xpath('//Degree/text()')
    # subject = Column('Subject', String(200), nullable=False)
    # university = Column('University', String(200), nullable=False)
    # submitdate = Column('SubmitDate', String(20), nullable=False)
    # quliaficationdate = Column('QuliaficationDate', String(20), nullable=True)
    # supervisor = Column('Supervisor', String(20), nullable=False)
    # supervisoraffiliation = Column('SupervisorAffiliation', String(255), nullable=False)
    #         language = tree.xpath('//Language/text()')
    #
    #         thesis = Thesis(
    #             guid=uuid.uuid1(),
    #             datasetid=', '.join(datasetid),
    #             title=', '.join(title),
    #             author=', '.join(author),
    #             authoradd=', '.join(authoradd),
    #             abstract=', '.join(abstract),
    #             keywords=', '.join(keywords),
    #             engtitle=', '.join(engtitle),
    #             engkeywords=', '.join(engkeywords),
    #             engabstract=', '.join(engabstract),
    #             engauthor=', '.join(engauthor),
    #             engauthoradd=', '.join(engauthoradd),
    #             language=', '.join(language),
    #             issn=', '.join(issn),
    #             doi=', '.join(doi),
    #             classification=', '.join(classification),
    #             journalname=', '.join(journalname),
    #             engjournalname=', '.join(engjournalname),
    #             year=', '.join(year),
    #             volume=', '.join(volume),
    #             period=', '.join(period),
    #             page=', '.join(page)
    #         )
    #
    #         return thesis
        except:
            raise
        finally:
            return None