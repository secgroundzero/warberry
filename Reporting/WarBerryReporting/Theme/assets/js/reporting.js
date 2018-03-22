var connectService = 'http://localhost/Reporting/WarberryReporting/SQLiteConnection/reporting.php';
var sessionID=findSession();
if (sessionID==-1){
    console.log("No sessions found");
}
else{
    var param = {session: sessionID};
}

$.ajax({
    type: "GET",
    url: connectService,
    beforeSend: function (req) {
        req.setRequestHeader("Accept", "application/json");
    },
    data: param,
    success: function(result){
        var response=result;
    
        if (response.status.indexOf("success")>=0) {
            
            //Sessions 
            var countS=response.sessions.length;
            var sessionsElement=document.getElementById("external-events");
            sessionsElement.className="display";
            sessionsElement.innerHTML="";
            for (var i=0; i<countS; i++){
                var sessionID=response.sessions[i].sessionID;
                var functionName="showSessionReporting("+sessionID+")";
                var hyperlink=document.createElement('a');
                hyperlink.setAttribute("onclick", functionName);
                hyperlink.style.color= "#ffffff";
                hyperlink.style.backgroundColor="#353535";
                var UTime=convert(response.sessions[i].StartTime);
                var hyperlink_text=document.createTextNode(UTime);
                hyperlink.appendChild(hyperlink_text);
                var divEl=document.createElement('div');
                divEl.className="external-event";
                divEl.style.background="#1f1f1f";
                divEl.setAttribute("style", "position:relative");
                divEl.appendChild(hyperlink);
                sessionsElement.appendChild(divEl);
            }
            //Session Info
            var sessionInfo=document.getElementById("SessionInfo");
            sessionInfo.innerHTML="";
            var tableSession=document.createElement("table");
            tableSession.className="display";
            var tbodySession=document.createElement("tbody");
            var rowStart=document.createElement("tr");
            rowStart.className="odd";
            var cellStart=document.createElement("td");
            var rowEnd=document.createElement("tr");
            rowEnd.className="odd";
            var cellEnd=document.createElement("td");
            var rowStatus=document.createElement("tr");
            rowStatus.className="odd";
            var cellStatus=document.createElement("td");
            startT=convert(response.session.StartTime);
            endT=convert(response.session.EndTime);
            var start_text=document.createTextNode("StartTime:\t"+ startT);
            var end_text=document.createTextNode("EndTime:\t"+ endT);
            var status_text=document.createTextNode("Status:\t"+ response.session.Status);
            cellStart.appendChild(start_text);
            cellEnd.appendChild(end_text);
            cellStatus.appendChild(status_text);
            rowStart.appendChild(cellStart);
            rowStart.setAttribute("style", "height:40px");
            rowEnd.appendChild(cellEnd);
            rowEnd.setAttribute("style", "height:40px");
            rowStatus.appendChild(cellStatus);
            rowStatus.setAttribute("style", "height:40px");
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
            }
            tbodySession.appendChild(rowStart);
            tbodySession.appendChild(rowEnd);
            tbodySession.appendChild(rowStatus);
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
                row.appendChild(cell);
                tbodySession.appendChild(row);
            }
            tableSession.appendChild(tbodySession);
            sessionInfo.appendChild(tableSession);

            //Common Info
            var commonInfo=document.getElementById("CommonInfo");
            commonInfo.innerHTML="";
            var tableSession=document.createElement("table");
            tableSession.className="display";
            var tbodySession=document.createElement("tbody");
            var rowCIDR=document.createElement("tr");
            rowCIDR.className="odd";
            var cellCIDR=document.createElement("td");
            var rowInternalIP=document.createElement("tr");
            rowInternalIP.className="odd";
            var cellInternalIP=document.createElement("td");
            var rowExternalIP=document.createElement("tr");
            rowExternalIP.className="odd";
            var cellExternalIP=document.createElement("td");
            var CIDR_text=document.createTextNode("CIDR:\t"+ response.common.CIDR);
            var InternalIP_text=document.createTextNode("Internal IP:\t"+ response.common.InternalIP);
            var External_text=document.createTextNode("External IP:\t"+ response.common.ExternalIP);
            cellCIDR.appendChild(CIDR_text);
            cellInternalIP.appendChild(InternalIP_text);
            cellExternalIP.appendChild(External_text);
            rowCIDR.appendChild(cellCIDR);
            rowCIDR.setAttribute("style", "height:40px");
            rowInternalIP.appendChild(cellInternalIP);
            rowInternalIP.setAttribute("style", "height:40px");
            rowExternalIP.appendChild(cellExternalIP);
            rowExternalIP.setAttribute("style", "height:40px");
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
            }
            tbodySession.appendChild(rowCIDR);
            tbodySession.appendChild(rowInternalIP);
            tbodySession.appendChild(rowExternalIP);
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
                row.appendChild(cell);
                tbodySession.appendChild(row);
            }
            tableSession.appendChild(tbodySession);
            commonInfo.appendChild(tableSession);
            

            //Wifis Info
            var wifiInfo=document.getElementById("WifisInfo");
            wifiInfo.innerHTML="";
            var tableWifis=document.createElement("table");
            tableWifis.className="display";
            var tbodyWifis=document.createElement("tbody");
            var countWifis=response.countWifis;
            if (countWifis>0){
                for (var i=0; i<countWifis; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.wifis[i].WifiName);
                    column1.appendChild(column1_text);
                    row.appendChild(column1);
                    tbodyWifis.appendChild(row);
                }
                for (var i=countWifis; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyWifis.appendChild(row);
                }
                tableWifis.appendChild(tbodyWifis);
                wifiInfo.appendChild(tableWifis);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyWifis.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyWifis.appendChild(row);
                }
                tableWifis.appendChild(tbodyWifis);
                wifiInfo.appendChild(tableWifis);
            }
            
            //Blues Info
            var blues=document.getElementById("BluesInfo");
            blues.innerHTML="";
            var tableBlues=document.createElement("table");
            tableBlues.className="display";
            var tbodyBlues=document.createElement("tbody");
            var countBlues=response.countBlues;
            if (countBlues>0){
                for (var i=0; i<countBlues; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.blues[i].blueName);
                    column1.appendChild(column1_text);
                    row.appendChild(column1);
                    tbodyBlues.appendChild(row);
                }
                for (var i=countBlues; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyBlues.appendChild(row);
                }
                tableBlues.appendChild(tbodyBlues);
                blues.appendChild(tableBlues);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyBlues.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyBlues.appendChild(row);
                }
                tableBlues.appendChild(tbodyBlues);
                blues.appendChild(tableBlues);
            }
            
            //IPS Info
            var IPS=document.getElementById("activeIPS");
            IPS.innerHTML="";
            var tableIPS=document.createElement("table");
            tableIPS.className="display";
            var tbodyIPS=document.createElement("tbody");
            var countIPS=response.countIPS;
            if (countIPS>0){
                for (var i=0; i<countIPS; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var modalLink=document.createElement('a');
                    modalLink.setAttribute("data-toggle","modal");
                    modalLink.setAttribute("data-target","#myModal");
                    modalLink.setAttribute("style", "color:#ffffff");
                    var ip=response.ips[i].ip;
                    var functionName1="showInfo('"+ip+"')";
                    modalLink.setAttribute("onclick", functionName1);
                    var column1_text=document.createTextNode(response.ips[i].ip);
                    modalLink.appendChild(column1_text);
                    column1.appendChild(modalLink);
                    row.appendChild(column1);
                    tbodyIPS.appendChild(row);
                }
                for (var i=countIPS; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyIPS.appendChild(row);
                }
                    tableIPS.appendChild(tbodyIPS);
                    IPS.appendChild(tableIPS);
            }else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyIPS.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyIPS.appendChild(row);
                }
                tableIPS.appendChild(tbodyIPS);
                IPS.appendChild(tableIPS);
            }
                            
            //Services Info
            var Services=document.getElementById("Services");
            Services.innerHTML="";
            var tableServices=document.createElement("table");
            tableServices.className="display";
            var tbodyServices=document.createElement("tbody");
            var countServices=response.countScanners;
            if (countServices>0){
                for (var i=0; i<countServices; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.scanners[i]);
                    var column1=document.createElement('td');
                    var modalLink=document.createElement('a');
                    modalLink.setAttribute("data-toggle","modal");
                    modalLink.setAttribute("data-target","#myModal1");
                    modalLink.setAttribute("style", "color:#ffffff");
                    var functionName2="showIPS('"+response.scanners[i]+"')";
                    modalLink.setAttribute("onclick", functionName2);
                    modalLink.appendChild(column1_text);
                    column1.appendChild(modalLink);
                    row.appendChild(column1);
                    tbodyServices.appendChild(row);
                }
                for (var i=countServices; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyServices.appendChild(row);
                }
                tableServices.appendChild(tbodyServices);
                Services.appendChild(tableServices);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyServices.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyServices.appendChild(row);
                }
                tableServices.appendChild(tbodyServices);
                Services.appendChild(tableServices);
            }

            //Hashes
            var hashes=document.getElementById("hashes");
            hashes.innerHTML="";
            var tableHashes=document.createElement("table");
            tableHashes.className="display";
            var tbodyHashes=document.createElement("tbody");
            var countHashes=response.countHashes;
            if (countHashes>0){
                for (var i=0; i<countHashes; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.hashes[i].ip);
                    column1.appendChild(column1_text);
                    row.appendChild(column1);
                    /*var column2=document.createElement('td');
                    var column2_text=document.createTextNode(response.hashes[i].username);
                    column2.setAttribute("style", "width:150px");
                    column2.appendChild(column2_text);
                    row.appendChild(column2);*/
                    var column3=document.createElement('td');
                    var column3_text=document.createTextNode(response.hashes[i].hash);
                    column3.appendChild(column3_text);
                    row.appendChild(column3);
                    tbodyHashes.appendChild(row);
                    

                }
                for (var i=countHashes; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    /*var cell1=document.createElement("td");
                    cell1.setAttribute("style", "height:25px");
                    cell1.setAttribute("style", "width:100px");*/
                    var cell2=document.createElement("td");
                    cell2.setAttribute("style", "height:25px");
                    
                    
                    tbodyHashes.appendChild(row);
                }
                tableHashes.appendChild(tbodyHashes);
                hashes.appendChild(tableHashes);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                var cell2=document.createElement("td");
                    cell2.setAttribute("style", "height:25px");
                    row.appendChild(cell2);
                    
                    var cell3=document.createElement("td");
                    cell3.setAttribute("style", "height:25px");
                
                
                    row.appendChild(cell3);
                tbodyHashes.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    var cell2=document.createElement("td");
                    cell2.setAttribute("style", "height:25px");
                    
                    row.appendChild(cell2);
                    var cell3=document.createElement("td");
                    cell3.setAttribute("style", "height:25px");
                
                
                    row.appendChild(cell3);
                    tbodyHashes.appendChild(row);
                }
                tableHashes.appendChild(tbodyHashes);
                hashes.appendChild(tableHashes);
            }


        }
        else{

        }
    },
    error: function (result){
        console.log(result);
    }
});

