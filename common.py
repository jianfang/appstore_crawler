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

#------------------------------------------------------------------------------
# App store URLs
#
#   US (Global)
#     Genre:
#       https://itunes.apple.com/us/genre/ios/id36?mt=8
#     Chart:
#       http://www.apple.com/itunes/charts/free-apps/
#       http://www.apple.com/itunes/charts/paid-apps/
#     App:
#       https://itunes.apple.com/us/app/paper-by-fiftythree/id506003812?mt=8
#
#   CN
#     Genre:
#       https://itunes.apple.com/cn/genre/ios/id36?mt=8
#     Chart:
#       http://www.apple.com/cn/itunes/charts/free-apps/
#       http://www.apple.com/cn/itunes/charts/paid-apps/
#     App:
#       https://itunes.apple.com/cn/app/wei-xin/id414478124?mt=8
#------------------------------------------------------------------------------

def getGenreUrl(country):
    url = 'https://itunes.apple.com/' + country + '/genre/ios/id36?mt=8'
    return url

def getChartUrl(country, type):
    url = 'http://www.apple.com/'
    if country != 'us':
        url += country + '/'
    url += 'itunes/charts/' + type + '-apps/'
    return url

def getApptUrlPrefix(country):
    prefix = 'https://itunes.apple.com/' + country + '/app'
    return prefix

def getChartFile(country, type):
    file = 'charts'
    if country != 'us':
        file += '_' + country
    file += '/top100_' + type + '_apps'
    return file

def getChartPageSection(country):
    section = ''
    if country == 'cn': # cn only
        section = 'section apps grid'
    else: # us, jp, etc.
        section = 'section apps chart-grid'
    return section

def getAppId(appLongUrl):
    id = "000000000"
    index = appLongUrl.find("/id")
    if index > 0:
        id = appLongUrl[index + 3 : index + 12]
    return id

def getAppUrl(country, appid):
    url = getApptUrlPrefix(country) + "/id" + appid
    return url




