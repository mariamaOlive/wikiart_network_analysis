
# import modules 
import scrapy 
import json 
from wikiArtSpider.items import InstitutionItem
import pandas as pd
  
  
class PersonSpider(scrapy.Spider): 
    name = "institution"
  
    def start_requests(self): 

        url_base = "https://www.wikiart.org"
        df_artists_rel = pd.read_csv("relationships.csv")
        list_institutions = df_artists_rel["institution"].explode().unique().tolist()
        list_institutions = [x for x in list_institutions if x == x]


        yield scrapy.Request(url_base, self.parse) 

        for institution in list_institutions:
            url_request = url_base + institution
            print(url_request)
            yield scrapy.Request(url_request, self.parse,  meta={'url': institution}) 
  

    def parse(self, response): 
        institution_item = InstitutionItem()
        title = response.xpath('//div[@class="wiki-breadcrumbs"]/following-sibling::header/h1/text()').get()

        institution_item["url"] = response.meta['url']
        return_institution = self.get_institution(title.strip())
        institution_item["title"] = return_institution[0]
        institution_item["city"] = return_institution[1]
        institution_item["country"] = return_institution[2]
        yield institution_item


    # Gets name, city and country of the institution
    def get_institution(self, string_institution):
        parts = [part.strip() for part in string_institution.split(',')]

        # Extract school, city, and country if available
        school = parts[0]

        # Check if city and country are available
        if len(parts) > 1:
            city = parts[1]
        else:
            city = None

        if len(parts) > 2:
            country = parts[2]
        else:
            country = None

        return (school, city, country)

  