function findSession(){
    var sessionID= localStorage.getItem("session");
    var sessionService= 'http://localhost/Reporting/WarberryReporting/SQLiteConnection/session.php';
    if (sessionID==null){
        $.ajax({
            type: "GET",
            url: sessionService,
            beforeSend: function (req) {
                req.setRequestHeader("Accept", "application/json");
            },
            success: function(result) {
                var response = result;
                if (response.status == "success") {
                    //Session Info
                    var count = response.sessions.length;
                    if (count == 0) {
                        console.log("No sessions Found");
                    }
                    else {
                        sessionID = response.sessions[0].sessionID;
                        return sessionID;
                    }
                }
            },
            error: function (result){
                console.log(result);
            }
        });
        return -1;
    }
    else{
        return sessionID;
    }
}

function convert(unixtimestamp){

 // Months array
 var months_arr = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

 // Convert timestamp to milliseconds
 var date = new Date(unixtimestamp*1000);

 // Year
 var year = date.getFullYear();

 // Month
 var month = months_arr[date.getMonth()];

 // Day
 var day = date.getDate();

 // Hours
 var hours = date.getHours();

 // Minutes
 var minutes = "0" + date.getMinutes();

 // Seconds
 var seconds = "0" + date.getSeconds();

 // Display date time in MM-dd-yyyy h:m:s format
 var convdataTime = month+'-'+day+'-'+year+' '+hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
 
return convdataTime;
 
}

