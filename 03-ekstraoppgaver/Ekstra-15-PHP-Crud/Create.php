<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="./css/style.css" rel="stylesheet" type="text/css">
    <title>Nytt kjæledyr</title>
</head>
<body>
    <?php include 'Menu.php'; ?>
    <main> 
        <form action="Result.php" method="post">
            <label for="navn">Navn</label> <br>
             <input type="text" name="navn" id="navn" required> <br>

             <label for="rase">Rase</label> <br>
             <input type="text" name="rase" id="rase" required> <br>

             <input type="submit" name="submit" id="submit" value="Registrer"> <br> <br>
        </form>
    </main>
</body>
</html>