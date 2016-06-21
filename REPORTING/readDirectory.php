<?php
$dir = $_GET["directory"];

$files=array();
// Open a directory, and read its contents
if (is_dir($dir)){
    if ($dh = opendir($dir)){
        while (($file = readdir($dh)) !== false){
            array_push($files, $file);
        }
        closedir($dh);
    }
}

$response=array(
    "status" => "success",
    "Files" => $files
);

echo json_encode($response);

