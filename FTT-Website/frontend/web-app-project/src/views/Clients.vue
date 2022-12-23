<template>
    <div>
        List of clients:
    </div>
    <h3 v-if=!connected>Please connect to your account to see the clients</h3>
    <div class="list_of_clients">
        <div v-for="(client) in clients.clients" v-bind:key="client" class="client-line">
                <div v-for="(clientI) in client" v-bind:key="clientI" class="client-row">
                    <div>{{`${clientI}`}}</div>
                </div>
        </div>
    </div>
</template>
<script>


    export default{
        mounted() {
            this.getClients();
        },
        name: 'clientsVue',
        data() {
            return {
                clients: [],
                connected: false
            }
        },
        methods: {
            getClients() {
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
                            if(data != "not connected"){
                                this.clients = data
                                this.connected = true
                            }
                            else{
                                this.connected = false
                            }
                        } 
                        ).catch((err) => console.error(err));
            }
        }
    }
    
    
</script>

<style lang="scss" scoped>
    .client-line{
        height: 4em;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2%;
        margin-top: 1%;
        width: 50%;
        margin-left: 25%;
        border-radius: 4px;
        cursor: pointer;
    }
    .client-line:hover{
        background-color: #191d23;
    }

    .list_of_clients{
        margin-top: 3em;
    }
</style>