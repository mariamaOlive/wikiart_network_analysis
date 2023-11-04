
# import modules 
import scrapy 
import json 
from wikiArtSpider.items import ArtistItem
  
  
class ArtistsSpider(scrapy.Spider): 
    name = "artists"
  
    def start_requests(self): 

        for page_number in range(1, 53):
            url_request = "https://www.wikiart.org/en/App/Search/Artists-by-Field?json=3&searchterm=painting&layout=new&page="+str(page_number)+"&resultType=masonry"
            yield scrapy.Request(url_request, self.parse) 
  
    def parse(self, response): 
        data = json.loads(response.text) 
        list_artists = data["Artists"]

        for artist in list_artists:

            artistItem = ArtistItem()
            artistItem["id"] = artist["id"]
            artistItem["title"] = artist["title"]
            artistItem["year"] = artist["year"]
            artistItem["nation"] = artist["nation"]
            artistItem["image"] = artist["image"]
            artistItem["artistUrl"] = artist["artistUrl"]
            artistItem["totalWorksTitle"] = artist["totalWorksTitle"]

            yield artistItem
  
  
