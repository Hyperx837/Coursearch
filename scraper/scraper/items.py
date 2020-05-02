# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    course_url = scrapy.Field()
    price = scrapy.Field()
    duration = scrapy.Field()
    image_url = scrapy.Field()

