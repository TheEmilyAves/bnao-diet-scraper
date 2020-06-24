# BNAO Diet Scraper

This project was initially designed to scrape diet data from Birds of North America Online (BNAO), which is now Birds of the World. I use Scrapy Spiders in Python to extract text files with the relevant data plus additional functions in separate files to clean up the data for use later.

## Scrapy Spiders

*BDSfunctions_WebScrape.py* (which is poorly named at the moment) is a spider that logs into Birds of the World via an American Ornithologists' Society (AOS) login, goes to any number of diet pages provided in a list of scientific names in a .txt file and extracts all text from the diet section. Then it puts text from each species into a separate row of a csv file. Still debugging.

*BDSspider_ABACodes.py* is a spider that extracts all 969 six-letter codes which are used by Birds of the World in the url of these species pages.

*BDSspider_AllCodes.py* is a spider that logs into Birds of the World via an AOS login, goes to the browse taxonomy page, and scrapes the urls into a text file. Eventually this will turn into a list of all species codes that can be used by the spider in BDSfunctions_WebScrape.py.

## Other Files

*BDSfunctions_ABACodes.py* takes the output file from BDSspider_ABACodes.py, extracts the codes, and outputs a .txt file list of codes. Also has a function for extracting Parulidae codes specifically. Could be expanded to call specific families with user input eventually.

*BDSfunctions_AllCodes.py* takes the output file from BDSspider_AllCodes.py, extracts the codes, and outputs a .csv file with separate columns for codes, scientific names, and common names of all species in Birds of the World.

## Author

Emily Webb, Biology PhD Candidate at Arizona State University

