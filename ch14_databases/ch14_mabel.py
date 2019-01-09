#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import random
import datetime

############## CREATE TABLE & INSERT DATA ############## 

# connect() connects to the db, db file is input
conn = sqlite3.connect('task1.db')
c = conn.cursor()

def create_table():
    # execute() takes sql commands as input
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild(unix REAL , datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(142233222, '2019-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

############## INSERT DATA WITH VAR ############## 
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'python'
    value = random.randrange(0,10)
    c.execute('INSERT INTO stuffToBuild(unix, datestamp, keyword, value) VALUES (?,?,?,?)', (unix,date,keyword,value))
    conn.commit()

#for i in range(1):
#    dynamic_data_entry()
#    time.sleep(1)

def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value >4 ORDER BY 'value'')
    for row in c.fetchall():
#        test = row
        return row
#        print(row)

read_from_db_all()
c.close()
conn.close()

##############  ############## 
