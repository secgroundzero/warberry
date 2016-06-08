
$('#warBerry_tabs a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
});

$('#responder_tabs a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
});

findResults();
createDropDown();

function newTab(id,contentID,tabName){
    var list_item=document.createElement('li');
    list_item.setAttribute("role", "presentation");
    var ref=document.createElement('a');
    ref.setAttribute("id",id);
    ref.setAttribute("href",contentID);
    ref.setAttribute("role", "tab");
    ref.setAttribute("data-toggle", "tab");
    ref.setAttribute("onclick", "changeTab('"+contentID+"')");
    var text=document.createTextNode(tabName);
    ref.appendChild(text);
    list_item.appendChild(ref);
    $('#warBerry_tabs').append(list_item);
    var newtabcontent=document.createElement('div');
    newtabcontent.setAttribute("role", "tabpanel");
    newtabcontent.className="tab-pane";
    newtabcontent.setAttribute("id", contentID.split("#")[1]);
    $('#content-tabs').append(newtabcontent);
}

function changeTab(id){
    var net_scan=document.getElementById("network_scanner_content");
    net_scan.innerHTML="";
    var previous_item=localStorage.getItem("previous");
    document.getElementById(previous_item).setAttribute("style","display:none");
    var id_c=id.split('#')[1];
    localStorage.setItem("previous", id_c);
    document.getElementById(id_c).setAttribute("style","visibility:visible");
}

function changeResponderTab(id){
    var pre=localStorage.getItem("previousResponder");
    document.getElementById(pre).className="tab-pane";
    var id_content=id.split("#")[1];
    localStorage.setItem("previousResponder", id_content);
    var active_pane=document.getElementById(id_content);
    active_pane.className="tab-pane active";
}

function filePresentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className="table table-striped";
        if (resolved>11){
            var line_items= [];
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    line_items.push(elem);
                }
            });
            for (var i=0; i<line_items.length; i++){
                if (i%4==0){
                    var row=document.createElement('tr');
                    var column1=document.createElement('td');
                    var column2=document.createElement('td');
                    var column3=document.createElement('td');
                    var column4=document.createElement('td');
                    var column1_text=document.createTextNode(line_items[i]);
                    column1.appendChild(column1_text);
                    if ((i+1)<line_items.length) {
                        var column2_text = document.createTextNode(line_items[i + 1]);
                    }
                    else{
                        var column2_text = document.createTextNode("-");
                    }
                    column2.appendChild(column2_text);
                    if ((i+2)<line_items.length) {
                        var column3_text = document.createTextNode(line_items[i + 2]);
                    }
                    else{
                        var column3_text = document.createTextNode("-");
                    }
                    column3.appendChild(column3_text);
                    if ((i+3)<line_items.length) {
                        var column4_text = document.createTextNode(line_items[i + 3]);
                    }
                    else{
                        var column4_text = document.createTextNode("-");
                    }
                    column4.appendChild(column4_text);
                    row.appendChild(column1);
                    row.appendChild(column2);
                    row.appendChild(column3);
                    row.appendChild(column4);
                    tbody.appendChild(row);
                }
            }
        }
        else {
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    var row = document.createElement('tr');
                    var column = document.createElement('td');
                    var cell_text = document.createTextNode(elem);
                    column.appendChild(cell_text);
                    row.appendChild(column);
                    tbody.appendChild(row);
                }
            });
        }
    }
    table.appendChild(tbody);
    return table;
}

