import csv
import datetime
import psycopg2
import getpass
import time

def connect_to_database(host, dbname, username, pw):
    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

    try:
        conn = psycopg2.connect(conn_string)
    except psycopg2.OperationalError as e:
        print('Connection failed!')
        print('Error message:', e)
        exit()

    cursor = conn.cursor()

    print("Connected!\n")

    return cursor, conn

cursor, conn = connect_to_database('localhost','moondata','postgres','postgres')


numberofrowstoinsert = 2000
counter = 0

insertstring = "insert into crimes (time, offense) values "
values = []

file = open('Crimes_-_2001_to_present.csv')

dataStoreage = csv.DictReader(file) 

data = []
for x in dataStoreage:
	data.append(x)

file.close()


for i in data:
    values.append((int(datetime.datetime.strptime(i['time'], "%m/%d/%Y %I:%M:%S %p").timestamp()), i['offense']))

args_str = b','.join(cursor.mogrify("(%s,%s)", x) for x in values)
cursor.execute(insertstring + args_str.decode('utf-8'))


conn.commit()
cursor.close()
conn.close()

