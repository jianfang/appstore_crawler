__author__ = 'sid'

import re
import string
import os

import common
from common import *

def getPopAppsInCategory(categoryUrl):
    #url = categoryUrl + "&page=" + str( start_idx )
    #print( url )
    categoryPage = common.getPageAsSoup(categoryUrl)
    #allAppLinks = [aDiv.get('href') for aDiv in
    #               categoryPage.findAll('a', href=re.compile('^https://itunes.apple.com/us/app'))]
    for aDiv in categoryPage.findAll('a', href=re.compile('^https://itunes.apple.com/us/app')):
        appLink = aDiv.get('href')
        text = aDiv.string
        print(appLink, text)


def getAppsInCategory(cat, categoryUrl, dump):
    if dump:
        f = open(DATA_DIR + '/' + cat + '/' + DATA_APP_URL_FILE, 'w')

    for alphabet in string.ascii_uppercase:
        url = categoryUrl + '&letter=' + alphabet
        getAppInCategoryWithLetter(url, f)

    url = categoryUrl + '&letter=*'
    getAppInCategoryWithLetter(url, f)

    if dump:
        f.close()


def getAppInCategoryWithLetter(categoryUrl, f):
    previous_apps = []
    start_idx = 1
    while True:
        url = categoryUrl + "&page=" + str(start_idx)
        #print( url )
        categoryPage = common.getPageAsSoup(url)
        allAppLinks = [aDiv.get('href') for aDiv in
                       categoryPage.findAll('a', href=re.compile('^https://itunes.apple.com/us/app'))]
        if allAppLinks == previous_apps:
            break
        for appLink in allAppLinks:
            print(appLink)
            f.write(appLink + '\n')
        previous_apps = allAppLinks
        start_idx += 1


def getAllCategories(dump):
    if dump:
        f = open(DATA_DIR + '/' + DATA_APP_CAT_FILE, 'w')

    itunesStoreUrl = 'https://itunes.apple.com/us/genre/ios/id36?mt=8'
    mainPage = common.getPageAsSoup(itunesStoreUrl)
    allCategories = []
    total = 0
    for column in ['list column first', 'list column', 'list column last']:
        columnDiv = mainPage.find('ul', {'class': column})
        #print(columnDiv)
        for aDiv in columnDiv.findAll('a', href=re.compile('^https://itunes.apple.com/us/genre')):
            #print(aDiv)
            catUrl = aDiv.get('href')
            #title = aDiv.get('title')
            text = aDiv.string
            print(catUrl, text)
            if (text != "Games") & (text != "Newsstand"):
                if dump:
                    f.write(catUrl + ', ' + text + '\n')
                total += 1

    print("Total Categories: ", total)

    if dump:
        f.close()

def getApps(cat, dump):
    f = open(DATA_DIR + '/' + DATA_APP_CAT_FILE)
    for line in f:
        url = line.partition(',')[0]
        print(url)
        m = re.search('ios-(\w|-)+', url)
        appcat = m.group(0)
        print(appcat)
        if (len(cat) == 0) | ((len(cat) > 0) & (cat == appcat)):
            os.makedirs(DATA_DIR + '/' + appcat, 0o777, True)
            getAppsInCategory(cat, url, dump)

dump = 1

#getAllCategories(dump)
getApps("ios-weather", 1)

#getAppsInCategory("https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8")
#getPopAppsInCategory("https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8")
#getAppInCategoryWithLetter("https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8&letter=W")
