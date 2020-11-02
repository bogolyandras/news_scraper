#!/usr/bin/env python3

from scrapy.crawler import CrawlerProcess

from news_scraper.spiders.theguardian import TheguardianSpider
import news_scraper.settings as settings

c = CrawlerProcess(vars(settings))
c.crawl(TheguardianSpider)
c.start()
