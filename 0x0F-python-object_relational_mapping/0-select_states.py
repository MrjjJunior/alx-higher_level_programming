#!/usr/bin/python3
''' lists all states from database '''
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database  = sys.argv[3]

    
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    
    cursor = db.cursor()

    
    cursor.execute("SELECT * FROM states")

    
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
