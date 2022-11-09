<template>
    <div>
        <div v-if="error" class="error">{{error.message}}</div>
        <form @submit.prevent="pressed">
            Register
            <div class="email">
                <input type="email" v-model="email" placeholder="email"> 
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
            async pressed(){
                try{
                    const auth = getAuth();
                    createUserWithEmailAndPassword(auth, this.email, this.password)
                    .then((userCredential) => {
                        const user = userCredential.user;
                        console.log(user);
                        this.$router.replace({name: "secret"});
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
                password: '',
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