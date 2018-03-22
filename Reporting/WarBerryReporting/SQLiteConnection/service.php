<?php
header("Access-Control-Allow-Origin: *");
require('php/SQLiteWarberryConnection.php');
$sqlite=new SQLiteWarberryConnection();
$pdo = $sqlite->connect();
if ($pdo != null) {
    $session=$_GET["sessionID"];
    $service=$_GET["service"];
    $hosts = $sqlite->getHosts($session,$service);
    $response = array(
        "status" => "success",
        "hosts" => $hosts,
        "countHosts" => sizeof($hosts)
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