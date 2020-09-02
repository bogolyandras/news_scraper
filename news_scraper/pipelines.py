# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import json
import uuid


from pathlib import Path
from itemadapter import ItemAdapter


class JsonWriterPipeline:

    def __init__(self):
        Path('data').mkdir(parents=True, exist_ok=True)
        self.file = None

    def open_spider(self, spider):
        self.file = open('data' + os.path.sep + 'theguardian-' + str(uuid.uuid1()) + '.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
