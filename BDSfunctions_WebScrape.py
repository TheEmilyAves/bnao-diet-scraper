"""
Scrapy spider for logging in to Birds of the World via AOS access
"""

import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

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
                }, callback = self.start_scraping)
    
    def start_scraping(self, response):
        open_in_browser(response)




