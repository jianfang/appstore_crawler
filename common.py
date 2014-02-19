__author__ = 'sid'

import urllib.request
from bs4 import BeautifulSoup

DATA_DIR = "data"
DATA_APP_CAT_FILE = "app_cat"
DATA_APP_URL_FILE = "app_urls"
DATA_APP_COUNT_FILE = ".app_count"

def getPageAsSoup(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("HTTPError with: ", url, e)
        return None
    the_page = response.read()
    soup = BeautifulSoup(the_page)

    return soup
