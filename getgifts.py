#This function is part of a larger script. It specifically grabs the gifts part and saves in a separate SQL database to the main register scrape
def getgifts(gifts3, gifts5, mpurl, mp):
    indexlist = []
    if gifts3 != "No entry":
        print "NOW GRABBING GIFTS: ", gifts3, gifts5, mpurl, mp
        gifttext = gifts3.replace(', benefits and hospitality from UK sources','')
        giftlist = gifttext.split("Name of donor: ")
        donorrecord = {}
        i = 0
        for gift in giftlist[1:]:
            i = i+1
            donorrecord['index'] = str(i)+mpurl
            print "GIFT: ", gift #ITV plcAddress of donor: The London Television Centre, Upper Ground, London SE1 9LTAmount of donation or nature and value if donation in kind: ticket to attend the National Television Awards with a value of £1,028Date received: 25 January 2017Date accepted: 25 January 2017Donor status: company, registration 4967001(Registered 13 March 2017)
            print "of ", len(giftlist), " gifts"
            donorrecord['donorname'] = gift.split("Address of donor: ")[0] #ITV plc
            try:
                donorrecord['donoraddress'] = gift.split("Address of donor: ")[1].split("Amount of donation or nature and value if donation in kind: ")[0] 
            except IndexError:
                donorrecord['donoraddress'] = 'could not extract'
            try:
                donationvalue = gift.split("donation in kind: ")[1].split("Date received: ")[0]
            except IndexError:
                print "TRYING AGAIN"
                donationvalue = gift.split(" amount of any donation): ")[1].split("Date received: ")[0]
            print "DONATIONVALUE", donationvalue
            donorrecord['donationdesc'] = donationvalue
            if len(donationvalue.split("total £"))>0:
                donorrecord['donationvalue'] = donationvalue.split("£")[1].replace(" ",";").replace(",","").replace("(","").replace(")","")
            else:
                donorrecord['donationvalue'] = 'could not extract'
            try:
                donorrecord['daterec'] = gift.split("Date received: ")[1].split("Date")[0]
            except IndexError:
                try:
                    donorrecord['daterec'] = gift.split("Date of receipt of donation: ")[1].split("Date")[0]
                except IndexError:
                    print "ERROR"
            try:
                donorrecord['dateacc'] = gift.split("Date accepted: ")[1].split("Donor status: ")[0]
            except IndexError:
                try:
                    donorrecord['dateacc'] = gift.split("Date of acceptance of donation: ")[1].split("Donor status: ")[0]
                except IndexError:
                    print "ERROR"
            try:
                donorrecord['donorstatus'] = gift.split("Donor status: ")[1]
            except IndexError:
                donorrecord['donorstatus'] = 'could not extract'
            donorrecord['url'] = mpurl
            print "DONORRECORD", donorrecord
            print "INDEX", donorrecord['index']
            indexlist.append(donorrecord['index'])
            print indexlist
            scraperwiki.sql.save(['index'],donorrecord, table_name="gifts")
    else:
        print "NO GIFTS TO GRAB"
