#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

def query(ms, es):
    con = lite.connect('people.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM people WHERE marriage_status=? AND employment_status=? GROUP BY post_id ORDER BY click_count LIMIT 5"
            , (ms, es,))
        posts = ""
        rows = cur.fetchall()
        for row in rows:
            posts+=str(row)
        return posts
    con.close()

def increment_click_count(post_id):
    con = lite.connect('people.db')
    with con:
        cur = con.cursor() 
        cur.execute("UPDATE people SET click_count=click_count + 1 WHERE post_id=?" , (post_id,)) 
    con.close()


           #####