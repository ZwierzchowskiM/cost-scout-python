# main.py

from src.tracker import get_prices_by_link

LINK = "https://www.ebay.pl/sch/i.html?_nkw=samsung+s24+ultra&_sacat=0&_from=R40&_trksid=p4582968.m570.l1311"

if __name__ == "__main__":
    get_prices_by_link(LINK)