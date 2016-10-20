##############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
import urlparse
import lxml.html
import urllib
import time

storenumber = 0

while storenumber < 1:
    time.sleep(1)
    storenumber = storenumber + 1 # putting this at top instead of bottom seemed to make a difference for redirect loops
    url = 'http://www.starbucks.com/store-locator/store/' + str(storenumber)
    html = urllib.urlopen(url).read()
    print html
    root = lxml.html.fromstring(html)
    addressblock = root.cssselect("div.adr")
    if addressblock:
        storename = root.cssselect("h2")[2]
        street = root.cssselect("span.street-address")
        extended = root.cssselect("span.extended-address")
        locality = root.cssselect("span.locality")
        region = root.cssselect("span.region")
        postcode = root.cssselect("span.postal-code")        
        country = root.cssselect("span.country-name")
        tel = root.cssselect("span.tel")
        record = {}
        record['StoreID'] = str(storenumber)
        try:
            record['Storename'] = storename.text_content()
        except:
            record['Storename'] = ""
        try:
            record['Street'] = street[0].text_content()
        except:
            record['Street'] = ""
        try:
            record['Extended'] = extended[0].text_content()
        except:
            record['Extended'] = ""
        try:
            record['Locality'] = locality[0].text_content()
        except:
            record['Locality'] = ""
        try:
            record['Region'] = region[0].text_content()
        except:
            record['Region'] = ""
        try:
            record['Postcode'] = postcode[0].text_content()
        except:
            record['Postcode'] = ""
        try:
            record['Country'] = country[0].text_content()
        except:
            record['Country'] = ""
        try:
            record['Tel'] = tel[0].text_content()
        except:
            record['Tel'] = ""
        print record
        scraperwiki.sqlite.save(["StoreID"], record)

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
