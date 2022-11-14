<template>
    <div>
        <form @submit.prevent="pressed">
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
                email: '',
                password: '',
                error: ''
            }
        },
        methods: {
            async pressed() {
                try{
                    const auth = getAuth();
                    const val = await signInWithEmailAndPassword(auth, this.email, this.password);
                    console.log(val);
                    this.$router.replace({name: "secret"});
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