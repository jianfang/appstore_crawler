__author__ = 'sid'

import src.app
from src.app import *
import crawler_app
from crawler_app import *

if __name__ == "__main__":
    print("Module app testing")

    #appLongUrl = "https://itunes.apple.com/cn/app/kuang-zhan-san-guo2-zui-qiang/id880597078?mt=8&uo=4&v0=WWW-NAUS-ITSTOP100-PAIDAPPS&l=en"
    #appLongUrl = "https://itunes.apple.com/us/app/over/id535811906?mt=8&uo=4&v0=WWW-NAUS-ITSTOP100-PAIDAPPS&l=en"
    appLongUrl = "https://itunes.apple.com/us/app/over/id535811906?mt=8"
    app_detail = getAppDetails(appLongUrl)
    #print(appDetail)
    pickleApp(app_detail)

    print("pickle load")
    app = unpickleApp('535811906')
    print(app)


