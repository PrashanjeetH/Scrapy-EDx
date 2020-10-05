# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    courseLink = scrapy.Field()
    courseTitle = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    discription = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    subject = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    imageSrc = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    price = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    certificate = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    provider = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    length = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    language = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    level = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    availableDate = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
    enrolledNo = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
        )
