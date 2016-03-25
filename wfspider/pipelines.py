# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

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
        
        return item




