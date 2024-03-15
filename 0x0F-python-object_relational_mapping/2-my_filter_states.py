#!/usr/bin/python3
''' displays all values in the states table of hbtn_0e_0_usa where name matches the argument '''
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database  = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            #s_search=state_searched
    )

    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name LIKE '{}'"

    cursor.execute(sql_query.format(state_searched))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
