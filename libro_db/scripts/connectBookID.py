#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def connectDatabase(dbName="bookID.db"):
    conn = sqlite3.connect(dbName)
    return conn
def createCursor(conn):
    cursor = conn.cursor()
    return cursor

def closeCursor(cursor):
    return cursor.close()

def closeDatabase(conn):
    return conn.close()

def selectAllByCursor(cursor,tableName = "bookId"):
    sql = "select * from " + tableName
    results = cursor.execute(sql)
    allRes = results.fetchall()
    return allRes

def selectOneByCursor(cursor,tableName = "bookId"):
    sql = "select * from " + tableName
    results = cursor.execute(sql)
    oneData = results.fetchone()
    return oneData

def searchDataByName(cursor,tableName,selectName,content):
    sql = "select * from " + tableName + " where " + selectName + " = '" + content + "'"
    results = cursor.execute(sql)
    allRes = results.fetchall()
    return allRes

if __name__ == '__main__':
    conn = connectDatabase()
    cursor = createCursor(conn)
    for i in searchDataByName(cursor,"bookId","bookName","红岩"):
        print (i)
    closeCursor(cursor)
    closeDatabase(conn)
