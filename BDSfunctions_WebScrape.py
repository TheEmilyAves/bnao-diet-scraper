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
import csv

base_url_start = "https://birdsoftheworld-org.proxy.birdsoftheworld.org/bow/species/"
base_url_end = "/cur/foodhabits"
#pages = ["comyel"]

# write function to clean up output before making csv file


def getPages(file, allcodesfile):
    """
    Uses txt file with line-by-line list of species names to find and select 
    the right codes to add to pages for web scraping
    """
    pages = []
    infile = open(file, "r")
    for line in infile:
        line = line.rstrip("\n")
        with open(allcodesfile) as csvfile:
            codereader = csv.reader(csvfile)
            for row in codereader:
                # if species name matches with given list
                if row[1] == line:
                    # add corresponding code to pages
                    pages.append(row[0])
                # otherwise, do nothing
                else:
                    pass
    return pages


def cleanText(t):
    # iterate through t which is a list
    # strip off whitespace, exclude headers, and make one single string
    pass


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
        file = input("Enter input file name: ")
        allcodesfile = "allCodes.csv"
        pages = getPages(file, allcodesfile)
        for page in pages:
            yield Request(
                    url = base_url_start + page + base_url_end, callback = self.action)
        
    
    def action(self, response):
        pass
        #open_in_browser(response)
        t = response.xpath("/html/body/div/main/div[2]/div/div/div[2]/section[2]/descendant-or-self::text()").extract()
        tclean = cleanText(t)
        print(tclean)
        
        #with open("output1.txt", "a") as f:
        #    for i, line in enumerate(t):
        #        f.write(line + "\n")


# used Firefox dev tools to copy xpath from inspecting elements

# this xpath gets the whole diet section (all html code)
# /html/body/div/main/div[2]/div/div/div[2]/section[2]/

# this xpath gets the text only from the diet section, but doesn't separate
# desired content from other stuff completely
# /html/body/div/main/div[2]/div/div/div[2]/section[2]/descendant-or-self::text()

# could clean up by adding if statements in the for loop when writing
# I need a better idea of what I want my output to be though...

# once I get the output I want, then I need to test with a few other species
# then figure out how to get a complete list of codes to iterate through

# Can't guarantee that each sentence is going to be a different estimate, so 
# maybe just one entry for each for the purposes of web scraping

