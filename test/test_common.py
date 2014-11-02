__author__ = 'sid'

import common
from common import *

if __name__ == "__main__":
    print("Module common testing")
    appLongUrl = "https://itunes.apple.com/us/app/over/id535811906?mt=8&uo=4&v0=WWW-NAUS-ITSTOP100-PAIDAPPS&l=en"
    print("- app long url:", appLongUrl)
    print("- app id:", getAppId(appLongUrl))
    print("- app url:", getAppUrl("us", getAppId(appLongUrl)))