function enum_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped";
        var line_items = [];

        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("Service");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                    var ports = [];
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                var service=line_items[i].split('open ')[1];
                port_details['port'] = port;
                port_details['service']=service;
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var http_t = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var http_ttext = document.createTextNode(host_details[i]['ports'][j]['service']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                http_t.appendChild(http_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(http_t);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function waf_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("WAF Detection");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
                if (line_items[i+1].indexOf("http-waf-detect")>0) {
                    var waf_title = line_items[i].split(": ")[1];
                    port_details['waf-detect'] = waf_title;
                }
                else{
                    port_details['waf-detect'] = "-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var waf_title = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var waf_ttext = document.createTextNode(host_details[i]['ports'][j]['waf-detect']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                waf_title.appendChild(waf_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(waf_title);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function nfs_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });
        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("NFS Path");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port']=port;
                if (line_items[i+1].indexOf("nfs-showmount")>0) {
                    var nfspath = line_items[i + 1];
                    if (nfspath.indexOf('/') > 0) {
                        port_details['nfs-path'] = nfspath;
                    }
                    else {
                        port_details['nfs-path']="-";
                    }
                }
                else{
                    port_details['nfs-path']="-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }

        host_details[host_counter - 1]['ports'] = ports;
        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var path_t = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var path = document.createTextNode(host_details[i]['ports'][j]['nfs-path']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                path_t.appendChild(path);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(path_t);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function http_title_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("HTTP - Title");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
            }
            else if (line_items[i].indexOf("http-title")>0){
                var http_title=line_items[i].split(": ")[1];
                port_details['http-title']=http_title;
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var http_t = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var http_ttext = document.createTextNode(host_details[i]['ports'][j]['http-title']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                http_t.appendChild(http_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(http_t);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function mysql_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h = document.createElement('thead');
        var t_row = document.createElement('tr');
        var ht1 = document.createElement('th');
        var ht2 = document.createElement('th');
        var ht3 = document.createElement('th');
        var ht1_text = document.createTextNode("Host");
        var ht2_text = document.createTextNode("Port");
        var ht3_text = document.createTextNode("Accounts");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
            }
            else if (line_items[i].indexOf(" Accounts")>0){
                var accounts_all=[];
                var accounts = line_items[i+1];
                if (accounts.indexOf(" No valid accounts found")>0) {
                    port_details['accounts']=[];
                    ports[ports_counter] = port_details;
                    ports_counter++;
                    console.log[host_details];
                }
                else{
                    var end_c;
                    for (var j=i+2; j<line_items.length; j++){
                        if (line_items[j].indexOf(" Statistics")){
                            end_c=j-1;
                        }
                    }
                    for (var j=i+1; j<=end_c; j++){
                        var ac=line_items[j];
                        accounts_all.push(ac);
                    }
                    port_details['accounts']=accounts_all;
                    ports[ports_counter] = port_details;
                    ports_counter++;
                }
            }
         }
        host_details[host_counter - 1]['ports'] = ports;
        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var accounts = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var acc_t="";
                if (host_details[i]['ports'][j]['accounts'].length==0){
                    acc_t="-"
                }
                else{
                    for (var k=0; k<host_details[i]['ports'][j]['accounts'].length; k++){
                        acc_t=acc_t+host_details[i]['ports'][j]['accounts'][k]+'\n';
                    }
                }
                var accounts_ttext = document.createTextNode(acc_t);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                accounts.appendChild(accounts_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(accounts);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function snmp_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("SNMP Enterprise");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
                if (line_items[i+1].indexOf("snmp-info")>0) {
                    if (line_items[i+2].indexOf("enterprise")>0){
                        var enterprise_title = line_items[i].split(": ")[1];
                        port_details['enterprise'] = enterprise_title;
                    }
                }
                else{
                    port_details['enterprise'] = "-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var waf_title = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var waf_ttext = document.createTextNode(host_details[i]['ports'][j]['enterprise']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                waf_title.appendChild(waf_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(waf_title);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function ftp_presentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Port");
        var ht3_text=document.createTextNode("FTP Anon");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf(" open") > 0) {
                var port = line_items[i].split(' ')[0];
                port_details['port'] = port;
                if (line_items[i+1].indexOf("ftp-anon:")>0) {
                    var ftp_title = line_items[i].split(": ")[1];
                    port_details['ftp-anon'] = ftp_title;
                }
                else{
                    port_details['ftp-anon'] = "-";
                }
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;

        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var portname = document.createElement('td');
                var ftp_title = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var portname_text = document.createTextNode(host_details[i]['ports'][j]['port']);
                var ftp_ttext = document.createTextNode(host_details[i]['ports'][j]['ftp-anon']);
                host.appendChild(host_text);
                portname.appendChild(portname_text);
                ftp_title.appendChild(ftp_ttext);
                row.appendChild(host);
                row.appendChild(portname);
                row.appendChild(ftp_title);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function mssql_presentation(lines){

    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });

        var table_h=document.createElement('thead');
        var t_row=document.createElement('tr');
        var ht1=document.createElement('th');
        var ht2=document.createElement('th');
        var ht3=document.createElement('th');
        var ht1_text=document.createTextNode("Host");
        var ht2_text=document.createTextNode("Server");
        var ht3_text=document.createTextNode("Databases");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        ht3.appendChild(ht3_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        t_row.appendChild(ht3);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        var ports = [];
        var port_details = [];
        var host_details = [[]];
        var ports_counter = 0;
        var host_counter = 0;
        for (var i = 0; i < line_items.length; i++) {
            if ((line_items[i].indexOf("scan report for") > 0)) {
                var hostname = line_items[i].split(' ')[4];
                if (host_counter != 0) {
                    host_details[host_counter - 1]['ports'] = ports;
                }
                else {
                    host_details[host_counter]['hostname'] = hostname;
                }
                host_counter++;
                var ports = [];
                ports_counter = 0;
            }
            else if (line_items[i].indexOf("ms-sql-info") > 0) {
                var server_name = line_items[i+1].split(": ")[1];
                port_details['server-name'] = server_name;
                var end_database_d;
                for (var k=i+1; k<line_items.length; k++){
                    if (line_items[k].indexOf("_  ")){
                        end_database_d=k;
                    }
                }
                var databases=[];
                for (var k=i+1; k<end_database_d; k++){
                    if (line_items[k].indexOf("Instance name:")>0){
                        var database_d=[];
                        var database_n=line_items[k].split(': ')[1];
                        database_d['database-name']=database_n;
                        var db_version=line_items[k+2].split(': ')[1];
                        database_d['version-name']=db_version;
                        databases.push(database_d);
                    }
                }
                port_details['databases-details']=databases;
                ports[ports_counter] = port_details;
                ports_counter++;
            }
        }
        host_details[host_counter - 1]['ports'] = ports;
        console.log(host_details);
        for (var i = 0; i < host_details.length; i++) {
            for (var j = 0; j < host_details[i]['ports'].length; j++) {
                var row = document.createElement('tr');
                var host = document.createElement('td');
                var servername = document.createElement('td');
                var db_details = document.createElement('td');
                var host_text = document.createTextNode(host_details[i]['hostname']);
                var servername_text = document.createTextNode(host_details[i]['ports'][j]['server-name']);
                var db="";
                for (var c=0; c<host_details[i]['ports'][j]['databases-details'].length; c++){
                    db=db+ "Name: "+ host_details[i]['ports'][j]['databases-details'][c]['database-name'];
                    db=db+ " Version: "+host_details[i]['ports'][j]['databases-details'][c]['version-name']+" \n";

                }
                var db_text = document.createTextNode(db);
                host.appendChild(host_text);
                servername.appendChild(servername_text);
                db_details.appendChild(db_text);
                row.appendChild(host);
                row.appendChild(servername);
                row.appendChild(db_details);
                tbody.appendChild(row);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}

function shares_presentation(lines){
    
}

function WifisPresentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className="table table-striped";
        if (resolved>11){
            table.className="table table-striped pre-scrollable";
            var line_items= [];
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    var wifi = elem.split(':')[1].split('"')[1];
                    line_items.push(wifi);
                }
            });
            for (var i=0; i<line_items.length; i++){
                if (i%4==0){
                    var row=document.createElement('tr');
                    var column1=document.createElement('td');
                    var column2=document.createElement('td');
                    var column3=document.createElement('td');
                    var column4=document.createElement('td');
                    var column1_text=document.createTextNode(line_items[i]);
                    column1.appendChild(column1_text);
                    if ((i+1)<line_items.length) {
                        var column2_text = document.createTextNode(line_items[i + 1]);
                    }
                    else{
                        var column2_text = document.createTextNode("-");
                    }
                    column2.appendChild(column2_text);
                    if ((i+2)<line_items.length) {
                        var column3_text = document.createTextNode(line_items[i + 2]);
                    }
                    else{
                        var column3_text = document.createTextNode("-");
                    }
                    column3.appendChild(column3_text);
                    if ((i+3)<line_items.length) {
                        var column4_text = document.createTextNode(line_items[i + 3]);
                    }
                    else{
                        var column4_text = document.createTextNode("-");
                    }
                    column4.appendChild(column4_text);
                    row.appendChild(column1);
                    row.appendChild(column2);
                    row.appendChild(column3);
                    row.appendChild(column4);
                    tbody.appendChild(row);
                }
            }
        }
        else {
            $.each(lines, function (n, elem) {
                if (n!=resolved) {
                    var row = document.createElement('tr');
                    var column = document.createElement('td');
                    var cell_text = document.createTextNode(elem.split(':')[1].split('"')[1]);
                    column.appendChild(cell_text);
                    row.appendChild(column);
                    tbody.appendChild(row);
                }
            });
        }
    }
    table.appendChild(tbody);
    return table;
}

function downloadFile(){
    $.fileDownload('Results/capture.pcap').done(function () { });
}

/*$.get('Results/capture.pcap',function(data){
    var lines = data.split("\n");
    var table=pcapResultsPresentation(lines);
    table.setAttribute("style", "overflow-x:hidden");
    var heading=document.createElement('h5');
    var heading_Text=document.createTextNode("Analysis of pcap_results");
    heading.appendChild(heading_Text);
    $('#network_traffic').append(heading);
    $('#network_traffic').append(table);
}).error(function(){console.log("pcapresults file does not Exist")});*/

function pcapResultsPresentation(lines){

    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className="table table-striped";
        $.each(lines, function (n, elem) {
            if (n!=resolved) {
                var row = document.createElement('tr');
                var column = document.createElement('td');
                var cell_text = document.createTextNode(elem);
                column.appendChild(cell_text);
                row.appendChild(column);
                tbody.appendChild(row);
            }
        });
    }
    table.appendChild(tbody);
    return table;
}


function ResponderPresentation(lines,file){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        table.className = "table table-striped";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n != resolved) {
                line_items.push(elem);
            }
        });
        if (line_items[0].indexOf("Clear-Text")>=0) {
            var table_h = document.createElement('thead');
            var t_row = document.createElement('tr');
            var ht1 = document.createElement('th');
            var ht2 = document.createElement('th');
            ht1.setAttribute("style", "text-align:center");
            ht2.setAttribute("style", "text-align:center");
            var ht1_text = document.createTextNode("Name");
            var ht2_text = document.createTextNode("Password");
            ht1.appendChild(ht1_text);
            ht2.appendChild(ht2_text);
            t_row.appendChild(ht1);
            t_row.appendChild(ht2);
            table_h.appendChild(t_row);
            table.appendChild(table_h);

            var accInfo=[];
            for (var i=0; i<line_items.length; i++){
                var passDomain=[];
                passDomain['user']=line_items[i].split(':')[0];
                passDomain['pass']=line_items[i].split(':')[1];
                accInfo.push(passDomain);
            }
            for (var i=0; i<line_items.length; i++){
                var row=document.createElement('tr');
                var c1=document.createElement('td');
                var c2=document.createElement('td');
                var c1_text=document.createTextNode(accInfo[i]['user']);
                var c2_text=document.createTextNode(accInfo[i]['pass']);
                c1.appendChild(c1_text);
                c2.appendChild(c2_text);
                row.appendChild(c1);
                row.appendChild(c2);
                tbody.append(row);
            }

        }
        else {
            var table_h = document.createElement('thead');
            var t_row = document.createElement('tr');
            var ht1 = document.createElement('th');
            var ht2 = document.createElement('th');
            var ht3 = document.createElement('th');
            ht1.setAttribute("style", "text-align:center");
            ht2.setAttribute("style", "text-align:center");
            var ht1_text = document.createTextNode("Name");
            var ht2_text = document.createTextNode("Domain");
            ht1.appendChild(ht1_text);
            ht2.appendChild(ht2_text);
            t_row.appendChild(ht1);
            t_row.appendChild(ht2);
            t_row.appendChild(ht3);
            table_h.appendChild(t_row);
            table.appendChild(table_h);

            var domains = [];
            for (var i = 0; i < line_items.length; i++) {
                var nameDomain = [];
                var name = line_items[i].split(':')[0];
                nameDomain['name'] = name;
                var domain = line_items[i].split('::')[1].split(':')[0];
                nameDomain['domain'] = domain;
                nameDomain['full'] = line_items[i];
                domains.push(nameDomain);
            }
            for (var i = 0; i < line_items.length; i++) {
                var row = document.createElement('tr');
                var row_copy = document.createElement('tr');
                var c1 = document.createElement('td');
                var c2 = document.createElement('td');
                var c3 = document.createElement('td');
                c1.setAttribute("style", "text-align:center");
                c2.setAttribute("style", "text-align:center");
                c3.setAttribute("style", "text-align:right");
                var link = document.createElement('a');
                var c1_text = document.createTextNode(domains[i]['name']);
                var c2_text = document.createTextNode(domains[i]['domain']);
                var span_t = document.createElement('span');
                span_t.className = "glyphicon glyphicon-menu-down";
                var row_ctext = document.createTextNode(domains[i]['full']);
                row_copy.setAttribute("id", file + i);
                var span_t2 = document.createElement('span');
                span_t2.setAttribute("style", "word-wrap:break-word;display:inline-block;");
                span_t2.className = "col-xs-1 col-sm-1 col-md-2";
                span_t2.appendChild(row_ctext);
                row_copy.appendChild(span_t2);
                row_copy.setAttribute("style", "display:none");
                link.appendChild(span_t);
                var fileID=file+i;
                link.setAttribute("onclick", "showContent('"+fileID+"')");
                c1.appendChild(c1_text);
                c2.appendChild(c2_text);
                c3.appendChild(link);
                row.appendChild(c1);
                row.appendChild(c2);
                row.appendChild(c3);
                tbody.appendChild(row);
                tbody.appendChild(row_copy);
            }
        }
    }
    table.appendChild(tbody);
    return table;
}


