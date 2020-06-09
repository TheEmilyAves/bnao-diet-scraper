"""
Scrapy spider for extracting codes from all Birds of the World pages
by scraping urls from the "Browse Taxonomy" page

as is it makes a text file of all the html lines containing urls, which is great 
but it also includes the links for families (not just species)
not sure how to fix yet...
"""

import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request

class AllCodesSpider(scrapy.Spider): 
    name = "allcodes"
    
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
        yield Request(
                url = "https://birdsoftheworld-org.proxy.birdsoftheworld.org/bow/species", callback = self.action)
        
    
    def action(self, response):
        t = response.xpath("//a[contains(@href,'/bow/species/') and @class='notranslate']").extract()
        with open("allurls.txt", "a") as f:
            for i, line in enumerate(t):
                f.write(line + "\n")

