__author__ = 'sid'

import re
import string

import common


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


def getAppsInCategory(categoryUrl):
    for alphabet in string.ascii_uppercase:
        url = categoryUrl + '&letter=' + alphabet
        getAppInCategoryWithLetter(url)


def getAppInCategoryWithLetter(categoryUrl):
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
        previous_apps = allAppLinks
        start_idx += 1


def getAllCategories():
    itunesStoreUrl = 'https://itunes.apple.com/us/genre/ios/id36?mt=8'
    mainPage = common.getPageAsSoup(itunesStoreUrl)
    allCategories = []
    total = 0
    for column in ['list column first', 'list column', 'list column last']:
        columnDiv = mainPage.find('ul', {'class': column})
        #print(columnDiv)
        for aDiv in columnDiv.findAll('a', href=re.compile('^https://itunes.apple.com/us/genre')):
            #print(aDiv)
            cat = aDiv.get('href')
            #title = aDiv.get('title')
            text = aDiv.string
            print(cat, text)
            total += 1
        #allCategories.extend( aDiv.get( 'href' ) for aDiv in columnDiv.findAll( 'a', href = re.compile( '^https://itunes.apple.com/us/genre' ) ) )
    print("Total Categories: ", total)

#getAllCategories()
#getAppsInCategory("https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8")
getPopAppsInCategory("https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8")
#getAppInCategoryWithLetter("https://itunes.apple.com/us/genre/ios-weather/id6001?mt=8&letter=W")