function showContent(record){
    var id=document.getElementById(record);
    if (id.getAttribute("style").indexOf("display:none")>=0){
        id.setAttribute("style","display:inherit");
    }
    else{
        id.setAttribute("style","display:none");
    }
}

function ResponderTabs(files){
    var div=document.createElement('div');
    div.setAttribute("id", "responder_c");
    var tabs=document.createElement('ul');
    tabs.setAttribute("role","tablist");
    tabs.setAttribute("id", "responder_tabs");
    tabs.className="nav nav-tabs nav-justified";
    tabs.setAttribute("style", "margin-top:20px");
    var panel_content=document.createElement('div');
    panel_content.className="tab-content";
    panel_content.setAttribute("style", "margin-top:20px");
    $.each(files, function(index, value){
        var file=value;
        var i=index;
        var path='Results/Responder_logs/logs/'+ file;
        $.get(path, function(data) {
            var lines = data.split("\n");
            var contentn = file + '_content';
            var tabPanel = createTabPanels(contentn, i);
            var responderi = file + '_responder';
            var list_i = newTabResponder(responderi, '#' + contentn, file, i);
            var table = ResponderPresentation(lines, file);
            table.setAttribute("id", "responder_table" + i);
            tabPanel.appendChild(table);
            panel_content.appendChild(tabPanel);
            tabs.appendChild(list_i);
            });
    });

    div.appendChild(tabs);
    div.appendChild(panel_content);
    console.log(div);
    $('#responder_content').append(div);
}

