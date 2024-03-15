#!/usr/bin/python3
''' list all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)

    cursor = db.cursor()
    match = sys.agrv[4]

    cursor.excute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    rows = cursor.fetchall()
    for row in rows:
        print (row)
    cursor.close()
    db.close()

