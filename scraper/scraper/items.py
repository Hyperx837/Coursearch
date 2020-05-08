# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    id = scrapy.Field()
    course_url = scrapy.Field()
    course_id = scrapy.Field()
    duration = scrapy.Field()
    image_url = scrapy.Field()
    ratings = scrapy.Field()
    instructors = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    students = scrapy.Field()

