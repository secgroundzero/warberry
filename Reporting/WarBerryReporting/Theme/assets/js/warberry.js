var connectService = 'http://localhost/Reporting/WarberryReporting/SQLiteConnection/home.php';
$.ajax({
    type: "GET",
    url: connectService,
    beforeSend: function (req) {
        req.setRequestHeader("Accept", "application/json");
    },
    success: function(result){
        var response=result;
        if (response.status.indexOf("success")>=0) {
           
            lastSession=0;
            //Warberry Info
            var name=document.getElementById("WarberryName");
            var model=document.getElementById("Model");
            var name_text=document.createTextNode(response.warberry.WarBerryName);
            var model_text=document.createTextNode(response.warberry.WarBerryModel);
            name.appendChild(name_text);
            model.appendChild(model_text);

            //Session Info
            var table=document.getElementById("displaySessions");
            table.className="col-lg-12";
            var tbody = document.createElement('tbody');
            var count=response.sessions.length;
            for (var i=0; i<count; i++){
                var row=document.createElement('tr');
                row.className="even"
                var column1=document.createElement('td');
                var sessionID=response.sessions[i].sessionID;
                var hyperlink=document.createElement('a');
                hyperlink.style.color= "#ffffff";
                var hyperlink1=document.createElement('a');
                hyperlink1.style.color= "#ffffff";
                var UTime=convert(response.sessions[i].StartTime);
                if (response.sessions[i].StartTime>lastSession){
                    lastSession=response.sessions[i].StartTime;
                }
                var column1_text=document.createTextNode(UTime);
                hyperlink.appendChild(column1_text);
                var functionName="showSession("+sessionID+")";
                hyperlink.setAttribute("onclick", functionName);
                hyperlink1.setAttribute("onclick", functionName);
                column1.appendChild(hyperlink);
                //var column2=document.createElement('td');
                //var column2_text=document.createTextNode(response.sessions[i].EndTime);
                //column2.appendChild(column2_text);
                var column3=document.createElement('td');
                var column3_text=document.createTextNode("Completed.");
                hyperlink1.setAttribute("style","color:#b2c831;width:50%");
                hyperlink1.appendChild(column3_text);
                column3.appendChild(hyperlink1);
                row.appendChild(column1);
                //row.appendChild(column2);
                row.appendChild(column3);
                tbody.appendChild(row);
            }
            table.appendChild(tbody);

            //Last Session
            convertedLastSession=convert(lastSession);
            var digclock=document.getElementById("lastSession");
            var digClock_Text=document.createTextNode(convertedLastSession);
            digclock.appendChild(digClock_Text);

        }
        else{

        }
    },
    error: function (result){
        console.log(result);
    }
});

function showSession(sessionID){
    localStorage.setItem("session", sessionID);
    window.location.href="WarberryReporting/Theme/indexReporting.html";
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
