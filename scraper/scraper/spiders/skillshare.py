# -*- coding: utf-8 -*-
import scrapy
import json
import uuid
import re

from ..items import CourseItem


class SkillShareSpider(scrapy.Spider):
    name = 'skillshare'
    start_urls = ['https://www.skillshare.com/search?query=python&page=0']

    def parse(self, response):
        # item = CourseItem()  # link, thumbnail, instructor, students, time, title
        _, current_page = (re.findall(r'page=\d+', response.url)[0]).split('=')
        print(current_page)
        data = json.loads(re.findall(r"SS.serverBootstrap =(.+?);\n", response.body.decode('utf-8'), re.S)[0])
        for course in data['classesData']['parentClasses']:
            yield CourseItem(
                id=uuid.uuid4(),
                title=course['title'],
                course_url=course['url'],
                image_url=course['image'],
                students=course['numStudents'],
                duration=course['totalSessionsDuration'],
                instructors=course['teacher']['fullName'],
            )
        # yield data

        if int(current_page) < 3:
            url = data["classesData"]["pagination"]["next"]
            yield scrapy.Request(url, callback=self.parse)

        # item['course_url'] =
        # yield data
