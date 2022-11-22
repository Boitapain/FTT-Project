<template>
  <top-header></top-header>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/secret">Secret</router-link> |
    <router-link to="/register">Register</router-link>
  </nav>
  <router-view/>
</template>

<script>
  import TopHeader from './components/Top-Header';
  export default {
    components: {'top-header': TopHeader}
  }
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #EEEEEE;
}

body{
  background-color: #232931;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #EEEEEE;

    &.router-link-exact-active {
      color: #4ECCA3;
    }
  }
}
</style>
