from bs4 import BeautifulSoup
import numpy as np
import requests

LINK = "https://www.ebay.pl/sch/i.html?_nkw=samsung+s24+ultra&_sacat=0&_from=R40&_trksid=p4582968.m570.l1311"

def get_prices_by_link (link):
        r = requests.get(link)
        page_parse = BeautifulSoup (r.text, 'html.parser')
        print (page_parse)
        print("test")

        return

if __name__ == "__main__":
    get_prices_by_link(LINK) 