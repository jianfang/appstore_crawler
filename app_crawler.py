__author__ = 'sid'

from optparse import OptionParser

import crawler_category
from crawler_category import *
import crawler_app
from crawler_app import *


if __name__ == "__main__":
    print("=====================")
    print("  App store crawler")
    print("=====================")

    parser = OptionParser()
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")
    parser.add_option("-f", "--full_category",
                      action="store_true", dest="full_category", default=False,
                      help="get app categories")
    parser.add_option("-a", "--apps",
                      action="store_true", dest="apps", default=False,
                      help="get apps in categories")
    parser.add_option("-c", "--category",
                      dest="cat",
                      help="get app URLs in given category")
    parser.add_option("-d", "--cat_detail",
                      dest="cat_detail",
                      help="get app details in given category")

    (options, args) = parser.parse_args()

    print(options)

    if options.full_category == True:
        getAllCategories(0)

    if options.cat != None:
        getApps(options.cat, 1)

    if options.cat_detail != None:
        getAllAppData(options.cat_detail)


