<?php
require('Config.php');
/**
 * SQLite connnection
 */
class SQLiteWarberryConnection
{
    /**
     * PDO instance
     * @var type
     */
    private $pdo;

    /**
     * return in instance of the PDO object that connects to the SQLite database
     * @return \PDO
     */
    public function connect()
    {
        if ($this->pdo == null) {
            try {
                //$this->pdo = new \PDO("jdbc:sqlite:" . Config::PATH_TO_SQLITE_FILE);
                $this->pdo = new \PDO("sqlite:" . Config::PATH_TO_SQLITE_FILE);
                return $this->pdo;
            } catch (\PDOException $e) {
                echo $e;
                return null;
            }
        } else {
            return $this->pdo;
        }
    }

    public function getSessions()
    {

        $stmt = $this->pdo->query('SELECT * FROM warberry_session ');
        $sessions = array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $session["sessionID"]=$row["WarberrySessionID"];
            $session["WarBerryID"] = $row['WarberryID'];
            $session["StartTime"] = $row["WarberryStart"];
            $session['EndTime'] = $row["WarberryEnd"];
            $session["Status"] = $row["WarberryStatus"];
            array_push($sessions,$session);
        }
        return $sessions;
    }

    public function getSessionInfo($warberrySession)
    {
        $stmt = $this->pdo->query("SELECT * FROM warberry_session WHERE WarberrySessionID='$warberrySession'");
        $sessionInfo = array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $sessionInfo["sessionID"]= $row["WarberrySessionID"];
            $sessionInfo["WarBerryID"] = $row['WarberryID'];
            $sessionInfo["StartTime"] = $row["WarberryStart"];
            $sessionInfo["EndTime"] = $row["WarberryEnd"];
            $sessionInfo["Status"] = $row["WarberryStatus"];
        }
        return $sessionInfo;
    }
    
    public function getCommonInfo($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM common_war_info WHERE WarberrySession='$warberrySession'");
        $commonInfo=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
                $commonInfo['commonID'] = $row["WarberryCommonID"];
                $commonInfo['WarberrySession'] = $row['WarberrySession'];
                $commonInfo['CIDR'] = $row["CIDR"];
                $commonInfo['Netmask'] = $row["netmask"];
                if ($row["internal_IP"]==null){
                    $commonInfo['InternalIP'] = "N/A";
                }
                else{
                    $commonInfo['InternalIP'] = $row["internal_IP"];
                }
                if ($row["external_ip"]==null){
                    $commonInfo['ExternalIP']="N/A";
                }
                else{
                    $commonInfo['ExternalIP']=$row["external_ip"];
                }

        }
        return $commonInfo;
    }

    public function getWifis($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_wifis WHERE WarberrySession='$warberrySession'");
        $wifis=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $w=array();
            $w['wifiID'] =$row["Warberry_wifiID"];
            $w['WarberrySession'] = $row['WarberrySession'];
            $w['WifiName'] = $row["wifiName"];
            array_push($wifis, $w);
        }
        return $wifis;
    }

    public function getBlues($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_blues WHERE WarberrySession='$warberrySession'");
        $blues=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $blue=array();
            $blue['blueID'] = $row["Warberry_blueID"];
            $blue['WarberrySession'] = $row['WarberrySession'];
            $blue['blueName'] = $row["blueName"];
            $blue['blueDevice'] =$row["blueDevice"];
            array_push($blues,$blue);
        }
        return $blues;
    }

    public function getIPS($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_ips WHERE WarberrySession='$warberrySession'");
        $ips=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $ip=array();
            $ip['ipID'] = $row["WarberryIPID"];
            $ip['WarberrySession'] = $row['WarberrySession'];
            $ip['ip'] = $row["ip"];
            array_push($ips, $ip);
        }
        return $ips;
    }

    /*public function getOS($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_os WHERE WarberrySession='$warberrySession'");
        $os=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $os=array();
            $o['osID'] = $row["WarberryOSID"];
            $o['WarberrySession'] = $row['WarberrySession'];
            $o['os'] = $row["os"];
            array_push($os, $o);
        }
        return $os;
    }

    public function getDomains($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_domain WHERE WarberrySession='$warberrySession'");
        $domains=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $dom=array();
            $dom['domainID'] = $row["WarberryDomainID"];
            $dom['WarberrySession'] = $row['WarberrySession'];
            $dom['domain'] = $row["domain"];
            array_push($domains, $dom);
        }
        return $domains;
    }*/

    /*public function getHostnames($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_hostnames WHERE WarberrySession='$warberrySession'");
        $hostnames=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $host=array();
            $host['hostnameID'] = $row["WarberryHostnamesID"];
            $host['WarberrySession'] = $row['WarberrySession'];
            $host['hostname'] = $row["hostname"];
            array_push($hostnames, $host);
        }
        return $hostnames;
    }*/

    public function getScanners($warberrySession){
        $stmt = $this->pdo->query("SELECT * FROM war_scanners WHERE WarberrySession='$warberrySession'");
        $scanners=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $scanner=array();
            $scanner['scannerID'] = $row["WarberryScannerID"];
            $scanner['WarberrySession'] = $row['WarberrySession'];
            $scanner['name'] = $row["scannerName"];
            $scanner['host'] =$row["host"];
            array_push($scanners, $scanner);
        }

        $scannerNames=array();
        $scannerKeys=array();
        foreach ($scanners as $scanner) {
            $key = $scanner["name"];
            if (array_key_exists($key, $scannerNames)) {
                array_push($scannerNames[$key], $scanner["host"]);
            }
            else{

                $scannerNames[$key]=array();
                array_push($scannerNames[$key], $scanner["host"]);
                array_push($scannerKeys, $key);

            }
        }
        return $scannerKeys;
    }

    public function getHosts($warberrySession, $service){
        $stmt = $this->pdo->query("SELECT * FROM war_scanners WHERE WarberrySession='$warberrySession' AND scannerName='$service'");
        $scanners=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            array_push($scanners,$row["host"]);
        }

        return $scanners;
    }


    public function getServices( $warberrySession, $ip){
        $stmt = $this->pdo->query("SELECT * FROM war_scanners WHERE WarberrySession='$warberrySession' AND host='$ip'");
        $services=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            array_push($services,$row["scannerName"]);
        }
        return $services;
        
    }
    
    public function hostnameInfo($warberrySession, $ip){
        $stmt=$this->pdo->query("SELECT * FROM war_hostnames WHERE WarberrySession='$warberrySession' AND hostname_IP=='$ip'");
        $hostnames=array();
        $hostname=array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $hostname["name"]=$row["hostname"];
            $hostname["domain"]=$row["hostname_domain"];
            $hostname["os"]=$row["hostname_os"];
            array_push($hostnames, $hostname);
        }
        return $hostnames;
    }
    
    public function getWarberry()
    {
        $stmt = $this->pdo->query('SELECT * FROM warberry ');
        $warberry = array();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $warberry['WarBerryID'] = $row["WarBerryID"];
            $warberry['WarBerryName'] = $row['WarBerryName'];
            $warberry['WarBerryModel'] = $row["WarBerryModel"];
        }
        return $warberry;
    }

    public function getHashes($warberrySession){
        $stmt=$this->pdo->query("SELECT * FROM war_hashes WHERE WarberrySession='$warberrySession'");
        $hashes=[];
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $hash=array();

            $str= str_replace("[0;33m", "", $row["client"]);
            $str=str_replace("[0m", "", $str);
            $hash['ip'] =$str;
            $str=str_replace("[1;34m", "",$row['username']);
            $str=str_replace("[0m", "", $str);
            $str=str_replace("[0;33m", "", $str);
            $hash['username'] = $str;
           $str= str_replace("[0;33m", "",  $row["hash"]);
            $str=str_replace("[1;34m", "",$str);
            $str=str_replace("[0m", "", $str);
            $hash['hash'] =$str;

            array_push($hashes,$hash);
        }
        return $hashes;
    }
    
}

