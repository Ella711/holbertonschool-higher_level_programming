#!/usr/bin/python3
"""
Same as task2 but is safe from MySQL injections
"""

import MySQLdb
from sys import argv


def main():
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cursor.execute("""SELECT * FROM states
    WHERE name = %(name)s
    ORDER BY id ASC""", {'name': argv[4]})
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
