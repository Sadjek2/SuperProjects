<?php

$connection = mysqli_connect("localhost","root","","news"); 

$delete = 'delete from news where id ='.$_GET['id'] ;

if (mysqli_query($connection,$delete) == true) {
    ?>
      <a href="index.php"><button class="btn btn-secondary">Вернуться на главную страницу</button></a>
    <?php
   } else {
          echo "Ошибка в выполнении запроса";
      }
  