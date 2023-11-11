# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class WikiartspiderItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class ArtistItem(scrapy.Item):

    id = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    nation = scrapy.Field()
    image = scrapy.Field()
    artistUrl = scrapy.Field()
    totalWorksTitle = scrapy.Field()
    
class ArtistRelationshipItem(scrapy.Item):
    influenced_on = scrapy.Field()
    influenced_by = scrapy.Field()
    friends = scrapy.Field()
    movements = scrapy.Field()
    institution = scrapy.Field()
    school = scrapy.Field()
    artistUrl = scrapy.Field()
    type = scrapy.Field()


class SchoolItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()


class InstitutionItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()



