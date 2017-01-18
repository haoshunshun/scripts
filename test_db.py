#!/usr/bin/python
#!-*- coding: utf-8 -*-
import MySQLdb

db = MySQLdb.connect(host="localhost",user="testuser",passwd="report123",db="report")
cursor = db.cursor()
sql = """CREATE TABLE hs-test (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1)
        INCOME FLOAT )"""
CURSOR.EXECUTE(sql)
db.close()
