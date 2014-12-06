__author__ = 'wzc'
import scrapy

from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    """my own spider used to scrape info from a domain"""
    name = "dmoz"  # identify the spider
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    """
    #this method is responsible for parsing the response data
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
    """

    """
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract();
            desc = sel.xpath('text()').extract();
            print title, link, desc
    """

    def parse(self, response):
        """ use our item 'DmozItem'
        """
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
