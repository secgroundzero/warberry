<?php
header("Access-Control-Allow-Origin: *");
require('php/SQLiteWarberryConnection.php');
$sqlite=new SQLiteWarberryConnection();
$pdo = $sqlite->connect();
if ($pdo != null) {
    $session=$_GET["sessionID"];
    $ip=$_GET["ip"];
    $hostnames = $sqlite->hostnameInfo($session,$ip);
    $scanners=$sqlite->getServices($session, $ip);
    $response = array(
        "status" => "success",
        "hostnames" => $hostnames,
        "scanners" => $scanners
    );
}
else {
    $response = array(
        "status" => "fail",
        "message" => "Could not connect to the SQLite Database"
    );
}

header('Content-type: application/json');
echo json_encode($response);