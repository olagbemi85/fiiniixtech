

$(document).ready(function(){

    setInterval(function() {
            $.ajax({
              "url": "/solarIot/auto",
              "type": "GET",
              "datatype": "json",
              success: function (response) { 
               // console.log(response)
               var instance = JSON.parse(response["numSerial"]);
               console.log(instance)
               var fields = instance[0]["fields"];
           /*    $("#autoload tbody").append(
                `<tr>
                <td>${fields["hourly"]||""}</td>
                <td>${fields["voltage"]||""}</td>
                <td>${fields["currents"]||""}</td
                <td>${fields["power"]||""}</td>
                <td>${fields["temp"]||""}</td>
                <td>${fields["intensity"]||""}</td>
                </tr>`
            ) */    
           // console.log(fields["intensity"])
            document.getElementById("days").innerHTML = fields["days"];  
            document.getElementById("hourly").innerHTML = fields["hourly"];
            document.getElementById("voltage").innerHTML = fields["voltage"];
            document.getElementById("currents").innerHTML = fields["currents"];
            document.getElementById("power").innerHTML = fields["power"];
            document.getElementById("temp").innerHTML = fields["temp"];
            document.getElementById("intensity").innerHTML = fields["intensity"];

               }
            });

        }, 2500); 
   
});
 /*
    $(document).ready(function () {  
        $('#autoload').dataTable({ 
            
            "ajax": {  
                "url": "/iotSolar_proj/auto",  
                "type": "GET",  
                "datatype": "json"  
            },  
            "columns": [  
                { "numSerial.hourly": "Time" },  
                { "numSerial.voltage": "Voltage" },  
                { "numSerial.currents": "Current" },  
                { "numSerial.power": "Power" },  
                { "numSerial.temp": "Temp" } , 
                { "numSerial.intensity": "Intensity" } 
                

                    $("#hourly").load(numSerial.hourly); 
                    $("#voltage").load(numSerial.voltage); 
                    $("#currents").load(numSerial.currents); 
                    $("#temp").load(numSerial.temp); 
                    $("#days").load(numSerial.days); 
                    $("#power").load(numSerial.power); 
                    $("#intensity").load(numSerial.intensity); 
                    
            ]  
        });  
    });

 */

    $(document).ready(function(){

        setInterval(function() {
                $.ajax({
                "url": "/solarIot/maxmin",
                "type": "GET",
                "datatype": "json",
                success: function (response) {             
                var maxv = JSON.parse(response["max_volt"]);
                var minv = JSON.parse(response["min_volt"]);
                let maxi = JSON.parse(response["max_amp"]);
                let mini = JSON.parse(response["min_amp"]);
                let maxt = JSON.parse(response["max_temp"]);
                let mint = JSON.parse(response["min_temp"]);
                let maxp = JSON.parse(response["max_power"]);
                let minp = JSON.parse(response["min_power"]);
                let maxin = JSON.parse(response["max_ints"]);
                let minin = JSON.parse(response["min_ints"]);

                document.getElementById("maxV").innerHTML = maxv;  
                document.getElementById("minV").innerHTML = minv;
                document.getElementById("maxI").innerHTML = maxi;
                document.getElementById("minI").innerHTML = mini;
                document.getElementById("maxP").innerHTML = maxp;
                document.getElementById("minP").innerHTML = minp;
                document.getElementById("maxIn").innerHTML = maxin;
                document.getElementById("minIn").innerHTML = minin;
                document.getElementById("maxT").innerHTML = maxt;
                document.getElementById("minT").innerHTML = mint;
              
    
                }
                });
    
            }, 2500); 
    
    });
