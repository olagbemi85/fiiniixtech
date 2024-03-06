
    // Selectors
    let appliance = document.querySelector(".gadget");
    let selected = document.querySelector(".selected");
    let loadActive = document.getElementsByClassName("load-active");
    // Bulb
    let bulb = document.querySelector(".bulb");
    let bulbLoad = document.getElementById("bulb-load");
    let bulbQty = document.getElementById("bulb-qty");
    // Tube Light
    let tlight = document.querySelector(".tlight");
    let tlightLoad = document.getElementById("tlight-load");
    let tlightQty = document.getElementById("tlight-qty");
    // LED Lamp
    let ledlamp = document.querySelector(".ledlamp");
    let ledlampLoad = document.getElementById("ledlamp-load");
    let ledlampQty = document.getElementById("ledlamp-qty");
    // Fan
    let fan = document.querySelector(".fan");
    let fanLoad = document.getElementById("fan-load");
    let fanQty = document.getElementById("fan-qty");
    // Music system
    let msystem = document.querySelector(".msystem");
    let msystemLoad = document.getElementById("msystem-load");
    let msystemQty = document.getElementById("msystem-qty");
    // TV one
    let tvone = document.querySelector(".tvone");
    let tvoneLoad = document.getElementById("tvone-load");
    let tvoneQty = document.getElementById("tvone-qty");
    // TV two
    let tvtwo = document.querySelector(".tvtwo");
    let tvtwoLoad = document.getElementById("tvtwo-load");
    let tvtwoQty = document.getElementById("tvtwo-qty");
    // Refrigerator one
    let fridgeone = document.querySelector(".fridgeone");
    let fridgeoneLoad = document.getElementById("fridgeone-load");
    let fridgeoneQty = document.getElementById("fridgeone-qty");
    // Refrigerator two
    let fridgetwo = document.querySelector(".fridgetwo");
    let fridgetwoLoad = document.getElementById("fridgetwo-load");
    let fridgetwoQty = document.getElementById("fridgetwo-qty");
    // Refrigerator three
    let fridgethree = document.querySelector(".fridgethree");
    let fridgethreeLoad = document.getElementById("fridgethree-load");
    let fridgethreeQty = document.getElementById("fridgethree-qty");
    // Refrigerator four
    let fridgefour = document.querySelector(".fridgefour");
    let fridgefourLoad = document.getElementById("fridgefour-load");
    let fridgefourQty = document.getElementById("fridgefour-qty");
    // AC one
    let acone = document.querySelector(".acone");
    let aconeLoad = document.getElementById("acone-load");
    let aconeQty = document.getElementById("acone-qty");
    // AC two
    let actwo = document.querySelector(".actwo");
    let actwoLoad = document.getElementById("actwo-load");
    let actwoQty = document.getElementById("actwo-qty");
    // AC three
    let acthree = document.querySelector(".acthree");
    let acthreeLoad = document.getElementById("acthree-load");
    let acthreeQty = document.getElementById("acthree-qty");
    // Desktop
    let desktop = document.querySelector(".desktop");
    let desktopLoad = document.getElementById("desktop-load");
    let desktopQty = document.getElementById("desktop-qty");
    // Laptop
    let laptop = document.querySelector(".laptop");
    let laptopLoad = document.getElementById("laptop-load");
    let laptopQty = document.getElementById("laptop-qty");
    // Toaster
    let toaster = document.querySelector(".toaster");
    let toasterLoad = document.getElementById("toaster-load");
    let toasterQty = document.getElementById("toaster-qty");
    // Washing Machine
    let washingmachine = document.querySelector(".washingmachine");
    let washingmachineLoad = document.getElementById("washingmachine-load");
    let washingmachineQty = document.getElementById("washingmachine-qty");
    // Gaming Console
    let gamingconsole = document.querySelector(".gamingconsole");
    let gamingconsoleLoad = document.getElementById("gamingconsole-load");
    let gamingconsoleQty = document.getElementById("gamingconsole-qty");
    // Microwave Oven
    let microwaveoven = document.querySelector(".microwaveoven");
    let microwaveovenLoad = document.getElementById("microwaveoven-load");
    let microwaveovenQty = document.getElementById("microwaveoven-qty");
    // Other
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
    // Bulb
    function selectBulb() {
      bulb.classList.toggle("selected");

      if (bulb.classList.contains("selected")) {
        bulbQty.classList.add("active");
        bulbLoad.classList.add("active", "load-active");
        bulbQty.value = 1;
        bulbQty.disabled = false;
      } else {
        bulbQty.classList.remove("active");
        bulbLoad.classList.remove("active", "load-active");
        bulbQty.value = 0;
        bulbLoad.value = 0;
        bulbQty.disabled = true;
      }
    }

    // Tube Light
    function selectTlight() {
      tlight.classList.toggle("selected");
      if (tlight.classList.contains("selected")) {
        tlightQty.classList.add("active");
        tlightLoad.classList.add("active", "load-active");
        tlightQty.value = 1;
        tlightQty.disabled = false;
      } else {
        tlightQty.classList.remove("active");
        tlightLoad.classList.remove("active", "load-active");
        tlightQty.value = 0;
        tlightLoad.value = 0;
        tlightQty.disabled = true;
      }
    }

    // LED Lamp
    function selectLedlamp() {
      ledlamp.classList.toggle("selected");
      if (ledlamp.classList.contains("selected")) {
        ledlampQty.classList.add("active");
        ledlampLoad.classList.add("active", "load-active");
        ledlampQty.value = 1;
        ledlampQty.disabled = false;
      } else {
        ledlampQty.classList.remove("active");
        ledlampLoad.classList.remove("active", "load-active");
        ledlampQty.value = 0;
        ledlampLoad.value = 0;
        ledlampQty.disabled = true;
      }
    }

    // Fan
    function selectFan() {
      fan.classList.toggle("selected");
      if (fan.classList.contains("selected")) {
        fanQty.classList.add("active");
        fanLoad.classList.add("active", "load-active");
        fanQty.value = 1;
        fanQty.disabled = false;
      } else {
        fanQty.classList.remove("active");
        fanLoad.classList.remove("active", "load-active");
        fanQty.value = 0;
        fanLoad.value = 0;
        fanQty.disabled = true;
      }
    }

    // Music system
    function selectMsystem() {
      msystem.classList.toggle("selected");
      if (msystem.classList.contains("selected")) {
        msystemQty.classList.add("active");
        msystemLoad.classList.add("active", "load-active");
        msystemQty.value = 1;
        msystemQty.disabled = false;
      } else {
        msystemQty.classList.remove("active");
        msystemLoad.classList.remove("active", "load-active");
        msystemQty.value = 0;
        msystemLoad.value = 0;
        msystemQty.disabled = true;
      }
    }

    // TV one
    function selectTvone() {
      tvone.classList.toggle("selected");
      if (tvone.classList.contains("selected")) {
        tvoneQty.classList.add("active");
        tvoneLoad.classList.add("active", "load-active");
        tvoneQty.value = 1;
        tvoneQty.disabled = false;
      } else {
        tvoneQty.classList.remove("active");
        tvoneLoad.classList.remove("active", "load-active");
        tvoneQty.value = 0;
        tvoneLoad.value = 0;
        tvoneQty.disabled = true;
      }
    }

    // TV two
    function selectTvtwo() {
      tvtwo.classList.toggle("selected");
      if (tvtwo.classList.contains("selected")) {
        tvtwoQty.classList.add("active");
        tvtwoLoad.classList.add("active", "load-active");
        tvtwoQty.value = 1;
        tvtwoQty.disabled = false;
      } else {
        tvtwoQty.classList.remove("active");
        tvtwoLoad.classList.remove("active", "load-active");
        tvtwoQty.value = 0;
        tvtwoLoad.value = 0;
        tvtwoQty.disabled = true;
      }
    }

    // Gaming Console
    function selectGamingconsole() {
      gamingconsole.classList.toggle("selected");
      if (gamingconsole.classList.contains("selected")) {
        gamingconsoleQty.classList.add("active");
        gamingconsoleLoad.classList.add("active", "load-active");
        gamingconsoleQty.value = 1;
        gamingconsoleQty.disabled = false;
      } else {
        gamingconsoleQty.classList.remove("active");
        gamingconsoleLoad.classList.remove("active", "load-active");
        gamingconsoleQty.value = 0;
        gamingconsoleLoad.value = 0;
        gamingconsoleQty.disabled = true;
      }
    }

    // Microwave Oven
    function selectMicrowaveoven() {
      microwaveoven.classList.toggle("selected");
      if (microwaveoven.classList.contains("selected")) {
        microwaveovenQty.classList.add("active");
        microwaveovenLoad.classList.add("active", "load-active");
        microwaveovenQty.value = 1;
        microwaveovenQty.disabled = false;
      } else {
        microwaveovenQty.classList.remove("active");
        microwaveovenLoad.classList.remove("active", "load-active");
        microwaveovenQty.value = 0;
        microwaveovenLoad.value = 0;
        microwaveovenQty.disabled = true;
      }
    }

    // Load calculators
    // Gaming Console
    function totalGamingconsoleLoad() {
      gamingconsoleLoad.value = gamingconsoleQty.value * 200;
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

    async function postForm(url, formBody) {

      //const formData = new URLSearchParams(new FormData(formBody)); 

      try {
          const response = await fetch(url, {
              method: "POST",
              headers: new Headers({
                "Access-Control-Allow-Origin": "*", 
                "Access-Control-Allow-Methods": "POST, PUT, DELETE, GET",
                "Access-Control-Request-Method": "*", 
                "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept, Authorization",
              }),
              body: formBody, 
              cache: "no-cache",
          });

          if (!response.ok) {
              const message = `An error has occured: ${response.status}`;
              throw new Error(message);
          }

          return await response.json();
      } catch (error) {
          console.log("Fetch error: ", error);
          
      }
    }

    // Refrigerator one
    function selectFridgeone() {
      fridgeone.classList.toggle("selected");
      if (fridgeone.classList.contains("selected")) {
        fridgeoneQty.classList.add("active");
        fridgeoneLoad.classList.add("active", "load-active");
        fridgeoneQty.value = 1;
        fridgeoneQty.disabled = false;
      } else {
        fridgeoneQty.classList.remove("active");
        fridgeoneLoad.classList.remove("active", "load-active");
        fridgeoneQty.value = 0;
        fridgeoneLoad.value = 0;
        fridgeoneQty.disabled = true;
      }
    }

    // Refrigerator two
    function selectFridgetwo() {
      fridgetwo.classList.toggle("selected");
      if (fridgetwo.classList.contains("selected")) {
        fridgetwoQty.classList.add("active");
        fridgetwoLoad.classList.add("active", "load-active");
        fridgetwoQty.value = 1;
        fridgetwoQty.disabled = false;
      } else {
        fridgetwoQty.classList.remove("active");
        fridgetwoLoad.classList.remove("active", "load-active");
        fridgetwoQty.value = 0;
        fridgetwoLoad.value = 0;
        fridgetwoQty.disabled = true;
      }
    }

    // Refrigerator three
    function selectFridgethree() {
      fridgethree.classList.toggle("selected");
      if (fridgethree.classList.contains("selected")) {
        fridgethreeQty.classList.add("active");
        fridgethreeLoad.classList.add("active", "load-active");
        fridgethreeQty.value = 1;
        fridgethreeQty.disabled = false;
      } else {
        fridgethreeQty.classList.remove("active");
        fridgethreeLoad.classList.remove("active", "load-active");
        fridgethreeQty.value = 0;
        fridgethreeLoad.value = 0;
        fridgethreeQty.disabled = true;
      }
    }

    // Refrigerator four
    function selectFridgefour() {
      fridgefour.classList.toggle("selected");
      if (fridgefour.classList.contains("selected")) {
        fridgefourQty.classList.add("active");
        fridgefourLoad.classList.add("active", "load-active");
        fridgefourQty.value = 1;
        fridgefourQty.disabled = false;
      } else {
        fridgefourQty.classList.remove("active");
        fridgefourLoad.classList.remove("active", "load-active");
        fridgefourQty.value = 0;
        fridgefourLoad.value = 0;
        fridgefourQty.disabled = true;
      }
    }

    // AC one
    function selectAcone() {
      acone.classList.toggle("selected");
      if (acone.classList.contains("selected")) {
        aconeQty.classList.add("active");
        aconeLoad.classList.add("active", "load-active");
        aconeQty.value = 1;
        aconeQty.disabled = false;
      } else {
        aconeQty.classList.remove("active");
        aconeLoad.classList.remove("active", "load-active");
        aconeQty.value = 0;
        aconeLoad.value = 0;
        aconeQty.disabled = true;
      }
    }

    // AC two
    function selectActwo() {
      actwo.classList.toggle("selected");
      if (actwo.classList.contains("selected")) {
        actwoQty.classList.add("active");
        actwoLoad.classList.add("active", "load-active");
        actwoQty.value = 1;
        actwoQty.disabled = false;
      } else {
        actwoQty.classList.remove("active");
        actwoLoad.classList.remove("active", "load-active");
        actwoQty.value = 0;
        actwoLoad.value = 0;
        actwoQty.disabled = true;
      }
    }

    // AC three
    function selectActhree() {
      acthree.classList.toggle("selected");
      if (acthree.classList.contains("selected")) {
        acthreeQty.classList.add("active");
        acthreeLoad.classList.add("active", "load-active");
        acthreeQty.value = 1;
        acthreeQty.disabled = false;
      } else {
        acthreeQty.classList.remove("active");
        acthreeLoad.classList.remove("active", "load-active");
        acthreeQty.value = 0;
        acthreeLoad.value = 0;
        acthreeQty.disabled = true;
      }
    }

    // Desktop Computer
    function selectDesktop() {
      desktop.classList.toggle("selected");
      if (desktop.classList.contains("selected")) {
        desktopQty.classList.add("active");
        desktopLoad.classList.add("active", "load-active");
        desktopQty.value = 1;
        desktopQty.disabled = false;
      } else {
        desktopQty.classList.remove("active");
        desktopLoad.classList.remove("active", "load-active");
        desktopQty.value = 0;
        desktopLoad.value = 0;
        desktopQty.disabled = true;
      }
    }

    // Laptop
    function selectLaptop() {
      laptop.classList.toggle("selected");
      if (laptop.classList.contains("selected")) {
        laptopQty.classList.add("active");
        laptopLoad.classList.add("active", "load-active");
        laptopQty.value = 1;
        laptopQty.disabled = false;
      } else {
        laptopQty.classList.remove("active");
        laptopLoad.classList.remove("active", "load-active");
        laptopQty.value = 0;
        laptopLoad.value = 0;
        laptopQty.disabled = true;
      }
    }

    // Toaster
    function selectToaster() {
      toaster.classList.toggle("selected");
      if (toaster.classList.contains("selected")) {
        toasterQty.classList.add("active");
        toasterLoad.classList.add("active", "load-active");
        toasterQty.value = 1;
        toasterQty.disabled = false;
      } else {
        toasterQty.classList.remove("active");
        toasterLoad.classList.remove("active", "load-active");
        toasterQty.value = 0;
        toasterLoad.value = 0;
        toasterQty.disabled = true;
      }
    }

    // Washing Machine
    function selectWashingmachine() {
      washingmachine.classList.toggle("selected");
      if (washingmachine.classList.contains("selected")) {
        washingmachineQty.classList.add("active");
        washingmachineLoad.classList.add("active", "load-active");
        washingmachineQty.value = 1;
        washingmachineQty.disabled = false;
      } else {
        washingmachineQty.classList.remove("active");
        washingmachineLoad.classList.remove("active", "load-active");
        washingmachineQty.value = 0;
        washingmachineLoad.value = 0;
        washingmachineQty.disabled = true;
      }
    }

    // Load calculators
    // Bulb
    function totalBulbLoad() {
      bulbLoad.value = bulbQty.value * 60;
    }
    // Tube light
    function totalTlightLoad() {
      tlightLoad.value = tlightQty.value * 18;
    }

    // LED Lamp
    function totalLedlampLoad() {
      ledlampLoad.value = ledlampQty.value * 15;
    }

    // Fan
    function totalFanLoad() {
      fanLoad.value = fanQty.value * 70;
    }

    // Music system
    function totalMsystemLoad() {
      msystemLoad.value = msystemQty.value * 320;
    }

    // TV one
    function totalTvoneLoad() {
      tvoneLoad.value = tvoneQty.value * 150;
    }

    // TV two
    function totalTvtwoLoad() {
      tvtwoLoad.value = tvtwoQty.value * 200;
    }

    // Refrigerator one
    function totalFridgeoneLoad() {
      fridgeoneLoad.value = fridgeoneQty.value * 150;
    }

    // Refrigerator two
    function totalFridgetwoLoad() {
      fridgetwoLoad.value = fridgetwoQty.value * 210;
    }

    // Refrigerator three
    function totalFridgethreeLoad() {
      fridgethreeLoad.value = fridgethreeQty.value * 320;
    }

    // Refrigerator four
    function totalFridgefourLoad() {
      fridgefourLoad.value = fridgefourQty.value * 460;
    }

    // AC one
    function totalAconeLoad() {
      aconeLoad.value = aconeQty.value * 1120;
    }

    // AC two
    function totalActwoLoad() {
      actwoLoad.value = actwoQty.value * 1830;
    }

    // AC three
    function totalActhreeLoad() {
      acthreeLoad.value = acthreeQty.value * 2500;
    }

    // Desktop Computer
    function totalDesktopLoad() {
      desktopLoad.value = desktopQty.value * 200;
    }

    // Laptop
    function totalLaptopLoad() {
      laptopLoad.value = laptopQty.value * 100;
    }

    // Toaster
    function totalToasterLoad() {
      toasterLoad.value = toasterQty.value * 800;
    }

    // Washing Machine
    function totalWashingmachineLoad() {
      washingmachineLoad.value = washingmachineQty.value * 1000;
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

    document.forms.inverter_load_form?.addEventListener("submit", function (event) {
      event.preventDefault();
      const mee = this;
      const btn_submit = event.target.querySelector("button[type=submit]");

      if (requiredForm(mee)) {
        btn_submit.disabled = true;
        readOnly(mee);

        var formData = new FormData(document.querySelector("#inverter_load_form"));   
        formData.append("watts", totalLoad.value);
        formData.append("rating", rating.value);
        formData.append("battery", batteryVolt.value);
        formData.append("capacity", batteryCapacity.value);
        formData.append("backup", backupTime.value);
        formData.append("price", loadPrice.value);

        Swal.fire({
          title: 'Please Wait!',
          text: 'Your request is currently being processed.',
          allowOutsideClick: false,
          allowEscapeKey: false,
          timerProgressBar: true,
          didOpen: () => {
            Swal.showLoading()
          }
        });

        postForm('https://elhadjseck.com/luminous-load-calculator/inverter-form.php', formData).then((resp) => {
          btn_submit.disabled = false;
          readOnly(mee, false);
          Swal.close();

          if (resp.status == true) {
            Swal.fire({
              title: 'Successful!',
              text: 'We appreciate you taking the time to complete this form, and we will get in touch with you as soon as we can.',
              icon: 'success',
              allowOutsideClick: false,
              allowEscapeKey: false
            });
            mee.reset();

          }else{
            Swal.fire({
              title: 'Oh Sorry!',
              text: 'There appeared to be a problem while processing your request; try again',
              footer: 'Please refresh your browser',
              icon: 'erorr',
              confirmButtonText: 'Return',
              confirmButtonColor: "#d33",
              allowOutsideClick: false,
              allowEscapeKey: false
            });
          }
        });

      }else{
        Swal.fire({
          title: 'Oh Sorry!',
          text: 'We apologize, but you have not yet completed the necessary fields.',
          footer: 'Please complete all form fields',
          icon: 'warning',
          confirmButtonText: 'Return',
          confirmButtonColor: "#d33",
          allowOutsideClick: false,
          allowEscapeKey: false
        });

      }
    });
