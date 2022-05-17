#!/usr/bin/python3
# Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cursor = conn.cursor()
    # HERE I have to know SQL to grab all states in my database
    sql_cmd = """
    SELECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name LIKE %s
    ORDER BY cities.id ASC
    """
    cursor.execute(sql_cmd, (argv[4], ))
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))
    cursor.close()
    conn.close()
