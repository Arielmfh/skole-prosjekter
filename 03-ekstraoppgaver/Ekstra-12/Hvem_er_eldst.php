<?php


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hvem er eldst</title>
</head>
<body>
    <h1>Hvem er eldst?</h1>
     <form action="resultat.php" method="POST">
     <h2>Person 1</h2>
     <label for="fornavn1">Fornavn</label>
     <input type="text" name="fornavn1" required>
     <label for="alder1">Alder</label>
     <input type="text" name="alder1" required>

     <h2>Person 2</h2>

     <label for="fornavn2">Fornavn</label>
     <input type="text" name="fornavn2" required>
     <label for="alder2">Alder</label>
     <input type="text" name="alder2" required>
     

     <input type="submit" name="submit1" value="Regn ut">

     </form>    



</body>
</html>