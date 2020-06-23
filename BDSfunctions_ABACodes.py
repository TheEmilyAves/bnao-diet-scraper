"""
BDS functions for extracting six letter codes from text file produced 
by BDSspider_ABACodes.py
"""

file = "codes.txt"

# read and get all codes
def getAllCodes():
    infile = open(file, "r")
    codes = {}
    for line in infile:
        # this and the next if/else statement ensure that only codes are kept, not headers
        if line[:5].isupper() == True:
            line_split = line.rstrip("\n").split("    ")
            if len(line_split) == 2:
                key = line_split[0]
                value = line_split[1]
                # if the dash stays in for some weird reason
                if value[0] == "-":
                    # remove the dash and extra spaces
                    value = value[3:]
                else:
                    pass
                codes[key] = value
            else:
                pass
        else:
            pass
    return codes


def getParulidaeCodes():
    infile = open(file, "r")
    codes = {} 
    isParulid = False
    for line in infile:
        if line[:13] == "WOOD-WARBLERS":
            isParulid = True
        elif line[:11] == "BANANAQUITS":
            isParulid = False
        elif isParulid == True and line[:5].isupper() == True and line[:12] != "WOOD-WARBLERS" and line[:10] != "BANANAQUITS":
            line_split = line.rstrip("\n").split("    ")
            if len(line_split) == 2:
                key = line_split[0]
                value = line_split[1]
                if value[0] == "-":
                    value = value[3:]
                else:
                    pass
                codes[key] = value
        else:
            pass
    return codes


def getOutput(codes):
    outfile = open("listofcodes.txt", "w")
    for k in codes.keys():
        print(k, file = outfile)
    outfile.close()


def main():
    codes = getParulidaeCodes()
    getOutput(codes)


if __name__ == "__main__":
    main()




