#!/usr/bin/python3
"""
# Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv


def main():
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM states
    WHERE name LIKE '{:s}'
    ORDER BY id ASC""".format(argv[4]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
