"""
Scrapy spider for scraping all six-letter codes for ABA bird checklist species, 
because Birds of the World uses these codes in their urls.
"""

import scrapy


class ABACodesSpider(scrapy.Spider):
    name = "abacodes"
    
    def start_requests(self):
        urls = ['https://jaxbirding.com/ABA-sixlettercode.php']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        txt = response.xpath("//*[@id=\"content\"]/descendant-or-self::text()").extract()
        with open("codes.txt", "a") as f:
            for i, line in enumerate(txt):
                f.write(line + "\n")



