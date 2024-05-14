<?php
$Fornavn1 = $_POST["fornavn1"];
$Alder1 = $_POST["alder1"];
$Fornavn2 = $_POST["fornavn2"];
$Alder2 = $_POST["alder2"];

$AldersForskjell1 = $Alder1 - $Alder2;
$Aldersforskjell2 = $Alder2 - $Alder1;


# $resultat = "";

/*
if ($Alder2 < $Alder1) 
    echo $Fornavn1," er eldre enn ",$Fornavn2," med ",$AldersForskjell1," år!";
elseif ($Alder1 < $Alder2)
    echo $Fornavn2," er eldre enn ",$Fornavn1," med ",$Aldersforskjell2," år!";
elseif ($Alder1 == $Alder2)
    echo "De er like gamle!"; */

/* echo $Fornavn1;
echo $Alder1;
echo $Fornavn2;
echo $Alder2; */
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultat av Regning</title>
</head>
<body>

    <h1><?php if ($Alder2 < $Alder1) 
    echo $Fornavn1," er eldre enn ",$Fornavn2," med ",$AldersForskjell1," år!";
    echo $Alder1," - ",$Alder2;
    ?></h1>
    <h1><?php if ($Alder1 < $Alder2) 
    echo $Fornavn2," er eldre enn ",$Fornavn1," med ",$Aldersforskjell2," år!";
    echo $Alder2," - ",$Alder1;
    ?></h1>
    <h1><?php if ($Alder2 == $Alder1) 
    echo "De er like gamle!";
    ?></h1>
    
</body>
</html>