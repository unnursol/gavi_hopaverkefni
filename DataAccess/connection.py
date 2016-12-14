import psycopg2
import getpass

host = 'localhost'
dbname = input('Database name: ')
username = input('User name for {}.{}: '.format(host,dbname))

#pw = getpass.getpass()
pw = input('pw: ')

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


# Do something here...

cursor.close()
conn.close()
