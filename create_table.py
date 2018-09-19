#!/usr/bin/python
# -*- coding:UTF-8 -*-

import MySQLdb
# from sql_connect_get import connect


def connectdb():
	db = MySQLdb.connect(host='localhost',user='root', passwd='2016',db='test')
	print 'mysql has connected!'
	return db

# build new table
def createtable(db):
	cursor = db.cursor()
	cursor.execute('drop table if exists employee')
	sql = '''create table employee(
			first_name  CHAR(20) NOT NULL,
        	last_name  CHAR(20),
        	age INT,  
        	sex CHAR(1),
        	income FLOAT )'''
	cursor.execute(sql)

# insert data into tables
def insertdb(db):
	cursor = db.cursor()

	sql_inser_1 = '''insert into employee(first_name,
							last_name, age, sex, income)
					values('li','lei','10','m','10000')'''
	sql_inser_2 = '''insert into employee(first_name,
							last_name, age, sex, income)
					values('hao','mei','15','w','100')'''
	sql_inser_3 = '''insert into employee(first_name,
							last_name, age, sex, income)
					values('zhang','san','25','m','500')'''



	try:
		cursor.execute(sql_inser_1)
		cursor.execute(sql_inser_2)
		cursor.execute(sql_inser_3)
		# commit to database and executing it
		db.commit()
	except:
		db.rollback()


# query tables info
def querydb(db):
	cursor = db.cursor()

	sql_describe='''select * from employee 
					where income >%d'''%(10)
	try:
		cursor.execute(sql_describe)
		results = cursor.fetchall()
		for row in results:
			fname = row[0]
			lname = row[1]
			age = row[2]
			sex = row[3]
			income = row[4]
			print 'fname=%s, lname=%s, age=%d,sex=%s,income=%d'%\
					(fname,lname,age,sex,income)

	except:
		print 'Error: unable to fetch data'


# update tabels info, depending critea
def updatedb(db):
	cursor = db.cursor()

	sql_update = "update employee set age=age+1 \
					where sex='%c'"%('m')
	try:
		cursor.execute(sql_update)
		db.commit()
	except:
		db.rollback()


# query tables info
def deletedb(db):
	cursor = db.cursor()
	
	sql_describe='''select * from employee 
				where income >%d'''%(10)

	# delect tables info:
	sql_delete = "delete from employee where age > '%d'"%(25)
	try:
		cursor.execute(sql_delete)
		db.commit()
	except Exception as e:
		print e, 'Error:unable to fetch data'


def closedb(db):
	db.close()


def main():
	db = connectdb()
	createtable(db)

	insertdb(db)
	print '---insert info after insert tables---:'
	querydb(db)

	updatedb(db)
	print '---update info---:'
	querydb(db)

	deletedb(db)
	print '---delete info---:'
	querydb(db)


	closedb(db)


if __name__ == '__main__':
	main()