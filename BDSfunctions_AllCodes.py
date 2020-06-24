"""
BDS Functions for extracting all Birds of the World codes from 
BDSspider_AllCodes.py output
"""

file = "allurls.txt"

import csv

class SPECIES:
    """
    A class which makes objects containing species information
    """
    def __init__(self, code="", spname="", coname=""):
        self.__code = code
        self.__spname = spname
        self.__coname = coname
    
    
    @property
    def code(self):
        """
        code is a string that represents the six or seven letter/number code
        (e.g. comyel or ostric2) of an avian species in Birds of the World
        """
        return self.__code
    
    
    @code.setter
    def set_code(self, value):
        self.__code = value


    @property
    def spname(self):
        """
        spname is a string that represents a scientific species name
        """
        return self.__spname
    
    
    @spname.setter
    def set_spname(self, value):
        self.__spname = value


    @property
    def coname(self):
        """
        coname is a string that represents a common species name
        """
        return self.__coname
    
    
    @coname.setter
    def set_coname(self, value):
        self.__coname = value


def readAllURLs(file):
    """
    Reads allurls.txt file (scraped from Birds of the World) and makes 
    dictionary of SPECIES objects which contain scientific name, common 
    name, and BotW code for each species
    """
    infile = open(file, "r+", encoding="utf-8")
    sp_obj_dict = {}
    for line in infile:
        # if a family name line, skip it
        # if I want to do something with family names later, this works
        if line[72:91] == "class=\"ListGrid-key":
            pass
        # all other lines containing this section of url are species
        elif line[:22] == "<a href=\"/bow/species/":
            nextline = next(infile)
            sp_obj = invokeSPECIES(line, nextline)
            key = sp_obj.spname
            sp_obj_dict[key] = sp_obj
        else:
            pass
    return sp_obj_dict


def invokeSPECIES(line, nextline):
    code = line[22:29].rstrip("/")
    spname = getSpname(nextline)
    coname = getConame(nextline)
    sp_obj = SPECIES(code=code, spname=spname, coname=coname)
    return sp_obj


def getSpname(nextline):
    return nextline.split(">")[1].split("<")[0]


def getConame(nextline):
    return nextline.split("<")[0].strip()


def getOutput(sp_obj_dict):
    with open("allCodes.csv", mode="w", encoding="utf-8") as csv_file:
        code_writer = csv.writer(csv_file)
        for s in sp_obj_dict.keys():
            row = []
            row.append(sp_obj_dict[s].code)
            row.append(s)
            row.append(sp_obj_dict[s].coname)
            code_writer.writerow(row)


def main():
    sp_obj_dict = readAllURLs(file)
    getOutput(sp_obj_dict)


if __name__ == "__main__":
    main()