function createTabPanels(id,counter){
    var panel=document.createElement('div');
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("id", id);
    if (counter==0){
        panel.className="tab-pane active";
    }
    else{
        panel.className="tab-pane";
    }
    return panel;
}

function newTabResponder(id,contentID,tabName,counter){
    var list_item=document.createElement('li');
    list_item.setAttribute("role", "presentation");
    var ref=document.createElement('a');
    ref.setAttribute("id",id);
    ref.setAttribute("href",contentID);
    ref.setAttribute("role", "tab");
    ref.setAttribute("data-toggle", "tab");
    ref.setAttribute("onclick", "changeResponderTab('"+contentID+"')");
    var text=document.createTextNode(tabName);
    ref.appendChild(text);
    list_item.appendChild(ref);
    if (counter==0){
        list_item.className="active";
        var c=contentID.split("#")[1];
        localStorage.setItem("previousResponder", c);
    }
    return list_item;
}

function findResponderElements(){
    var dir='readDirectory.php';
    var directory="Results/Responder_logs/logs/";
    var arg={directory:directory};

    $.ajax({
        url:dir,
        type:'GET',
        dataType: 'json',
        success:function(data) {
            var response= data;
            var validFiles=[];
            for (var i=0; i<response.Files.length; i++) {
                if ((response.Files[i].indexOf(".log")>=0) || (response.Files[i].indexOf("..")>=0) || ((response.Files[i].length==1) && (response.Files[i].indexOf('.')>=0))){}
                else{
                    validFiles.push(response.Files[i])
                }
            }
           ResponderTabs(validFiles);
        },
        error:function(){
            console.log("Error");
        },
        data: arg
    });
}