function showInfo(ipg) {
    var connect="http://localhost/Reporting/WarberryReporting/SQLiteConnection/ip.php";
    var s=localStorage.getItem("session");
    var param={sessionID:s, ip:ipg};
    $.ajax({
        type: "GET",
        url: connect,
        beforeSend: function (req) {
            req.setRequestHeader("Accept", "application/json");
        },
        success: function(result){
            var response=result;
            if (response.status.indexOf("success")>=0) {
                var title=document.getElementById("titleHost");
                title.innerHTML="";
                var title_text=document.createTextNode(ipg);
                title.appendChild(title_text);
                var hostnames=document.getElementById("hostnamesInfo");
                hostnames.innerHTML="";
                if (response.hostnames.length>0){
                      var os=document.createElement("p");
                      var os_T=response.hostnames[0].os;
                      var os_t1=os_T.replace("[0m ", "");
                      var os_text=document.createTextNode("OS:"+ os_t1);
                      var domain=document.createElement("p");
                      var domain_text=document.createTextNode("Domain:"+ response.hostnames[0].domain);
                      var hostname=document.createElement("p");
                      var hostname_text= document.createTextNode("Hostname:"+ response.hostnames[0].name);
                      os.appendChild(os_text);
                      domain.appendChild(domain_text);
                      hostname.appendChild(hostname_text);
                      hostnames.appendChild(hostname);
                      hostnames.appendChild(os);
                      hostnames.appendChild(domain);
                }
                else{
                    var none=document.createElement("p");
                    var none_text=document.createTextNode("Not found");
                    none.appendChild(none_text);
                    hostnames.appendChild(none);
                }
                var scanners=document.getElementById("servInfo");
                scanners.innerHTML="";
                if (response.scanners.length>0){
                    for (var i=0; i<response.scanners.length; i++){
                        var scanner=document.createElement("p");
                        var scanner_text=document.createTextNode(response.scanners[i]);
                        scanner.appendChild(scanner_text);
                        scanners.appendChild(scanner);
                    }
                }
                else{
                    var none=document.createElement("p");
                    var none_text=document.createTextNode("Not found");
                    none.appendChild(none_text);
                    scanners.appendChild(none);
                }
            
            }
            else{

            }
        },
        error: function (result){
            console.log(result);
        },
        data: param
    });

}

