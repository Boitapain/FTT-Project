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
    input{
        width: 400px;
        padding: 30px;
        margin: 20px;
        font-size: 21px;
    }
    button{
        width: 400px;
        height: 75px;
        font-size: 100%;
    }
</style>