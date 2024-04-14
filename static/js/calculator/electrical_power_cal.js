


    // Selectors
    let appliance = document.querySelector(".gadget");
    let selected = document.querySelector(".selected");
    let loadActive = document.getElementsByClassName("load-active");

    // Resistive Load
    let resistive = document.querySelector(".resistiveLoad");
    let resistiveLoad = document.getElementById("resistive-load");
    let ResistiveQty = document.getElementById("resistive-qty");

    // Other
    /*
    let totalLoad = document.getElementById("total-load");
    let batteryCapacity = document.getElementById("battery-capacity");
    let backupTime = document.getElementById("backup-time");
    let rating = document.getElementById("rating");
    let batteryVolt = document.getElementById("inverter_battery");
    let loadPrice = document.getElementById("etimate-price");
    let load = document.getElementsByName("load");
    let note = document.querySelector(".note");
    let lcForm = document.getElementById("lc-form");
    let lcFormTitle = document.getElementById("lc-form-title");
    let lcFormButton = document.getElementById("lc-submit");
    let results = document.querySelector("#lc-results");
    let getInvertors = document.getElementById("get-invertors");
    */


    function showResults() {
      lcFormTitle.style.display = "none";
      lcForm.style.display = "none";
      results.style.display = "block";
    }

    function showResultsDelayed() {
      setTimeout(showResults, 3000);
    }

    // lcForm.addEventListener("submit", showResultsDelayed);

    // Select functions
    // resistive
    function selectResistive() {
      resistive.classList.toggle("selected");

      if (resistive.classList.contains("selected")) {
        ResistiveQty.classList.add("active");
        resistiveLoad.classList.add("active", "load-active");
        ResistiveQty.value = 1;
        ResistiveQty.disabled = false;
      } else {
        ResistiveQty.classList.remove("active");
        resistiveLoad.classList.remove("active", "load-active");
        ResistiveQty.value = 0;
        resistiveLoad.value = 0;
        ResistiveQty.disabled = true;
      }
    }

   

 
    // Load calculators
    //Resistive Load
    function totalResistLoad() {
        resistiveLoad.value = ResistiveQty.value * 200;
    }

    // Microwave Oven
    function totalMicrowaveovenLoad() {
      microwaveovenLoad.value = microwaveovenQty.value * 1400;
    }


 /*   function baseurl(){
      return 'http://fanquix.com'; 
    }
*/

    function isEmpty(str) {
      return !str || str.length === 0 || str == null || str === "";
    }

    document.querySelectorAll(".num")?.forEach((el) => {
      let events;
      for (events of ["change", "keyup", "paste", "blur"]) {
          el.addEventListener(events, function (ev) {
              el.value = el.value.replace(/[^0-9.]/g, "").replace(/(\..*)\./g, "$1");
          });
      }
    });

    function readOnly(inputs, action = true) {
      let elem = inputs.elements;
      for (var i = 0, len = elem.length; i < len; ++i) {
          elem[i].readOnly = action;
      }
    }

    function requiredForm(element) {
      var required_filled = true;
      element.querySelectorAll("[required]")?.forEach(function (input) {
          if (!required_filled) return;
          if (input.type === "radio" || input.type === "checkbox") {
              var radioValueCheck = false;
              element.querySelectorAll(`[name='${input.name}']`)?.forEach(function (radio) {
                  if (radio.checked) radioValueCheck = true;
              });
              required_filled = radioValueCheck;
              return;
          }
          if (!input.value) {
              required_filled = false;
              return;
          }
      });

      return required_filled;
    }
    
    //invter AC two
    function selectInvActwo() {
      invactwo.classList.toggle("selected");
      if (invactwo.classList.contains("selected")) {
        invactwoQty.classList.add("active");
        invactwoLoad.classList.add("active", "load-active");
        invactwoQty.value = 1;
        invactwoQty.disabled = false;
      } else {
        invactwoQty.classList.remove("active");
        invactwoLoad.classList.remove("active", "load-active");
        invactwoQty.value = 0;
        invactwoLoad.value = 0;
        invactwoQty.disabled = true;
      }
    }



    // Toaster
    function totalToasterLoad() {
      toasterLoad.value = toasterQty.value * 800;
    }

    

    // Recommended rating
    var bbv = 0;
    function getRating() {
      if (totalLoad.value <= 400) {
        rating.value = 800;
        bbv = 12;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir01";
      } else if (totalLoad.value > 400 && totalLoad.value < 751) {
        rating.value = 1500;
        bbv = 24;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir02";
      } else if (totalLoad.value > 750 && totalLoad.value < 1226) {
        rating.value = 2500;
        bbv = 36;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir03";
      } else if (totalLoad.value > 1225 && totalLoad.value < 1751) {
        rating.value = 3500;
        bbv = 48;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir04";
      } else if (totalLoad.value > 1750 && totalLoad.value < 2501) {
        rating.value = 5000;
        bbv = 96;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir05";
      } else if (totalLoad.value > 2500 && totalLoad.value < 3751) {
        rating.value = 7500;
        bbv = 120;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir06";
      } else if (totalLoad.value > 3750 && totalLoad.value < 5001) {
        rating.value = 10000;
        bbv = 180;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir07";
      } else if (totalLoad.value > 5000 && totalLoad.value < 7501) {
        rating.value = 15000;
        bbv = 240;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir08";
      } else if (totalLoad.value > 7500 && totalLoad.value < 10001) {
        rating.value = 20000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir09";
      } else if (totalLoad.value > 10000 && totalLoad.value < 15001) {
        rating.value = 30000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir10";
      } else if (totalLoad.value > 15000 && totalLoad.value < 20001) {
        rating.value = 40000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir11";
      } else if (totalLoad.value > 20000 && totalLoad.value < 25001) {
        rating.value = 50000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir12";
      } else if (totalLoad.value > 25000 && totalLoad.value < 30001) {
        rating.value = 60000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir13";
      } else if (totalLoad.value > 30000 && totalLoad.value < 40001) {
        rating.value = 80000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir14";
      } else if (totalLoad.value > 40000 && totalLoad.value < 60001) {
        rating.value = 120000;
        bbv = 384;
        //getInvertors.href = "https://www.thesimbaden.com/product-tag/ir15";
      } else {
        console.log("none");
      }
      
    }

    // Battery backup time calculator
    function calcBackupTime() {
      var bbt = 0;
      const x = 0.8;
      bbt = (x * batteryCapacity.value * bbv) / totalLoad.value;
      backupTime.value = Math.round(bbt * 100) / 100;

      if (isEmpty(bbt)) {
        backupTime.value = 0;
        note.innerText = `please select at least one appliance to calculate your load.`;
      } else {
        note.innerText = ``;
      }

      /*
      if(batteryCapacity.value == 150){
        batt_price = 180000;
      }else if(batteryCapacity.value == 220){
        batt_price = 245000;
      }else{
        batt_price = 0;
        loadPrice.value = `Battery Unavailable`;
        return; 
      }

      if(totalLoad.value >= 700 && rating.value >= 1500 && rating.value < 2000){
        batteryVolt.value = `2 Battery 24v`;

        if(rating.value >= 1400 && rating.value < 1550){
          loadPrice.value = `NGN ${Number(batt_price + 128000).toLocaleString()}`; 
        }else{
          loadPrice.value = `NGN ${Number(batt_price + 128000).toLocaleString()}`; 
        }
      }else if(totalLoad.value >= 730 && rating.value >= 1500){
        batteryVolt.value = `4 Battery 48v`;
        if(rating.value >= 2200 && rating.value < 7400){
          loadPrice.value = `NGN ${Number(batt_price + 933000).toLocaleString()}`; 
        }else if(rating.value >= 7400 && rating.value < 9900){
          loadPrice.value = `NGN ${Number(batt_price + 1261000).toLocaleString()}`; 
        }else{
          loadPrice.value = `NGN ${Number(batt_price + 1512000).toLocaleString()}`; 
        }
      }else{
        batteryVolt.value = `1 Battery 12v`;
        if(rating.value >= 0 && rating.value < 890){
          loadPrice.value = `NGN ${Number(batt_price + 120000).toLocaleString()}`; 
        }else if(rating.value >= 890 && rating.value < 1050){
          loadPrice.value = `NGN ${Number(batt_price + 91000).toLocaleString()}`; 
        }else{
          loadPrice.value = `NGN ${Number(batt_price + 117000).toLocaleString()}`; 
        }
      }
      */
    }


    // Total load calculator
    function calcTotalLoad() {
      var total = 0;
      var i = 0;
      var batt_price = 0;

      for (i = 0; i < loadActive.length; i++) {
        total += parseInt(loadActive[i].value);
      }
      
      totalLoad.value = total;
      getRating();
      calcBackupTime();

      if(batteryCapacity.value == 150){
        batt_price = 180000;
      }else if(batteryCapacity.value == 220){
        batt_price = 245000;
      }else{
        batt_price = 0;
        loadPrice.value = `Battery Unavailable`;
        return; 
      }

      if(totalLoad.value >= 700 && rating.value >= 1500 && rating.value < 2000){
        batteryVolt.value = `2 Battery 24v`;

        if(rating.value >= 1400 && rating.value < 1550){
          loadPrice.value = `NGN ${Number(batt_price + 128000).toLocaleString()}`; 
        }else{
          loadPrice.value = `NGN ${Number(batt_price + 128000).toLocaleString()}`; 
        }
      }else if(totalLoad.value >= 730 && rating.value >= 1500){
        batteryVolt.value = `4 Battery 48v`;
        if(rating.value >= 2200 && rating.value < 7400){
          loadPrice.value = `NGN ${Number(batt_price + 933000).toLocaleString()}`; 
        }else if(rating.value >= 7400 && rating.value < 9900){
          loadPrice.value = `NGN ${Number(batt_price + 1261000).toLocaleString()}`; 
        }else{
          loadPrice.value = `NGN ${Number(batt_price + 1512000).toLocaleString()}`; 
        }
      }else{
        batteryVolt.value = `1 Battery 12v`;
        if(rating.value >= 0 && rating.value < 890){
          loadPrice.value = `NGN ${Number(batt_price + 120000).toLocaleString()}`; 
        }else if(rating.value >= 890 && rating.value < 1050){
          loadPrice.value = `NGN ${Number(batt_price + 91000).toLocaleString()}`; 
        }else{
          loadPrice.value = `NGN ${Number(batt_price + 117000).toLocaleString()}`; 
        }
        
      }
    }

