### 连接数据库
    conn = connectDatabase()
    cursor = createCursor(conn)
### 关闭连接
```
    closeCursor(cursor)
    closeDatabase(conn)
```
### 从某个表（默认是bookId）查询所有数据
```
    if __name__ == '__main__':
        conn = connectDatabase()
        cursor = createCursor(conn)

        for i in selectAllByCursor(cursor,"bookId"):
            print (i)
        closeCursor(cursor)
        closeDatabase(conn)
```
### 从某个表（默认是bookId）查询第一条数据
```
    if __name__ == '__main__':
        conn = connectDatabase()
        cursor = createCursor(conn)

        for i in selectOneByCursor(cursor,"bookId"):
            print (i)
        closeCursor(cursor)
        closeDatabase(conn)
```

### 从某个表查询某一列数据为xxx的记录
函数 searchDataByName(cursor,tableName,selectName,content)    
cursor 指传入的光标    
tableName 指要查询的表名    
selectName 指查询的列名    
content 指要查询的内容    
返回值：    
    所有符合条件的记录    
```
    if __name__ == '__main__':
        conn = connectDatabase()
        cursor = createCursor(conn)

        for i in searchDataByName(cursor,"bookId","bookName","红岩"):
            print (i)
        closeCursor(cursor)
        closeDatabase(conn)
```