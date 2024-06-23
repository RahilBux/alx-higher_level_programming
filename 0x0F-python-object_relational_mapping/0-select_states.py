#!/usr/bin/python3
"""Lists the states of USA"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf-8")
    curr = con.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_row = curr.fetchall()
    for row in query_row:
        print(row)
    curr.close()
    con.close()
