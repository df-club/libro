# libro_db包说明

## 包功能
1. 包含图书及位置信息的sqlite的数据库系统
2. 数据库相关增删改查操作的程序实现

## 数据库结构
数据库名：bookID.db

表信息：
- bookId：用于存储书籍的相关信息
- blockPosition：用于存储书架、块位置等信息

表：bookId
- Id：数据表中的编号，每本书有一个唯一的Id
- bookId：书籍的编号，每种书有唯一bookId，每种书可能有多本，例如图书馆中存有2本《西游记》，这两本《西游记》的bookId相同，Id则不同
- bookName：书名
- shelfId：书架编号
- blockId：块编号，每个书架分为多个块，方便查找
- isBorrowed：是否已借出
- bookArr：每种书中每本的编号

表：blockPosition
- id：编号
- shelfId：书架编号
- blockId：块编号
- posX：块所在的位置X
- posY：块所在的位置Y
- posZ：块所在的位置Z
- theta：块的朝向，用于确定机器人的位姿

## 使用方法
1. 需安装sqlite: sudo apt install sqlite3
2. 数据库管理软件（选装）：DBeaver
3. 数据库操作：
