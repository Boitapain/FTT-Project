<template>
    <div>
        List of clients:
    </div>
</template>
<script>
    export default{
        name: 'clientsVue'
    }
    fetch("http://127.0.0.1:5000/getclients", 
                    {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json',
                            'Accept': 'application/json'
                        },
                    body:JSON.stringify({email: "test@test.fr"})}).then(res=>{
                            if(res.ok){
                                return res.json()
                            }else{
                                alert("something is wrong")
                            }
                        }).then(data=>{    
                            // Log the response data in the console
                            console.log(data)
                        } 
                        ).catch((err) => console.error(err));
</script>

<style lang="scss" scoped>

</style>