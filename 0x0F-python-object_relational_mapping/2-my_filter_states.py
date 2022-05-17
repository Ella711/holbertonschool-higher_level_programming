#!/usr/bin/python3
# Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(argv[4]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
