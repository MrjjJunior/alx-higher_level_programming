#!/usr/bin/python3
''' lists states name start with N  '''
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

    sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(sql_query, (state_searched,3-my_safe_filter_states.py))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
