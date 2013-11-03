__author__ = 'sid'

import urllib.request
from bs4 import BeautifulSoup


def getPageAsSoup(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("HTTPError with: ", url, e)
        return None
    the_page = response.read()
    soup = BeautifulSoup(the_page)

    return soup
