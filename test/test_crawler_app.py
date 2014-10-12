__author__ = 'sid'

import crawler_app
from crawler_app import *

if __name__ == "__main__":
    app_url = "https://itunes.apple.com/us/app/angry-birds/id343200656?mt=8"
    #app_url = "https://itunes.apple.com/us/app/isnowreport/id412841793?mt=8"
    #app_url = "https://itunes.apple.com/us/app/appzapp-hd-pro-daily-new-apps/id428248004?mt=8"
    #app_url = "https://itunes.apple.com/us/app/aar-planner/id583324413?mt=8"
    app_details = getAppDetails(app_url)
    print(app_details)

