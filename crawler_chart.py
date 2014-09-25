__author__ = 'sid'

import re

import common
from common import *
import datetime
from datetime import datetime

CHARTS_URLS = ['http://www.apple.com/itunes/charts/free-apps/',
               'http://www.apple.com/itunes/charts/paid-apps/']
CHARTS_FILES = ['charts/top100_free_apps',
                'charts/top100_paid_apps']


def getAppCharts(chartUrl, chartFile):
    date = datetime.now().strftime('%Y-%m-%d')
    f = open(DATA_DIR + "/" + chartFile + "_" + date, 'w')
    mainPage = common.getPageAsSoup(chartUrl)
    total = 0
    appGrid = mainPage.find('section', {'class': 'section apps chart-grid'})
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

        # print(aDiv)
        appUrl = aDiv.get('href')
        img = aDiv.find('img')
        #print(img)
        title = img.get('alt')
        iconUrl = img.get('src')
        #text = aDiv.string
        print(title, appUrl, '\n', iconUrl)
        f.write(str(title.encode('utf8')))
        f.write('\n')
        f.write(iconUrl + '\n')
        f.write(appUrl + '\n')

    f.close()

# def putToDb():


if __name__ == "__main__":
    for u, file in zip(CHARTS_URLS, CHARTS_FILES):
        getAppCharts(u, file)

    #putToDb()


