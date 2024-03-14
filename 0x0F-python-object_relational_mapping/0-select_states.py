#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    #connection param
    username = sys.argv[1]
    password = sys.argv[2]
    database  = sys.argv[3]

    #connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    #Cursor object
    cursor = db.cursor()

    #excute SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #get and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
