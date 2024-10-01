<?php

session_start();

$connection = mysqli_connect("localhost","root","","news"); 

$select = 'select * from users where login ="'.$_SESSION['login'].'"';

$rezult = mysqli_query($connection, $select);

$rezult = mysqli_fetch_array($rezult);

$insert = 'insert into news(title,info,users_id) values("'.$_POST['title'].'","'.$_POST['info'].'",'.$rezult['id'].')';

if (mysqli_query($connection,$insert) == true) {
  ?>
    <a href="index.php"><button class="btn btn-secondary">Вернуться на главную страницу</button></a>
  <?php
    exit;
 } else {
        echo "Ошибка в выполнении запроса";
    }
