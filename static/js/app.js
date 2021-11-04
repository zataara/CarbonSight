

const removeHomeUsageButtons = document.querySelectorAll('.rhu')
const removeVehicleUsageButtons = document.querySelectorAll('.rvu')
const removeFlightButtons = document.querySelectorAll('.rf')

// Delete a Home Usage
for(let btn of removeHomeUsageButtons) {
    btn.addEventListener('click', function(e) {
        deleteHomeUsage(e.target.parentElement.parentElement.id)
        
        e.target.parentElement.parentElement.remove()
    })
}

async function deleteHomeUsage(id) {
    await axios.post(`/homeUsage/${id}/delete`)
}

// Delete Vehicle Usage
for(let btn of removeVehicleUsageButtons) {
    btn.addEventListener('click', function(e) {
        deleteVehicleUsage(e.target.parentElement.parentElement.id)
        
        e.target.parentElement.parentElement.remove()
    })
}
async function deleteVehicleUsage(id) {
    await axios.post(`/vehicleUsage/${id}/delete`)
}



// Delete Flight
for(let btn of removeFlightButtons) {
    btn.addEventListener('click', function(e) {
        deleteFlight(e.target.parentElement.parentElement.id)
        
        e.target.parentElement.parentElement.remove()
    })
}
async function deleteFlight(id) {
    await axios.post(`/flight/${id}/delete`)
}