function showIPS(serv) {
    var connect="http://localhost/Reporting/WarberryReporting/SQLiteConnection/service.php";
    var s=localStorage.getItem("session");
    var param={sessionID:s, service:serv};
    $.ajax({
        type: "GET",
        url: connect,
        beforeSend: function (req) {
            req.setRequestHeader("Accept", "application/json");
        },
        success: function(result){
            var response=result;
            if (response.status.indexOf("success")>=0) {
                
                var services=document.getElementById("servicesP");
                var title=document.getElementById("hostTitle");
                title.innerHTML="";
                var title_text=document.createTextNode(serv);
                title.appendChild(title_text);
                services.innerHTML="";
                if (response.hosts.length>0){
                    for (var i=0; i<response.hosts.length; i++){
                        var host=document.createElement("p");
                        var host_text=document.createTextNode( response.hosts[i]);
                        host.appendChild(host_text);
                        services.appendChild(host);
                    }
                }
                else{
                    var none=document.createElement("p");
                    var none_text=document.createTextNode("Not found");
                    none.appendChild(none_text);
                    hostnames.appendChild(none);
                }
            }
            else{

            }
        },
        error: function (result){
            console.log(result);
        },
        data: param
    });

}

function showSessionReporting(sessionID){
    localStorage.setItem("session", sessionID);
    var connectService = 'http://localhost/Reporting/WarberryReporting/SQLiteConnection/reporting.php';
    var sessionID=findSession();
    if (sessionID==-1){
        console.log("No sessions found");
    }
    else{
        var param = {session: sessionID };
    }

    $.ajax({
        type: "GET",
        url: connectService,
        beforeSend: function (req) {
            req.setRequestHeader("Accept", "application/json");
        },
        data:param,
        success: function(result){
            var response=result;
            if (response.status.indexOf("success")>=0) {
                //Sessions 
            var countS=response.sessions.length;;
            var sessionsElement=document.getElementById("external-events");
            sessionsElement.innerHTML="";
            for (var i=0; i<countS; i++){
                var sessionID=response.sessions[i].sessionID;
                var functionName="showSessionReporting("+sessionID+")";
                var hyperlink=document.createElement('a');
                hyperlink.setAttribute("onclick", functionName);
                hyperlink.style.color= "#ffffff";
                hyperlink.style.backgroundColor="#353535";
                var UTime=convert(response.sessions[i].StartTime);
                var hyperlink_text=document.createTextNode(UTime);
                hyperlink.appendChild(hyperlink_text);
                var divEl=document.createElement('div');
                divEl.className="external-event";
                divEl.style.background="#1f1f1f";
                divEl.setAttribute("style", "position:relative");
                divEl.appendChild(hyperlink);
                sessionsElement.appendChild(divEl);
            }
            //Session Info
            var sessionInfo=document.getElementById("SessionInfo");
            sessionInfo.innerHTML="";
            var tableSession=document.createElement("table");
            tableSession.className="display";
            var tbodySession=document.createElement("tbody");
            var rowStart=document.createElement("tr");
            rowStart.className="odd";
            var cellStart=document.createElement("td");
            var rowEnd=document.createElement("tr");
            rowEnd.className="odd";
            var cellEnd=document.createElement("td");
            var rowStatus=document.createElement("tr");
            rowStatus.className="odd";
            var cellStatus=document.createElement("td");
            startT=convert(response.session.StartTime);
            endT=convert(response.session.EndTime);
            var start_text=document.createTextNode("StartTime:\t"+ startT);
            var end_text=document.createTextNode("EndTime:\t"+ endT);
            var status_text=document.createTextNode("Status:\t"+ response.session.Status);
            cellStart.appendChild(start_text);
            cellEnd.appendChild(end_text);
            cellStatus.appendChild(status_text);
            rowStart.appendChild(cellStart);
            rowStart.setAttribute("style", "height:40px");
            rowEnd.appendChild(cellEnd);
            rowEnd.setAttribute("style", "height:40px");
            rowStatus.appendChild(cellStatus);
            rowStatus.setAttribute("style", "height:40px");
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
            }
            tbodySession.appendChild(rowStart);
            tbodySession.appendChild(rowEnd);
            tbodySession.appendChild(rowStatus);
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
                row.appendChild(cell);
                tbodySession.appendChild(row);
            }
            tableSession.appendChild(tbodySession);
            sessionInfo.appendChild(tableSession);

            //Common Info
            var commonInfo=document.getElementById("CommonInfo");
            commonInfo.innerHTML="";
            var tableSession=document.createElement("table");
            tableSession.className="display";
            var tbodySession=document.createElement("tbody");
            var rowCIDR=document.createElement("tr");
            rowCIDR.className="odd";
            var cellCIDR=document.createElement("td");
            var rowInternalIP=document.createElement("tr");
            rowInternalIP.className="odd";
            var cellInternalIP=document.createElement("td");
            var rowExternalIP=document.createElement("tr");
            rowExternalIP.className="odd";
            var cellExternalIP=document.createElement("td");
            var CIDR_text=document.createTextNode("CIDR:\t"+ response.common.CIDR);
            var InternalIP_text=document.createTextNode("Internal IP:\t"+ response.common.InternalIP);
            var External_text=document.createTextNode("External IP:\t"+ response.common.ExternalIP);
            cellCIDR.appendChild(CIDR_text);
            cellInternalIP.appendChild(InternalIP_text);
            cellExternalIP.appendChild(External_text);
            rowCIDR.appendChild(cellCIDR);
            rowCIDR.setAttribute("style", "height:40px");
            rowInternalIP.appendChild(cellInternalIP);
            rowInternalIP.setAttribute("style", "height:40px");
            rowExternalIP.appendChild(cellExternalIP);
            rowExternalIP.setAttribute("style", "height:40px");
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
            }
            tbodySession.appendChild(rowCIDR);
            tbodySession.appendChild(rowInternalIP);
            tbodySession.appendChild(rowExternalIP);
            for (var i=0; i<5; i++){
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                cell.setAttribute("style", "height:20px");
                row.appendChild(cell);
                tbodySession.appendChild(row);
            }
            tableSession.appendChild(tbodySession);
            commonInfo.appendChild(tableSession);
            

            //Wifis Info
            var wifiInfo=document.getElementById("WifisInfo");
            wifiInfo.innerHTML="";
            var tableWifis=document.createElement("table");
            tableWifis.className="display";
            var tbodyWifis=document.createElement("tbody");
            var countWifis=response.countWifis;
            if (countWifis>0){
                for (var i=0; i<countWifis; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.wifis[i].WifiName);
                    column1.appendChild(column1_text);
                    row.appendChild(column1);
                    tbodyWifis.appendChild(row);
                }
                for (var i=countWifis; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyWifis.appendChild(row);
                }
                tableWifis.appendChild(tbodyWifis);
                wifiInfo.appendChild(tableWifis);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyWifis.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyWifis.appendChild(row);
                }
                tableWifis.appendChild(tbodyWifis);
                wifiInfo.appendChild(tableWifis);
            }
            
            //Blues Info
            var blues=document.getElementById("BluesInfo");
            blues.innerHTML="";
            var tableBlues=document.createElement("table");
            tableBlues.className="display";
            var tbodyBlues=document.createElement("tbody");
            var countBlues=response.countBlues;
            if (countBlues>0){
                for (var i=0; i<countBlues; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.blues[i].blueName);
                    column1.appendChild(column1_text);
                    row.appendChild(column1);
                    tbodyBlues.appendChild(row);
                }
                for (var i=countBlues; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyBlues.appendChild(row);
                }
                tableBlues.appendChild(tbodyBlues);
                blues.appendChild(tableBlues);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyBlues.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyBlues.appendChild(row);
                }
                tableBlues.appendChild(tbodyBlues);
                blues.appendChild(tableBlues);
            }
            
            //IPS Info
            var IPS=document.getElementById("activeIPS");
            IPS.innerHTML="";
            var tableIPS=document.createElement("table");
            tableIPS.className="display";
            var tbodyIPS=document.createElement("tbody");
            var countIPS=response.countIPS;
            if (countIPS>0){
                for (var i=0; i<countIPS; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var modalLink=document.createElement('a');
                    modalLink.setAttribute("data-toggle","modal");
                    modalLink.setAttribute("data-target","#myModal");
                    modalLink.setAttribute("style", "color:#ffffff");
                    var ip=response.ips[i].ip;
                    var functionName1="showInfo('"+ip+"')";
                    modalLink.setAttribute("onclick", functionName1);
                    var column1_text=document.createTextNode(response.ips[i].ip);
                    modalLink.appendChild(column1_text);
                    column1.appendChild(modalLink);
                    row.appendChild(column1);
                    tbodyIPS.appendChild(row);
                }
                for (var i=countIPS; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyIPS.appendChild(row);
                }
                    tableIPS.appendChild(tbodyIPS);
                    IPS.appendChild(tableIPS);
            }else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyIPS.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyIPS.appendChild(row);
                }
                tableIPS.appendChild(tbodyIPS);
                IPS.appendChild(tableIPS);
            }
                            
            //Services Info
            var Services=document.getElementById("Services");
            Services.innerHTML="";
            var tableServices=document.createElement("table");
            tableServices.className="display";
            var tbodyServices=document.createElement("tbody");
            var countServices=response.countScanners;
            if (countServices>0){
                for (var i=0; i<countServices; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.scanners[i]);
                    var column1=document.createElement('td');
                    var modalLink=document.createElement('a');
                    modalLink.setAttribute("data-toggle","modal");
                    modalLink.setAttribute("data-target","#myModal1");
                    modalLink.setAttribute("style", "color:#ffffff");
                    var functionName2="showIPS('"+response.scanners[i]+"')";
                    modalLink.setAttribute("onclick", functionName2);
                    modalLink.appendChild(column1_text);
                    column1.appendChild(modalLink);
                    row.appendChild(column1);
                    tbodyServices.appendChild(row);
                }
                for (var i=countServices; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyServices.appendChild(row);
                }
                tableServices.appendChild(tbodyServices);
                Services.appendChild(tableServices);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                tbodyServices.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    tbodyServices.appendChild(row);
                }
                tableServices.appendChild(tbodyServices);
                Services.appendChild(tableServices);
            }

            //Hashes
            var hashes=document.getElementById("hashes");
            hashes.innerHTML="";
            var tableHashes=document.createElement("table");
            tableHashes.className="display";
            var tbodyHashes=document.createElement("tbody");
            var countHashes=response.countHashes;
            if (countHashes>0){
                for (var i=0; i<countHashes; i++){
                    var row=document.createElement('tr');
                    row.className="odd";
                    var column1=document.createElement('td');
                    var column1_text=document.createTextNode(response.hashes[i].ip);
                    column1.appendChild(column1_text);
                    row.appendChild(column1);
                    /*var column2=document.createElement('td');
                    var column2_text=document.createTextNode(response.hashes[i].username);
                    column2.setAttribute("style", "width:150px");
                    column2.appendChild(column2_text);
                    row.appendChild(column2);*/
                    var column3=document.createElement('td');
                    var column3_text=document.createTextNode(response.hashes[i].hash);
                    column3.appendChild(column3_text);
                    row.appendChild(column3);
                    tbodyHashes.appendChild(row);
                    

                }
                for (var i=countHashes; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    /*var cell1=document.createElement("td");
                    cell1.setAttribute("style", "height:25px");
                    cell1.setAttribute("style", "width:100px");*/
                    var cell2=document.createElement("td");
                    cell2.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    //row.appendChild(cell1);
                    row.appendChild(cell2);
                    tbodyHashes.appendChild(row);
                }
                tableHashes.appendChild(tbodyHashes);
                hashes.appendChild(tableHashes);
            }
            else{
                var row=document.createElement("tr");
                row.className="odd";
                var cell=document.createElement("td");
                var column1_text=document.createTextNode("No records found.");
                cell.appendChild(column1_text);
                row.appendChild(cell);
                var cell2=document.createElement("td");
                    cell2.setAttribute("style", "height:25px");
                    row.appendChild(cell2);
                    
                    var cell3=document.createElement("td");
                    cell3.setAttribute("style", "height:25px");
                
                
                    row.appendChild(cell3);
                tbodyHashes.appendChild(row);
                for (var i=1; i<9; i++){
                    var row=document.createElement("tr");
                    row.className="odd";
                    var cell=document.createElement("td");
                    cell.setAttribute("style", "height:25px");
                    row.appendChild(cell);
                    var cell2=document.createElement("td");
                    cell2.setAttribute("style", "height:25px");
                    row.appendChild(cell2);
                    
                    var cell3=document.createElement("td");
                    cell3.setAttribute("style", "height:25px");
                
                
                    row.appendChild(cell3);
                    tbodyHashes.appendChild(row);
                }
                tableHashes.appendChild(tbodyHashes);
                hashes.appendChild(tableHashes);
            }


        }
        else{

        }
        },
        error: function (result){
            console.log(result);
        }
    });
}

