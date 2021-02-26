<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Document</title>
   <script src="../src/js/include/jquery-3.5.1.min.js"></script>
</head>
<body>
<?php
   class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('../../libro_db/bookID.db');
      }
   }
   $db = new MyDB();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      echo "Opened database successfully<br><br>";
   }
   $sql =<<<EOF
   SELECT * from bookId;
EOF;

$ret = $db->query($sql);
echo "<table border='1'><tr><td>书籍编号</td><td>书籍名称</td><td>该种书籍内编号</td><td>操作</td></tr>";
while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
   echo "<tr><td>". $row['bookId'] . "</td>";
   echo "<td> ". $row['bookName'] ."</td>";
   echo "<td> ". $row['bookArr'] ."</td>";
   echo "<td><button class='getBook' bookId=".$row['bookId'] ." >Get it!</button></td></tr>";
}
echo "</table>";
echo "Operation done successfully";
?>
<div class='bookStatus'></div>
</body>
<script>
   var btns = document.getElementsByClassName('getBook')
      for (var i = 0, len = btns.length; i < len; i++) {
      　　var btn = btns[i]
      　　btn.onclick = function () {
      　　　　var bookId = this.getAttribute("bookId");
                        var btnThis = this;
                        $.ajax({url:"./borrow.php?bookId="+bookId,success:function(result){
                              $(".bookStatus").html("success");
                        }});
      　　}
      }
</script>
</html>
