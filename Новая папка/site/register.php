<?php
    if (count($_POST) != 0){
        $connection = mysqli_connect("localhost","root","","news"); 

        $select = 'select * from users where login = "'.$_POST ['login'].'"';
   
        $rezult = mysqli_fetch_array(mysqli_query($connection, $select ));

        if ($rezult ==  null) {
 
            $insert = 'insert into users(login,password) values("'.$_POST['login'].'","'.$_POST['password'].'")';

            mysqli_query($connection, $insert);

            session_start();
        
            $_SESSION['login'] = $_POST['login'];
        
          ?>
            <a href="index.php"><button>Вернуться на главную страницу</button></a>
          <?php die();
         } else { ?>
            <p> Данный логин уже существует </p>
         <?php
 }
            
 }
?>
<!DOCTYPE html>
<html lang="en">
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация</title>
</head>
<body>
    <form action="" method= "post">
    <input type="text" name="login" placeholder="Логин" required> 
    <input type="text" name="password" placeholder="Пароль" required> 
    <button type="submit">Зарегистрироваться</button>
</form>
</body>
</html>