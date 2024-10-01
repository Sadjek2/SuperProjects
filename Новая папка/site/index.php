<?php

session_start();

$connection = mysqli_connect("localhost","root","","news"); 

$select = "select * from news inner join users where users_id = users.id";

$query = mysqli_query($connection, $select);

// while ($row = mysqli_fetch_array($query)) {
//     echo $row["title"] ."<br>";   
//     echo $row["info"] ."<br><br>";
// }

//var_dump(mysqli_fetch_array($query));
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Новости ТОП</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body class="bg-dark" >

        <div class="container bg-white">
        <?php if (isset($_SESSION['login'])): ?>
        <a href="create.php"><button class="btn btn-primary"> Добавить</button></a>

        <?php endif ?>
        <?php if (isset($_SESSION['login'])): ?>
            <a href="logout.php"><button class="btn btn-danger">Выйти</button></a>
            <?php else: ?>
        <a href="login.php"><button" class="btn btn-primary">Войти</button></a>

        <a href="register.php"><button class="btn btn-danger">Регистрация</button></a>
        <?php endif ?>
    <h1 align="center">Новости</h1>
    <hr> 

    <?php while ($row = mysqli_fetch_array($query)): ?>
        <h3><?= $row ["title"] ?></h3>
        <p><?= $row ["info"] ?></p>
        <p style="font-size: 10px;">Автор <?= $row['login'] ?></p>
        


        <?php if (isset($_SESSION['login']) and $_SESSION['login'] == $row ['login']): ?>
        
        <a href="create.php?id=<?= $row[0] ?>"><button class="btn btn-success">Изменить</button></a>
        <?php endif ?>

        <?php if (isset($_SESSION['login']) and $_SESSION['login'] == $row ['login']): ?>
        <a href="delete.php?id=<?= $row[0] ?>"><button class="btn btn-danger">Удалить</button></a>
        <?php endif ?>

        <hr>
    <?php endwhile; ?>

    <div class="container">
  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <p class="col-md-4 mb-0 text-body-secondary">© 2024 Company, Inc</p>

    <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
      <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"></use></svg>
    </a>
    <img src="logo.png" width="100" height="" alt="10">  
    <ul class="nav col-md-4 justify-content-end">
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Home</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Features</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">Pricing</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">FAQs</a></li>
      <li class="nav-item"><a href="#" class="nav-link px-2 text-body-secondary">About</a></li>
    </ul>
  </footer>
</div>

</body>
</html>