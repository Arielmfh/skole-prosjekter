<?php

// Henter connect.php
include 'Connect.php';

//Prosedyren
$sql_read = "SELECT kjnr, rase, navn FROM dyr";

$sql_read = mysqli_query($conn, $sql_read);
$dyr = mysqli_fetch_all($sql_read, MYSQLI_ASSOC);

// foreach($dyr as $kjaeledyr)
//   {
//     echo "<br>".$kjaeledyr['navn'];
//   }

mysqli_free_result($sql_read);
mysqli_close($conn);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="./css/style.css" rel="stylesheet" type="text/css">
    <title>Read</title>
</head>
<body>
    <?php
    include 'Menu.php';
    ?>
    <main>
        <table>
            <thead>
                <tr>
                    <th>Kjnr</th>
                    <th>Rase</th>
                    <th>Navn</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach($dyr as $kjaeledyr)
                { ?>
                <tr>
                    <td><?php echo $kjaeledyr['kjnr']; ?></td>
                    <td><?php echo $kjaeledyr['rase']; ?></td>
                    <td><?php echo $kjaeledyr['navn']; ?></td>
                </tr>
                <?php } ?>
            </tbody>
        </table>
    </main>

    

</body>
</html>