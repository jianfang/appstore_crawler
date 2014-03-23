__author__ = 'sid'

import pymongo

if __name__ == "__main__":
    con = pymongo.Connection('192.168.56.50', 27017)

    appdb = con.appdb # new a database
    appdb.add_user('test', 'test') # add a user
    appdb.authenticate('test', 'test') # check auth
    muser = appdb.user # new a table
    muser.insert({'title': 'A$$hole (by Martin Kihn)', 'rating': 'N/A',
                  'app_url': 'https://itunes.apple.com/us/app/a$$hole-by-martin-kihn/id389377362?mt=8'})
