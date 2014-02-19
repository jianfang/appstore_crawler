__author__ = 'sid'

#mongo.py
#
import pymongo

con = pymongo.Connection('192.168.56.50', 27017)

mydb = con.mydb # new a database
mydb.add_user('test', 'test') # add a user
mydb.authenticate('test', 'test') # check auth
muser = mydb.user # new a table

muser.save({'id':1, 'name':'test'}) # add a record
muser.insert({'id':2, 'name':'hello'}) # add a record
muser.find_one() # find a record
muser.find_one({'id':2}) # find a record by query
muser.create_index('id')
muser.find().sort('id', pymongo.ASCENDING) # DESCENDING

# muser.drop() delete table
muser.find({'id':1}).count() # get records number
muser.find({'id':1}).limit(3).skip(2) # start index is 2 limit 3 records
muser.remove({'id':1}) # delet records where id = 1
muser.update({'id':2}, {'$set':{'name':'haha'}}) # update one recor

#end of mongo.py
