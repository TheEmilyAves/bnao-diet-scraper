# BNAO Diet Scraper

This project was initially designed to scrape diet data from Birds of North America Online (BNAO), which is now Birds of the World. I use Scrapy Spiders in Python to extract text files with the relevant data plus additional functions in separate files to clean up the data for use later.

*BDSfunctions_WebScrape.py* (which is poorly named at the moment) is a spider that logs into Birds of the World via an American Ornithologists' Society (AOS) login, goes to any number of diet pages provided in a list (right now just 'comyel' or Common Yellowthroat) and extracts all text from the diet section into a text file. 

*BDSspider_ABACodes.py* is a spider that extracts all 969 six-letter codes which are used by Birds of the World in the url of these species pages.

*BDSspider_AllCodes.py* is a spider that logs into Birds of the World via an AOS login, goes to the browse taxonomy page, and scrapes the urls into a text file. Eventually this will turn into a list of all species codes that can be used by the spider in BDSfunctions_WebScrape.py.

## Author

Emily Webb, Biology PhD Candidate at Arizona State University

