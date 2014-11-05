__author__ = 'sid'

import re

import common
from common import *
import datetime
from datetime import datetime

def getAppCharts(country, type):
    chartUrl = getChartUrl(country, type)
    chartFile = getChartFile(country, type)
    prefix = getApptUrlPrefix(country)
    section = getChartPageSection(country)

    date = datetime.now().strftime('%Y-%m-%d')
    f = open(DATA_DIR + "/" + chartFile + "_" + date, 'wb')
    mainPage = common.getPageAsSoup(chartUrl)
    total = 0
    appGrid = mainPage.find('section', {'class': section})
    i = 0
    for aDiv in appGrid.findAll('a', href=re.compile('^' + prefix)):
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
        title = img.get('alt')
        iconUrl = img.get('src')
        print(title, '\n', appUrl, '\n', iconUrl)
        str_out = title + '\n' + iconUrl + '\n' + appUrl + '\n'
        bytes_out = str_out.encode('utf-8')
        f.write(bytes_out)

    f.close()

def dumpChartsGlobal():
    getAppCharts('us', 'free')
    getAppCharts('us', 'paid')

def dumpChartsCN():
    getAppCharts('cn', 'free')
    getAppCharts('cn', 'paid')

if __name__ == "__main__":
    dumpChartsCN();
    dumpChartsGlobal()
    #putToDb()


