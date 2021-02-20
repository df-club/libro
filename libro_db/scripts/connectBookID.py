#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

def connectDatabase(dbName="/home/lzhao-df/catkin_ws/src/libro/libro_db/bookID.db"):
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

def getPosByBookID(cursor,bookid):
    sql = "select * from bookId where bookId='" + bookid + "' AND isBorrowed='false'" 
    results = cursor.execute(sql)
    oneData = results.fetchone()
    print("bookName: " + oneData[2])
    sql = "select * from blockPosition where shelfId='" + oneData[3] + "' AND blockId='" + oneData[4] + "'"
    results = cursor.execute(sql)
    oneData = results.fetchone()
    return (oneData[3:7])

def getPosByBookIDFromDB(bookid):
    conn = connectDatabase()
    cursor = createCursor(conn)
    sql = "select * from bookId where bookId='" + bookid + "' AND isBorrowed='false'" 
    results = cursor.execute(sql)
    oneData = results.fetchone()
    print("bookId: " + oneData[1] + ', ' + "bookName: " + oneData[2])
    print("shelfId: " + oneData[3] + ', ' + "blockId: " + oneData[4])
    sql = "select * from blockPosition where shelfId='" + oneData[3] + "' AND blockId='" + oneData[4] + "'"
    results = cursor.execute(sql)
    oneData = results.fetchone()
    closeCursor(cursor)
    closeDatabase(conn)
    return (oneData[3:7])

def getPosByBookNameFromDB(bookname):
    conn = connectDatabase()
    cursor = createCursor(conn)
    sql = "select * from bookId where bookName='" + bookname + "' AND isBorrowed='false'" 
    results = cursor.execute(sql)
    oneData = results.fetchone()
    print("bookId: " + oneData[1] + ', ' + "bookName: " + oneData[2])
    print("shelfId: " + oneData[3] + ', ' + "blockId: " + oneData[4])
    sql = "select * from blockPosition where shelfId='" + oneData[3] + "' AND blockId='" + oneData[4] + "'"
    results = cursor.execute(sql)
    oneData = results.fetchone()
    closeCursor(cursor)
    closeDatabase(conn)
    return (oneData[3:7])

if __name__ == '__main__':
    conn = connectDatabase()
    cursor = createCursor(conn)
    # for i in searchDataByName(cursor,"bookId","bookName","红岩"):
    #     print (i[2])
    print(getPosByBookID(cursor, '110'))
    closeCursor(cursor)
    closeDatabase(conn)
