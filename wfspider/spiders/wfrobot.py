# -*- coding: utf-8 -*-

from twisted.internet import defer

import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector

from wfspider.items import SpiderItem, ExportItem


class WfrobotSpider(scrapy.spiders.CrawlSpider):
    name = "wfrobot"
    allowed_domains = ["wanfangdata.com.cn"]
    start_urls = [
        u"http://s.wanfangdata.com.cn/Paper.aspx?q=海洋资源勘探"
    ]
    rules = [
        Rule(
            LinkExtractor(
                allow=(''),
                deny=('p=3'),  # 设置爬几页搜索结果
                restrict_xpaths=(u'//p[contains(@class, "pager")]/a[contains(text(), "下一页")]')),
            callback='parse_item',
            follow=True
        )
    ]

    # def parse(self, response):
    #     for sel in response.css('.record-item'):
    #         item = SpiderItem()
    #         item['name'] = sel.css('.title')[0].xpath('string(.)').extract()
    #         item['url'] = sel.css('.title')[0].xpath('@href').extract()
    #         print item['name'], item['url']
    #         yield item


    def parse_item(self, response):
        ExportUrl = "http://s.wanfangdata.com.cn/Export/Export.aspx?scheme=NoteFirst"
        for sel in response.css('.record-item'):

            item = SpiderItem()
            item['name'] = sel.css('.title')[0].xpath('string(.)').extract()
            item['url'] = sel.css('.title')[0].xpath('@href').extract()
            item['data'] = sel.css('.exportLink')[0].xpath('@data-resourceid').extract()

            # item['export'] = self.get_xml(response.headers, str(item['data'][0]))
            export = str(item['data'][0])

            # ExportResponse = scrapy.http.TextResponse(url=ExportUrl,
            #                                           headers=response.headers,
            #                                           request=scrapy.http.Request(
            #                                             url=ExportUrl,
            #                                             headers=response.headers,
            #                                             cookies={'rs': str(item['data'][0])},
            #                                             meta={'dont_merge_cookies': False}))

            yield scrapy.http.Request(
                url=ExportUrl+'&rs='+export,
                headers=response.headers,
                cookies={'rs': export},
                meta={'dont_merge_cookies': False},
                callback=self.parse_export
            )
            # ExportResponse = self._response_downloaded(
            #     scrapy.http.TextResponse(
            #         url=ExportUrl,
            #         headers=response.headers,
            #         request=scrapy.http.Request(
            #                 url=ExportUrl,
            #                 headers=response.headers,
            #                 cookies={'rs': str(item['data'][0])}
            #         )
            #     )
            # )

            # export = self._parse_response(response=ExportResponse, callback=self.parse_export, cb_kwargs={})

            # self.handles_request(ExportRequest)

            # item['export'] = ExportResponse.css('#export_container').xpath('string(.)').extract()
            # print response.headers
            # print ExportResponse.headers
            # print ExportResponse.meta
            # print ExportResponse.xpath('//body').extract()
            # print ExportResponse.xpath('//div[contains(@id, "export_right")]').extract()
            # print ExportResponse.css('#export_right').extract()

            # print item['name'][0].encode('utf-8'), item['url'][0].encode('utf-8')
            # yield item


    def get_xml(self, headers, rs):
        ExportUrl = "http://s.wanfangdata.com.cn/Export/Export.aspx?scheme=NoteFirst"

        export = yield scrapy.Request(
                url=ExportUrl,
                headers=headers,
                cookies={'rs': rs},
                meta={'dont_merge_cookies': False},
                callback=self.parse_export
        )

        # return export

    def parse_export(self, response):
        item = ExportItem()
        print response.css('#export_container').xpath('string(.)').extract()

        item['export'] = response.css('#export_container').xpath('string(.)').extract()
        # yield str(response.css('#export_container').xpath('string(.)').extract())
        return item