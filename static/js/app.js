

const removeHomeUsageButtons = document.querySelectorAll('.rhu')


for(let btn of removeHomeUsageButtons) {
    btn.addEventListener('click', function(e) {
        deleteUsage(e.target.parentElement.parentElement.id)
        
        e.target.parentElement.parentElement.remove()
    })
}

async function deleteUsage(id) {
    await axios.post(`/homeUsage/${id}/delete`)
}



