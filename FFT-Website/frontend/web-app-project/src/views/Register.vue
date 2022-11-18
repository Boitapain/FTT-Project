<template>
    <div>
        <div v-if="error" class="error">{{error.message}}</div>
        <form @submit.prevent="pressedAPI">
            Register
            <div class="email">
                <input type="email" v-model="email" placeholder="email"> 
            </div>
            <div class="firstname">
                <input type="text" v-model="firstname" placeholder="firstname"> 
            </div>
            <div class="lastname">
                <input type="text" v-model="lastname" placeholder="lastname"> 
            </div>
            <div class="financial_inst">
                <input type="text" v-model="financial_inst" placeholder="financial_inst"> 
            </div>
            <div class="password">
                <input type="password" v-model="password" placeholder="password">   
            </div>
            <button type="submit">Register</button>
        </form>
    </div>
</template>
<script>
    // import * as firebase from "firebase/compat/app";
    import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
    
    export default{
        name: 'RegisterPage',
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
                    body:JSON.stringify({subject:'register', firstname:this.firstname, lastname: this.lastname, email: this.email, password: this.password, financial_inst: this.financial_inst})}).then(res=>{
                            if(res.ok){
                                return res.json()
                            }else{
                                alert("something is wrong")
                            }
                        }).then(data=>{    
                            // Log the response data in the console
                            document.cookie = "login=" + this.email + ";"
                            console.log(data)
                        } 
                        ).catch((err) => console.error(err));
            },
            async pressed(){
                try{
                    const auth = getAuth();
                    createUserWithEmailAndPassword(auth, this.email, this.password)
                    .then((userCredential) => {
                        const user = userCredential.user;
                        console.log(user);
                        this.$router.replace({name: "login"});
                    })
                }
                catch(err){ 
                    console.log(err);
                }
                
            }
        },
        data() {
            return{
                email: "",
                firstname: "",
                lastname: "",
                password: '',
                financial_inst: '',
                error: ''
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