function findResults(){
    localStorage.setItem("previous","network_traffic");
    var dir='readDirectory.php';
    var directory="Results/";
    var arg={directory:directory};
    $.ajax({
        url:dir,
        type:'GET',
        dataType: 'json',
        success:function(data) {
            var response= data;
            var validFiles=[];
            for (var i=0; i<response.Files.length; i++) {
                if ((response.Files[i].indexOf("statics")>=0) || (response.Files[i].indexOf("capture.pcap")>=0)|| (response.Files[i].indexOf("avail_ips")>=0) || (response.Files[i].indexOf("..")>=0) || ((response.Files[i].length==1) && (response.Files[i].indexOf('.')>=0))){}
                else{
                    validFiles.push(response.Files[i])
                }
            }
            $.each(validFiles, function(index, value){
                var path=directory+value;
                if (value.localeCompare('Responder_logs')==0){
                    newTab("responder","#responder_content","Responder Results");
                    findResponderElements();
                }
                else {
                    $.get(path, function (data) {
                        var title = findTitle(value);
                        if (title.localeCompare("network_scanner")==0){
                            var scan=[];
                            scan['filename']=value;
                            scan['data']=lines;
                            newDropdownItem(scan);
                        }
                        else{
                            newTab(value, "#" + value + "_content", title);
                            var lines = data.split("\n");
                            Presentation(lines, value);
                        }
                    });
                }
            });
        },
        error:function(){
            console.log("Error");
        },
        data: arg
    });

}

