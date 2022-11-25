<template>
    <div>
        <form @submit.prevent="pressedAPI">
            Login
            <div class="login">
                <input type="email" v-model="email" placeholder="login"> 
            </div>
            <div class="password">
                <input type="password" v-model="password" placeholder="password">   
            </div>
            <button type="submit">Login</button>
        </form>
        <div class="error" v-if="error">{{error.message}}</div>
        <span>Click here to <RouterLink to='/register'>Register</RouterLink></span>

    </div>
</template>
<script>
    // import * as firebase from "firebase/compat/app";
    import {getAuth, signInWithEmailAndPassword } from "firebase/auth";

    export default{
        name: 'LoginPage',
        data() {
            return {
                email: "",
                password: '',
                error: ''
            }
        },
        methods: {
            pressedAPI(){
                // Get the reciever endpoint from Python using fetch:
                fetch("http://127.0.0.1:5000/", 
                    {
                        method: 'POST',
                        headers: {
                            'Content-type': 'application/json',
                            'Accept': 'application/json'
                        },
                    body:JSON.stringify({subject:'login', email: this.email, password: this.password})}).then(res=>{
                            if(res.ok){
                                return res.text()
                            }else{
                                alert("something is wrong")
                            }
                        }).then(data=>{    
                            // Log the response data in the console
                            console.log(data)
                            if(data == "successful"){
                                this.$router.replace({name: "home"});
                            }
                            else{
                                alert(data);
                            }
                        } 
                        ).catch((err) => console.error(err));
            },
            async pressed() {
                try{
                    const auth = getAuth();
                    const val = await signInWithEmailAndPassword(auth, this.email, this.password);
                    console.log(val);
                    this.$router.replace({name: "clients"});
                }
                catch(e){
                    console.log(e);
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    .error {
        color: red;
        font-size: 18px;
    }

    html, body {
        height: 100%;
        margin: 0;
        padding: 0;
    }

    #app{
        height: 100%;
        
    }

    input{
        width: 300px;
        height: 10px;
        padding: 20px;
        margin: 15px;
        font-size: 21px;
        border-radius: 5px;
        background-color: #EEEEEE;
        border: 4px solid #393e4600;
    }

    // palette: https://colorhunt.co/palette/232931393e464ecca3eeeeee
    
    button{
        width: 300px;
        height: 45px;
        font-size: 100%;
        margin-top: 2%;
        background-color: #4ECCA3;
    }
    button:hover{
        cursor: pointer;
        background-color: #232931;
        border: 3px solid #4ECCA3;
        color: #4ECCA3;
        transition: 0.2s;
    }
    input:hover{
        border: 4px solid #393E46;
        transition: 0.2s;
    }
</style>