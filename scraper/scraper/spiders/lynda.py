# -*- coding: utf-8 -*-
import uuid

import scrapy
import re

from ..items import CourseItem


class LyndaSpider(scrapy.Spider):
    name = 'lynda'
    start_urls = ['https://www.lynda.com/search?q=python&page=1']

    def parse(self, response):
        _, current_page = (re.findall(r'page=\d+', response.url)[0]).split('=')

        for course in response.css('.course'):
            yield CourseItem(
                id=uuid.uuid4(),
                title=''.join(course.css('.col-sm-9 h2 *::text').extract()).strip(),
                course_url=course.css('a::attr(href)').get(),
                image_url=course.css('img::attr(data-lazy-src)').get(),
                duration=course.css('.meta-duration::text').get(),
                instructors=course.css('.meta-author::text').get(),
                students=course.css('.meta-views::text').get().split()[-1],
                description=course.css('.meta-description::text').get()
            )

        if int(current_page) < 2:
            url = f'https://www.lynda.com/search?q=python&page={int(current_page) + 1}'
            yield scrapy.Request(url, callback=self.parse)
