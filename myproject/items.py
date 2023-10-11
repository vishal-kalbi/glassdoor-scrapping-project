# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassdoorTcsReview(scrapy.Item):
    review_title=scrapy.Field()
    rating = scrapy.Field()
    pros = scrapy.Field()
    cons = scrapy.Field()
    date = scrapy.Field()
