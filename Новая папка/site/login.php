<?php
    if (count($_POST) != 0){

$connection = mysqli_connect("localhost","root","","news"); 

$select = 'select Count(*) from users where login = "'.$_POST['login'].'" and password = "'.$_POST['password'].'"' ;

$count = mysqli_query($connection, $select);
$count = mysqli_fetch_array($count);

if ($count[0] == 1) {
    session_start();

    $_SESSION['login'] = $_POST['login']

  ?>

    <a href="index.php"><button class="btn btn-secondary">Вернуться на главную страницу</button></a>
  <?php die();
 } else { ?>
    <p> Неверный логин или пароль </p>
 <?php
    }
    
 }
?>

<!DOCTYPE html>
<html lang="en">
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Войти</title>
</head>
<body>
    <form action=""  method="post">
    <input type="text" name="login" placeholder="Логин" required> 
    <input type="text" name="password" placeholder="Пароль" required> 
    <input type="submit" value= "Войти">
       </form>

</body>
</html>