# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EdmundsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Price = scrapy.Field()
    VIN = scrapy.Field()
    Vehicle_Summary = scrapy.Field()
    Top_Features_And_Specs = scrapy.Field()