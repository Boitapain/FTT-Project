<template>
    <div>
        Logged in
        <span v-if="loggedIn">Yes</span>
        <span v-else>No</span>
        <div>
            <button @click="signOut">Sign Out</button>
        </div>

    </div>
</template>
<script>

    // import * as firebase from "firebase/app";

    export default{
        name: 'LoggedPage',
        created(){

                fetch("http://127.0.0.1:5000/islogin")
                    .then((response) => response.text())
                    .then((data) =>{
                        console.log("test");
                        if(data == "true"){
                            this.loggedIn = true;
                        }
                        else{
                            this.loggedIn = false;
                        }
                    } 
                    ); 
            
        },
        data(){
            return {
                loggedIn: false
            }
        },
        methods: {
            signOut(){
                fetch("http://127.0.0.1:5000/logout")
                    .then((response) => response.text())
                    .then((data) =>{
                        if(data == "succes"){
                            this.loggedIn = true;
                            location.reload();
                        }
                        else{
                            alert(data);
                        }
                    } 
                    ); 
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>