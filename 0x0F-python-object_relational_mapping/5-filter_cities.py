#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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


if __name__ == "__main__":
    main()
