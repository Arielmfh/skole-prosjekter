<?php
//Include
include 'Connect.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['submit'])) {
    if (isset($_POST['navn']) && isset($_POST['rase'])) {
        $navn = mysqli_real_escape_string($conn, $_POST['navn']);
        $rase = mysqli_real_escape_string($conn, $_POST['rase']);

        $sql = "INSERT INTO `dyr` (`navn`, `rase`) VALUES ('$navn','$rase')";
        $run_query = mysqli_query($conn, $sql);
    }
}
?>

<!DOCTYPE html>
<html lang="nb">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="./css/style.css" rel="stylesheet" type="text/css">
    <title>Resultat</title>
</head>
<body>
    <?php include 'Menu.php'; ?>
    <main>
        <header>
            <p>Status nytt kjæledyr</p>
        </header>
        <?php
        if($run_query)
        {
            echo '<p> Et nytt kjæledyr er lagt til!</p>';
        }
        else
        {
            echo '<p>Mislykket</p>';
        }
        ?>
    </main>
</body>
</html>
