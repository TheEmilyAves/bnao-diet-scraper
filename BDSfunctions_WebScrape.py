"""
Scrapy spider for...
1. logging in to Birds of the World via AOS access
2. going to "Diet and Foraging" section of given set of species pages
3. extracting only the "Diet" subsection as txt file output
"""

import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request
#from scrapy.utils.response import open_in_browser

base_url_start = "https://birdsoftheworld-org.proxy.birdsoftheworld.org/bow/species/"
base_url_end = "/cur/foodhabits"
pages = ["comyel"]

class DietsSpider(scrapy.Spider):
    name = "diets"
    start_urls = [
            "https://login.proxy.birdsoftheworld.org/login"
    ]
    
    def parse(self, response):
        aosuser = input("Enter username: ")
        password = input("Enter password: ")
        user = "AOS-" + aosuser
        return FormRequest.from_response(response, formdata = {
                "user": user, 
                "url": "https://birdsoftheworld.org", 
                "aosuser": aosuser, 
                "pass": password
                }, callback = self.after_login)
    
    def after_login(self, response):
        for page in pages:
            yield Request(
                    url = base_url_start + page + base_url_end, callback = self.action)
        
    
    def action(self, response):
        #open_in_browser(response)
        t = response.xpath("/html/body/div/main/div[2]/div/div/div[2]/section[2]").extract()
        with open("output.txt", "a") as f:
            for i, line in enumerate(t):
                f.write(line + "\n")





