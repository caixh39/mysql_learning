#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
# import pymysql 

# connecting database
def connect():
	db = MySQLdb.connect(host='localhost',user='root', passwd='2016',db='test')
	print 'mysql has connected!'
	return db


# getting cursor function getting control symbol
db = connect()
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()

print 'database version: %s'%data

# closing database
# db.close()