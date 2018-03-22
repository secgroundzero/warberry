<?php
header("Access-Control-Allow-Origin: *");
require('php/SQLiteWarberryConnection.php');
$sqlite=new SQLiteWarberryConnection();
$pdo = $sqlite->connect();
if ($pdo != null) {
    $session=$_GET["session"];
    $sessions= $sqlite->getSessions();
    $sessionInfo = $sqlite->getSessionInfo($session);
    $commonInfo = $sqlite->getCommonInfo($session);
    $wifis=$sqlite->getWifis($session);
    $blues=$sqlite->getBlues($session);
    $ips=$sqlite->getIPS($session);
    $scanners=$sqlite->getScanners($session);
    $hashes=$sqlite->getHashes($session);
    $response = array(
        "status" => "success",
        "sessions" => $sessions,
        "countSessions" =>count($sessions),
        "session" => $sessionInfo,
        "common" => $commonInfo,
        "wifis" => $wifis,
        "countWifis" => count($wifis),
        "blues" => $blues,
        "countBlues" => count($blues),
        "ips" => $ips,
        "countIPS" => count($ips),
        "scanners" => $scanners,
        "countScanners" => count($scanners),
        "hashes" => $hashes,
        "countHashes"=>count($hashes)
    );
}
else {
    $response = array(
        'status' => 'fail',
        'message' => 'Could not connect to the SQLite Database'
    );
}

header('Content-type: application/json');

echo json_encode($response);
?>