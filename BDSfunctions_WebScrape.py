"""
Scrapy spider for...
1. logging in to Birds of the World via AOS access
2. going to "Diet and Foraging" section of given set of species pages
3. extracting only the "Diet" subsection as txt file output

Works for some species as is, but there is a weird redirecting issue

Also still need to figure out how to put a column in for species name
"""

import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request
#from scrapy.utils.response import open_in_browser
import csv

base_url_start = "https://birdsoftheworld-org.proxy.birdsoftheworld.org/bow/species/"
base_url_end = "/cur/foodhabits"

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
    s = ""
    for i in t:
        # if item starts with end line notation...
        # note1: this also excludes the reference information
        # note2: if I want these later, I can write something here to pull refs specifically
        if i[:1] == "\n":
            # ignore it
            pass
        # if header...
        # note1: will need to add other headers to this for all species
        # note2: might be easier to ask if i is in a list of headers
        elif i == "Quantitative Analysis" or i == "Diet":
            # also ignore it
            pass
        # everything else should be what I want
        else:
            # concatenate this item to the existing string
            s = s + i.strip()
    return s


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
            # the meta part is supposed to fix the redirect issue but
            # this just skips the species that are having problems...
            yield Request(
                    url = base_url_start + page + base_url_end, 
                    meta = {"dont_redirect": True, 
                            "handle_httpstatus_list": [302]},
                    callback = self.action) 
        
    
    def action(self, response):
        pass
        #open_in_browser(response)
        # used Firefox dev tools to copy xpath from inspecting elements
        t = response.xpath("/html/body/div/main/div[2]/div/div/div[2]/section[2]/descendant-or-self::text()").extract()
        s = cleanText(t)
        with open("dietdata.csv", mode="a", encoding="utf-8") as csv_file:
            diet_writer = csv.writer(csv_file)
            row = []
            #row.append(page)
            row.append(s)
            diet_writer.writerow(row)

