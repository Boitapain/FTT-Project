<template>
  <div class="home">
    Home

  </div>

</template>
<script>




var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();

today = yyyy + '/' + dd + '/' + mm;


function getdiff() {
  // Get the reciever endpoint from Python using fetch:
  fetch("http://127.0.0.1:5000/pricediff", 
    {
    method: 'POST',
    headers: {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    },
    body:JSON.stringify({stock:'tesla'})})
                        .then(res=>{
                                if(res.ok){
                                    return res.text()
                                }else{
                                    console.log("something is wrong")
                                }
                            })
                        .then((data)=>{    
                            // Log the response data in the console
                            console.log(data)
                        } 
                        ).catch((err) => console.error(err));
}
function getcryptopage() {
  // Get the reciever endpoint from Python using fetch:
  fetch("http://127.0.0.1:5000/cryptopage", 
    {
    method: 'POST',
    headers: {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    },
    body:JSON.stringify({crypto:'bitcoin'})})
                        .then(res=>{
                                if(res.ok){
                                    return res.text()
                                }else{
                                    console.log("something is wrong")
                                }
                            })
                        .then((data)=>{    
                            // Log the response data in the console
                            console.log(data)
                        } 
                        ).catch((err) => console.error(err));
}

function purchase() {
  // Get the reciever endpoint from Python using fetch:
  fetch("http://127.0.0.1:5000/purchase", 
    {
    method: 'POST',
    headers: {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    },
    body:JSON.stringify({email:'jeremieblanc@gmail.com', purchaseAmount:'500.00', asset:'amd', date:today })})
                        .then(res=>{
                                if(res.ok){
                                    return res.text()
                                }else{
                                    console.log("something is wrong")
                                }
                            })
                        .then((data)=>{    
                            // Log the response data in the console
                            console.log(data)
                        } 
                        ).catch((err) => console.error(err));
}


getdiff();
getcryptopage();
purchase();
  
</script>