function findTitle(filename){
    switch (filename){
        case 'avail_ips': return 'Available IPs';
            break;
        case 'hostnames' : return 'Hostnames';
            break;
        case 'used_ips': return 'Used IPs';
            break;
        case 'ips_discovered': return "IPs Discovered";
            break;
        case 'windows': return 'network_scanner';
            break;
        case 'ftp': return 'network_scanner';
            break;
        case 'mysql': return 'network_scanner';
            break;
        case 'webservers80': return 'network_scanner';
            break;
        case 'webservers443': return 'network_scanner';
            break;
        case 'webservers8080': return 'network_scanner';
            break;
        case 'webservers4443': return 'network_scanner';
            break;
        case 'webservers8081': return 'network_scanner';
            break;
        case 'webservers8181': return 'network_scanner';
            break;
        case 'webservers9090': return 'network_scanner';
            break;
        case 'mssql': return 'network_scanner';
            break;
        case 'oracle': return 'network_scanner';
            break;
        case 'nfs': return 'network_scanner';
            break;
        case 'webservers': return 'network_scanner';
            break;
        case 'printers': return 'network_scanner';
            break;
        case 'mongo': return 'network_scanner';
            break;
        case 'telnet': return 'network_scanner';
            break;
        case 'vnc': return 'network_scanner';
            break;
        case 'dns': return 'network_scanner';
            break;
        case 'phpmyadmin': return 'network_scanner';
            break;
        case 'tightvnc': return 'network_scanner';
            break;
        case 'websphere': return 'network_scanner';
            break;
        case 'firebird': return 'network_scanner';
            break;
        case 'xserver': return 'network_scanner';
            break;
        case 'svn': return 'network_scanner';
            break;
        case 'snmp': return 'network_scanner';
            break;
        case 'voip': return 'network_scanner';
            break;
        case 'rlogin': return 'network_scanner';
            break;
        case 'openvpn': return 'network_scanner';
            break;
        case 'ipsec': return 'network_scanner';
            break;
        case 'ldap': return 'network_scanner';
            break;
        case 'pop3': return 'network_scanner';
            break;
        case 'smtp': return 'network_scanner';
            break;
        case 'http_titles': return 'HTTP Titles Enum';
            break;
        case 'shares': return 'Shares Enum';
            break;
        case 'smb_users': return 'SMB Users Enum';
            break;
        case 'nfs_enum': return 'NFS Enum';
            break;
        case 'wafed': return 'WAF Enum';
            break;
        case 'mysql_enum': return 'MYSQL Enum';
            break;
        case 'mssql_enum': return 'MSSQL Enum';
            break;
        case 'ftp_enum': return 'FTP Enum';
            break;
        case 'snmp_enum': return 'SNMP Enum';
            break;
        case 'wifis': return 'Wireless Networks';
            break;
        case 'blues': return 'Bluetooth Devices';
            break;
        default: return filename;
    }
}

