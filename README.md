# MPs declare sports and bookies as most common donors

![](https://ichef.bbci.co.uk/news/624/cpsprodpb/E857/production/_97497495_chart_regint_birmingham-1.png)

In September 2017 we [published a story on sports and betting companies topping the list of donors treating MPs to gifts and hospitality](http://www.bbc.co.uk/news/uk-england-41027964). 

The story was based on an analysis of [the latest MPs' register of interests](https://publications.parliament.uk/pa/cm/cmregmem/170829/contents.htm), and followed a [story the previous month on MPs employing relatives](http://www.bbc.co.uk/news/uk-england-40709220). The data was scraped using a script written in Python.

## Get the data

* [Gifts and hospitality, by gift and MP, August 31 2017](https://github.com/BBC-Data-Unit/mp-gifts-bookies-2017/blob/master/gifts_registerofinterests_170829.csv)

## Other documents

* The Code of Conduct together with The Guide to the Rules relating to the Conduct of Members - House of Commons: [Chapter 1: Registration of Members' Financial Interests](https://publications.parliament.uk/pa/cm201516/cmcode/1076/107604.htm#a3)

## Visualisation

* Bar chart: Donors appearing most in register of MPs' interests (shown above)
* Bar chart: Biggest donors by value

# Code

These are part of a longer script which is still under development and will be published here later:
* [Python function: get each gift](https://github.com/BBC-Data-Unit/mp-gifts-bookies-2017/blob/master/getgifts.py
* [Python function: count numbers and find largest number in declaration text string](https://github.com/BBC-Data-Unit/mp-gifts-bookies-2017/blob/master/find_largest_num.py)

## Related repos

* [Register of interests: MPs employing family members](https://github.com/BBC-Data-Unit/mps-registers-of-interest)
