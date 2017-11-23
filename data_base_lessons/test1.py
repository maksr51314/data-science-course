#!/usr/bin/python

hostname = 'localhost'
username = 'patrick'
password = '1111'
database = 'super_awesome_application'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    # print(conn)
    cur.execute( "SELECT * FROM books" )
    for el in cur.fetchall() :
        print(el)


# print("Using psycopg2")
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()

# print("Using PyGreSQL")
# import pgdb
# myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
# doQuery( myConnection )
# myConnection.close()