function Presentation(lines,filename){
    var table;
    switch (filename){
        case 'wifis': table=WifisPresentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'http_titles': table=http_title_presentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'smb_users': table=enum_presentation(lines,filename);
            $("#"+filename+"_content").append(table);
            break;
        case 'shares': table=enum_presentation(lines,filename);
            $("#"+filename+"_content").append(table);
            break;
        case 'nfs_enum': table=nfs_presentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'wafed': table=waf_presentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'mysql_enum': table=mysql_presentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'mssql_enum':table=mssql_presentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'ftp_enum': table=enum_presentation(lines,filename);
            $("#"+filename+"_content").append(table);
            break;
        case 'snmp_enum':table=snmp_presentation(lines);
            $("#"+filename+"_content").append(table);
            break;
        case 'blues': table=BluesPresentation(lines,filename);
            $("#"+filename+"_content").append(table);
            break;
        default: table=filePresentation(lines);
            $("#"+filename+"_content").append(table);
            break;
    }
}


function createDropDown(){
    var dropdowntab=document.createElement('li');
    dropdowntab.className="dropdown";
    dropdowntab.setAttribute("role","presentation");
    dropdowntab.setAttribute("id", "dropdowntab_scanners");
    var dropdownA=document.createElement("a");
    dropdownA.className="dropdown-toggle";
    dropdownA.setAttribute("data-toggle", "dropdown");
    dropdownA.setAttribute("role","tab");
    dropdownA.setAttribute("aria-haspopup","true");
    dropdownA.setAttribute("aria-expanded","false");
    dropdownA.setAttribute("href","#");
    var ttext=document.createTextNode('Network Scanners');
    dropdownA.appendChild(ttext);
    var spant=document.createElement('span');
    spant.classname="caret";
    var dropdownmenu=document.createElement('ul');
    dropdownmenu.className="dropdown-menu";
    dropdownmenu.setAttribute("id", "dropdownmenu_scanners");
    dropdownA.appendChild(spant);
    dropdowntab.appendChild(dropdownA);
    dropdowntab.appendChild(dropdownmenu);
    $('#warBerry_tabs').append(dropdowntab);
}

function newDropdownItem(scan){
    var newItem=document.createElement('li');
    var t=findItemTitle(scan['filename']);
    var litext=document.createTextNode(t);
    var a=document.createElement('a');
    a.setAttribute('onclick',"show_scanner_content('"+scan['filename']+"')");
    a.appendChild(litext);
    newItem.appendChild(a);
    $('#dropdownmenu_scanners').append(newItem);
}

