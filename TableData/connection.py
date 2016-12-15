import csv
import psycopg2
import getpass
import datetime

def readFromFile(filename):
    file = open(filename)
    dataStoreage = csv.DictReader(file)
    data = []
    for x in dataStoreage:
    	data.append(x)
    file.close()
    return data

def connectToDatabase():
    host = 'localhost'
    #dbname = input('Database name: ')
    #username = input('User name for {}.{}: '.format(host,dbname))
    dbname = 'moondata'
    username = 'postgres'
    pw = 'postgres'


    #pw = getpass.getpass()
    #pw = input('pw: ')

    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

    print("Connecting to database {}.{} as {}".format(host, dbname, username))

    try:
        conn = psycopg2.connect(conn_string)
    except psycopg2.OperationalError as e:
        print('Connection failed!')
        print('Error message:', e)
        exit()

    cursor = conn.cursor()
    print("Connected!\n")

    return cursor, conn
