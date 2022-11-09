import { createApp } from 'vue';
import App from './App.vue'
import router from './router'
import store from './store'
// import axios from 'axios'
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import 'firebase/compat/firestore';


// Vue.prototype.$axios = axios;
// Vue.config.productionTip = false;


const firebaseConfig = {
    apiKey: "AIzaSyCIlhnOKeVyCWg7DS2_iNlUjIHoOUuT2sQ",
    authDomain: "ftt-website-project.firebaseapp.com",
    projectId: "ftt-website-project",
    storageBucket: "ftt-website-project.appspot.com",
    messagingSenderId: "418944536974",
    appId: "1:418944536974:web:e5854f587d68b417f594df"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);



createApp(App).use(store).use(router).mount('#app')
