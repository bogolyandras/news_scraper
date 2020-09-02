from scrapy.spiders import XMLFeedSpider


class TheguardianSpider(XMLFeedSpider):

    name = 'theguardian'

    allowed_domains = ['https://www.theguardian.com']
    start_urls = ['https://www.theguardian.com/world/rss']

    iterator = 'iternodes'
    itertag = 'item' # will iterate on <item>

    def parse_node(self, response, selector):

        self.logger.info('Node tag <%s>: %s', self.itertag, ''.join(selector.getall()))

        item = {}
        item['original'] = selector.getall()
        return item
