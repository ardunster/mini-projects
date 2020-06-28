#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:50:50 2020

@author: adunster
"""

import psycopg2 as pg2

conn = pg2.connect(database="dvdrental", user='postgres',password='PGsudo')

cur = conn.cursor()

cur.execute('SELECT * FROM payment')

# print(cur.fetchone())
# print(cur.fetchmany(10))
# print(cur.fetchall())

conn.close()
