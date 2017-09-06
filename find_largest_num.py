#This function is taken from a longer script. It is used to give a broad indication of the biggest numbers in an MP's entry, which can then be sorted in a spreadsheet. However, it still produces incomplete data which we check.
#define the function
def find_largest_num(stringtore):
    #examples could be £60, £107.57, £1,155.88 but not '72 Broad Street'
    #replace new lines and split on each pound sign
    splitstring = stringtore.replace("\n"," ").split("£")
    #that creates a list - the length of it (how many numbers) is checked here
    numbers = len(splitstring)
    print "there are ", numbers, "mentions of £"
    biggestnum = 0
    totalnums = 0
    if len(splitstring)>1:
        print "first figure: ", splitstring[1].split(" ")[0]
        storingnums = []
        for i in range(1,numbers):
            #Some numbers break the scraper and are individually addressed in this line
            thisnum = splitstring[i].split(" ")[0].replace(",","").replace(")","").replace("-","").replace("p.a","").replace("2.676.41","2676.41").replace("1.261.79","1261.79")
            print thisnum
            if thisnum.endswith('.'):
                thisnum = thisnum[:-1]
            storingnums.append(float(thisnum.strip()))
            print storingnums
        biggestnum = max(storingnums)
        totalnums = len(storingnums)
    print biggestnum
    return biggestnum, totalnums
