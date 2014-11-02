__author__ = 'sid'

import pickle

class AppUpdate:
    version = "1.0"
    updated = "01-01-2007"
    price = "Free"
    size = "1kb"
    whatsnew = "NA"


class App(object):
    # basic
    name = "app name"
    id = "000000000"
    category = "NA"
    description = "NA"
    seller = "NA"

    # extended
    rated = "NA"
    ratings_current = 0
    ratings_all = 0

    image = "NA"
    screenshots_iphone = []
    screenshots_ipad = []

    updates = []

    def serialize(self):
        fn = '../data/apps/000000000.pkl'
        with open(fn, 'w') as f:                     # open file with write-mode
            pickle_string = pickle.dump(self, f)
            #print(pickle_string)

#def genAppObject(appUrl)



