#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
db = MySQLdb.connect(host="localhost",user="haoshun",passwd="shun123",db="TESTDB")
cursor = db.cursor()
sql = """CREATE TABLE CRID (
         CREATIVEID  CHAR(20) NOT NULL,
         BIDS INT )"""
cursor.execute(sql)
db.close()
