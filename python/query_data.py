#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('people.db')

def query(marriage_status, employment_status):
    with con:   
        cur = con.cursor()    
        cur.execute("SELECT * FROM people WHERE marriage_status = " + marriage_status +
                    " AND employment_status = " + employment_status + " ORDER BY click_count LIMIT 5")
        rows = cur.fetchall()
        for row in rows:
        	print row


con.close()