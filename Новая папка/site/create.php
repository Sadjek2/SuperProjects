<?php 

$connection = mysqli_connect("localhost","root","","news"); 

if (isset($_GET['id'])){
$select = "select * from news where id =".$_GET['id'];

$query = mysqli_query($connection, $select);
$row = mysqli_fetch_array($query);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Добавить новую новость </title>
</head>
<body> 
<div class="container">
    <?php if (!isset($_GET['id'])):?>
    <form action="_create.php"method="post">
        <input type="text" name="title" class="form-control" placeholder="Заголовок" required> <br>
        <textarea name="info" class="form-control rows="10" cols="20" placeholder="Информация" required ></textarea>
        <button type="submit" class="btn btn-secondary">Создать запись</button>
    </form>
    <?php else: ?>
        <form action="_update.php"method="post">
            <input type="text" name="title" class="form-control value="<?= $row['title'] ?>" placeholder="Заголовок" required> <br>
            <input type="hidden" name="id"  value="<?= $_GET['id'] ?>" placeholder="Заголовок" required> <br>
            <textarea name="info" class="form-control rows="10" cols="20" placeholder="Информация" required ><?= $row['info'] ?></textarea>
            <button type="submit" class="btn btn-secondary">Создать запись</button>
        </form>

    <?php endif; ?>
    </div class="container">
</body>
</html>