function findItemTitle(filename){
    switch (filename){
        case 'windows': return 'Windows';
            break;
        case 'ftp': return 'FTP';
            break;
        case 'mysql': return 'MySQL';
            break;
        case 'webservers80': return 'Web Servers 80';
            break;
        case 'webservers443': return 'Web Serveres 443';
            break;
        case 'webservers8080': return 'Web Serveres 8080';
            break;
        case 'webservers4443': return 'Web Serveres 4443';
            break;
        case 'webservers8081': return 'Web Serveres 8081';
            break;
        case 'webservers8181': return 'Web Serveres 8181';
            break;
        case 'webservers9090': return 'Web Serveres 9090';
            break;
        case 'mssql': return 'MSSQL';
            break;
        case 'oracle': return 'Oracle';
            break;
        case 'nfs': return 'NFS';
            break;
        case 'webservers': return 'Web Servers';
            break;
        case 'printers': return 'Printers';
            break;
        case 'mongo': return 'Mongo';
            break;
        case 'telnet': return 'Telnet';
            break;
        case 'vnc': return 'VNC';
            break;
        case 'dns': return 'DNS';
            break;
        case 'phpmyadmin': return 'PhpMyAdmin';
            break;
        case 'tightvnc': return 'Tight VNC';
            break;
        case 'websphere': return 'WebSphere';
            break;
        case 'firebird': return 'FireBird';
            break;
        case 'xserver': return 'XServer';
            break;
        case 'svn': return 'SVN';
            break;
        case 'snmp': return 'SNMP';
            break;
        case 'voip': return 'VOIP';
            break;
        case 'rlogin': return 'r Login';
            break;
        case 'openvpn': return 'Open VPN';
            break;
        case 'ipsec': return 'IP Sec';
            break;
        case 'ldap': return 'LDAP';
            break;
        case 'pop3': return 'POP3';
            break;
        case 'smtp': return 'SMTP';
            break;
    }

}

function show_scanner_content(file){
    var directory="Results/";
    var path=directory+file;
    $.get(path, function (data) {
        var lines=data.split("\n");
        var table=filePresentation(lines);
        table.setAttribute("table", "shownTable");
        var net_scan=document.getElementById("network_scanner_content");
        net_scan.innerHTML="";
        $('#network_scanner_content').append(table);
        $('#dropdowntab_scanners').tab('show');
        var previous=localStorage.getItem("previous");
        var content=document.getElementById('network_scanner_content');
        content.style.display="inherit";
        document.getElementById(previous).setAttribute("style", "display:none");
    });
}

function BluesPresentation(lines){
    var resolved=lines.length-1;
    var table=document.createElement('table');
    var tbody=document.createElement('tbody');
    if (resolved==0){
        var row=document.createElement('tr');
        table.className="table";
        var column=document.createElement('td');
        column.className="warning";
        var column_text=document.createTextNode("No Results Found");
        column.appendChild(column_text);
        row.appendChild(column);
        tbody.appendChild(row);
    }
    else {
        var table_h = document.createElement('thead');
        var t_row = document.createElement('tr');
        var ht1 = document.createElement('th');
        var ht2 = document.createElement('th');
        var ht1_text = document.createTextNode("Device");
        var ht2_text = document.createTextNode("MAC Address");
        ht1.appendChild(ht1_text);
        ht2.appendChild(ht2_text);
        t_row.appendChild(ht1);
        t_row.appendChild(ht2);
        table_h.appendChild(t_row);
        table.appendChild(table_h);

        table.className = "table table-striped pre-scrollable";
        var line_items = [];
        $.each(lines, function (n, elem) {
            if (n!=resolved) {
                var c = elem.lastIndexOf(' ');
                var device_d = [];
                device_d["device_name"] = elem.substring(0, c);
                device_d['mac'] = elem.substring(c + 1);
                line_items.push(device_d);
            }
        });

        var device_n=[];
        var mac_n=[];

        for(var i = 0; i <line_items.length; i++) {
            if(!mac_n.includes(line_items[i]['mac'])) {
                device_n.push(line_items[i]['device_name']);
                mac_n.push(line_items[i]['mac']);
            }
        }

        for (var i=0; i<device_n.length; i++){
            var row = document.createElement('tr');
            var column1 = document.createElement('td');
            var column2 = document.createElement('td');
            var cell_text1 = document.createTextNode(device_n[i]);
            var cell_text2 = document.createTextNode(mac_n[i]);
            column1.appendChild(cell_text1);
            column2.appendChild(cell_text2);
            row.appendChild(column1);
            row.appendChild(column2);
            tbody.appendChild(row);
        }

    }
    table.appendChild(tbody);
    return table;
}

