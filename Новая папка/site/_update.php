<?php

$connection = mysqli_connect("localhost","root","","news"); 

$insert = 'update news
           set title = "'.$_POST['title'].'", info = "'.$_POST['info'].'"
           where id ='.$_POST['id'];

if (mysqli_query($connection,$insert) == true) {
  ?>
    <a href="index.php"><button class="btn btn-secondary">Вернуться на главную страницу</button></a>
  <?php
    exit;
 } else {
        echo "Ошибка в выполнении запроса";
    }
