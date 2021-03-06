const removeHomeUsageButtons = document.querySelectorAll(".rhu");
const removeVehicleUsageButtons = document.querySelectorAll(".rvu");
const removeFlightButtons = document.querySelectorAll(".rf");
let totalElectricityCarbonAmount;
let totalVehicleCarbonAmount;
let totalFlightCarbonAmount = 0;

//Calculate a Users Electricity Usage
function calculateElectricity() {
  let electricityUsage = document.querySelectorAll(".electricUsage");
  let totalUsage = [0];
  for (let usage of electricityUsage) {
    totalUsage.push(parseInt(usage.innerHTML));
  }
  let totalElectricityUsageAmount = totalUsage.reduce((a, b) => a + b);
  let totalElectricityAmount = document.querySelector("#totalElectricityUsage");
  totalElectricityAmount.innerHTML = totalElectricityUsageAmount;

  let electricityCarbon = document.querySelectorAll(".electricCarbon");
  let totalCarbon = [0];
  for (let usage of electricityCarbon) {
    totalCarbon.push(parseInt(usage.innerHTML));
  }
  totalElectricityCarbonAmount = totalCarbon.reduce((a, b) => a + b);
  let totalElectricityCarbon = document.querySelector(
    "#totalElectricityCarbon"
  );
  totalElectricityCarbon.innerHTML = totalElectricityCarbonAmount;
}

//Calculate a Users Vehicle Usage
function calculateVehicle() {
  let vehicleMileage = document.querySelectorAll(".vehicleMileage");
  let totalMileage = [0];
  for (let usage of vehicleMileage) {
    totalMileage.push(parseInt(usage.innerHTML));
  }
  let totalVehicleMileageAmount = totalMileage.reduce((a, b) => a + b);
  let totalVehicleMileage = document.querySelector("#totalVehicleMileage");
  totalVehicleMileage.innerHTML = totalVehicleMileageAmount;

  let vehicleCarbon = document.querySelectorAll(".vehicleCarbon");
  let totalCarbon = [0];
  for (let usage of vehicleCarbon) {
    totalCarbon.push(parseInt(usage.innerHTML));
  }
  totalVehicleCarbonAmount = totalCarbon.reduce((a, b) => a + b);
  let totalVehicleCarbon = document.querySelector("#totalVehicleCarbon");
  totalVehicleCarbon.innerHTML = totalVehicleCarbonAmount;
}

//Calculate a Users Flight Usage
function calculateFlight() {
  let flightMileage = document.querySelectorAll(".flightMileage");
  let totalMileage = [0];
  for (let usage of flightMileage) {
    totalMileage.push(parseInt(usage.innerHTML));
  }
  let totalFlightMileageAmount = totalMileage.reduce((a, b) => a + b);
  let totalFlightMileage = document.querySelector("#totalFlightMileage");
  totalFlightMileage.innerHTML = totalFlightMileageAmount;

  let flightCarbon = document.querySelectorAll(".flightCarbon");
  let totalCarbon = [0];
  for (let usage of flightCarbon) {
    totalCarbon.push(parseInt(usage.innerHTML));
  }
  totalFlightCarbonAmount = totalCarbon.reduce((a, b) => a + b);
  let totalFlightCarbon = document.querySelector("#totalFlightCarbon");
  totalFlightCarbon.innerHTML = totalFlightCarbonAmount;
}


//Caculate a User's total Footprint
function calculateTotal() {
    let totals = [0];
    if(totalElectricityCarbonAmount) {
      totals.push(totalElectricityCarbonAmount);
    }
    if(totalVehicleCarbonAmount) {
      totals.push(totalVehicleCarbonAmount);
    }
    if(totalFlightCarbonAmount) {
      totals.push(totalFlightCarbonAmount);
    }
    
    totalCarbonAmount = totals.reduce((a,b) => a + b)



  let totalCarbon = document.querySelector("#totalFootprint");
  totalCarbon.innerHTML = totalCarbonAmount;
}

// Delete a Home Usage
for (let btn of removeHomeUsageButtons) {
  btn.addEventListener("click", function (e) {
    deleteHomeUsage(e.target.parentElement.parentElement.id);

    e.target.parentElement.parentElement.remove();
    calculateElectricity();
    calculateTotal();
  });
}

async function deleteHomeUsage(id) {
  await axios.post(`/homeUsage/${id}/delete`);
}

// Delete Vehicle Usage
for (let btn of removeVehicleUsageButtons) {
  btn.addEventListener("click", function (e) {
    deleteVehicleUsage(e.target.parentElement.parentElement.id);

    e.target.parentElement.parentElement.remove();
    calculateVehicle();
    calculateTotal();
  });
}
async function deleteVehicleUsage(id) {
  await axios.post(`/vehicleUsage/${id}/delete`);
}

// Delete Flight
for (let btn of removeFlightButtons) {
  btn.addEventListener("click", function (e) {
    deleteFlight(e.target.parentElement.parentElement.id);

    e.target.parentElement.parentElement.remove();
    calculateFlight();
    calculateTotal();
  });
}
async function deleteFlight(id) {
  await axios.post(`/flight/${id}/delete`);
}

//Calculate All Usgaes
function calculateAll() {
  calculateElectricity();
  calculateVehicle();
  calculateFlight();
  calculateTotal();
}

calculateAll();
