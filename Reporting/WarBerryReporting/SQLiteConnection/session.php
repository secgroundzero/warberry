<?php
header("Access-Control-Allow-Origin: *");
require('php/SQLiteWarberryConnection.php');
$sqlite=new SQLiteWarberryConnection();
$pdo = $sqlite->connect();
if ($pdo != null) {
    $sessions = $sqlite->getSessions();
    $response = array(
        "status" => "success",
        "sessions" => $sessions,
        "sessionsCount"=>count($sessions)
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