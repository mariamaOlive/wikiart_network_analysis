
# import modules 
import scrapy 
import json 
from wikiArtSpider.items import ArtistRelationshipItem
import pandas as pd
  
  
class PersonSpider(scrapy.Spider): 
    name = "person"
  
    def start_requests(self): 

        url_base = "https://www.wikiart.org"
        df_artists = pd.read_csv("artists.csv")
        list_urls = df_artists["artistUrl"].tolist()


        yield scrapy.Request(url_base, self.parse) 

        for url in list_urls:
            url_request = url_base + url
            yield scrapy.Request(url_request, self.parse,  meta={'artist': url}) 
  
    def parse(self, response): 
        artistRelationshipItem = ArtistRelationshipItem()

        type_entry = response.xpath('//div[@class="wiki-breadcrumbs-links"]/a[2]/text()').get()
       
        influeced_container = response.xpath('//s[text()="Influenced by:"]/..')
        influeced_list = influeced_container.xpath('.//a/@href').extract() 
        data_influenced = []
        for artist in influeced_list:
            data_influenced.append(artist)

        influeced_on_container = response.xpath('//s[text()="Influenced on:"]/..')
        influeced_on_list = influeced_on_container.xpath('.//a/@href').extract() 
        data_influenced_on = []
        for artist in influeced_on_list:
            data_influenced_on.append(artist)

        friends_container = response.xpath('//s[text()="Friends and Co-workers:"]/..')
        friends_list = friends_container.xpath('.//a/@href').extract() 
        data_friends = []
        for friend in friends_list:
            data_friends.append(friend)
            

        movement_container = response.xpath('//s[text()="Art Movement:"]/..')
        movement_list = movement_container.xpath('.//a/text()').extract() 
        data_movement = []
        for mov in movement_list:
            data_movement.append(mov)

        intitution_container = response.xpath('//s[text()="Art institution:"]/..')
        institution_list = intitution_container.xpath('.//a/@href').extract() 
        # data_intitution = []
        # for inst in institution_list:
        #     data_intitution.append(inst)

        school_container = response.xpath('//s[text()="Painting School:"]/..')
        school_list = school_container.xpath('.//a/@href').extract() 

        school_container = response.xpath('//s[text()="Painting School:"]/..')
        school_list = school_container.xpath('.//a/@href').extract() 

        artistRelationshipItem["influenced_on"] = data_influenced_on
        artistRelationshipItem["influenced_by"] = data_influenced
        artistRelationshipItem["friends"] = data_friends
        artistRelationshipItem["movements"] = data_movement
        artistRelationshipItem["institution"] = institution_list
        artistRelationshipItem["school"] = school_list
        artistRelationshipItem["artistUrl"] = response.meta['artist']
        artistRelationshipItem["type"] = type_entry

        yield artistRelationshipItem
  