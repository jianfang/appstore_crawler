__author__ = 'sid'

import re

import common
from common import *

def getAppCharts():
    f = open(DATA_DIR + "/charts/top100_free_apps", 'w')

    chartUrl = 'http://www.apple.com/itunes/charts/free-apps/'
    mainPage = common.getPageAsSoup(chartUrl)
    total = 0
    appGrid = mainPage.find('section', {'class': 'section apps grid'})
    #print(appGrid)
    i = 0
    for aDiv in appGrid.findAll('a', href=re.compile('^https://itunes.apple.com/us/app')):
        if i == 0:
            i += 1
        elif i == 1:
            i += 1
            continue
        elif i == 2:
            i = 0
            continue

        #print(aDiv)
        appUrl = aDiv.get('href')
        img = aDiv.find('img')
        print(img)
        title = img.get('alt')
        iconUrl = img.get('src')
        #text = aDiv.string
        print(appUrl, title, iconUrl)
        f.write(title + '\n')
        f.write(iconUrl + '\n')
        f.write(appUrl + '\n')

    f.close()


if __name__ == "__main__":
    getAppCharts()
