__author__ = 'sid'

import src.app
from src.app import *
import crawler_app
from crawler_app import *

if __name__ == "__main__":
    print("Module app testing")
    #app = App()
    #print(app)
    #app.serialize()

    entry = {}
    entry['title'] = 'Dive into history, 2009 edition'
    entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-200'
    entry['comments_link'] = None
    entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
    entry['tags'] = ('diveintopython', 'docbook', 'html')
    entry['published'] = True
    import time
    entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')
    entry['published_date']

    appLongUrl = "https://itunes.apple.com/us/app/over/id535811906?mt=8&uo=4&v0=WWW-NAUS-ITSTOP100-PAIDAPPS&l=en"
    appDetail = getAppDetails(appLongUrl)
    print(appDetail)
    with open('../data/apps/000000000.pkl', 'wb') as f:
        pickle.dump(appDetail, f)



