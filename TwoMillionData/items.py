# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TwomilliondataItem(scrapy.Item):
    image_urls = scrapy.Field()  # 保存图片地址
    images = scrapy.Field()  # 保存图片的信息
    pass
