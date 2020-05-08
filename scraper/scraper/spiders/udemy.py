import uuid

import scrapy
import json

from ..items import CourseItem


class CourseScraper(scrapy.Spider):
    name = 'udemy'

    @property
    def headers(self):

        page = self.data["pagination"]["current_page"] + 1 if hasattr(self, 'data') else 1

        return {
            'path': f'/api-2.0/search-courses/?q=python&src=ukw&skip_price=true&p={page}',
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'authority': 'www.udemy.com',
            'referer': f'https://www.udemy.com/courses/search/?src=ukw&q=python'
        }

    def start_requests(self):
        url = 'https://www.udemy.com/api-2.0/search-courses/?q=python&src=ukw&skip_price=true'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        self.data = json.loads(response.body)

        for course in self.data['courses']:
            yield CourseItem(
                id=uuid.uuid4(),
                title=course['title'],
                course_id=course['id'],
                course_url=course['url'],
                ratings=course['rating'],
                duration=course['content_info'],
                image_url=course['image_304x171'],
                description=course['headline'],
                students=course['num_subscribers'],
                instructors=[instructor['display_name'] for instructor in course['visible_instructors']],
            )

        if self.data["pagination"]["current_page"] < 3:
            next_url = self.data["pagination"]["next"]["url"]
            yield response.follow(next_url, headers=self.headers)
