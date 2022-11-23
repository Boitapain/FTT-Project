<template>
    <div>
        <!-- Logged in
        <span v-if="loggedIn">Yes</span>
        <span v-else>No</span>
        <div>
            <button @click="signOut">Sign Out</button>
        </div> -->

    </div>
</template>
<script>
    import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
    // import * as firebase from "firebase/app";

    export default{
        name: 'LoggedPage',
        // created() {
        //     onAuthStateChanged(user=>{
        //         this.loggedIn = !!user;
        //         if(user){
        //             this.loggedIn = true
        //         }
        //         else{
        //             this.loggedIn = false
        //         }
        //     })
        // },
        created(){
            const auth = getAuth();
            onAuthStateChanged(auth, (user) => {
                    this.loggedIn = !!user;
                });
        },
        data(){
            return {
                loggedIn: false
            }
        },
        methods: {
            async signOut(){
                const auth = getAuth();
                const data = await signOut(auth).then(() => {
                    console.log("signed out succefully!")
                    this.$router.replace({name: "login"})
                }).catch((error) => {
                    console.log(error)
                });
                console.log(data)
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>