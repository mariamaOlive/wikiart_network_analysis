
# import modules 
import scrapy 
import json 
from wikiArtSpider.items import SchoolItem
import pandas as pd
  
  
class PersonSpider(scrapy.Spider): 
    name = "school"
  
    def start_requests(self): 

        url_base = "https://www.wikiart.org"
        df_artists_rel = pd.read_csv("relationships.csv")
        list_schools = df_artists_rel["school"].explode().unique().tolist()
        list_schools = [x for x in list_schools if x == x]


        yield scrapy.Request(url_base, self.parse) 

        for school in list_schools:
            url_request = url_base + school
            print(url_request)
            yield scrapy.Request(url_request, self.parse,  meta={'url': school}) 
  
    def parse(self, response): 
        school_item = SchoolItem()
        title = response.xpath('//div[@class="wiki-breadcrumbs"]/following-sibling::header/h1/text()').get()

        school_item["url"] = response.meta['url']
        school_item["title"] = title.strip()
        yield school_item
  