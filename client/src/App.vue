<template>
  <div id="app">
    <div>
      <router-link to="/home"></router-link> |
      <router-link to="/"></router-link>
      <router-link to="/signin">Login</router-link>
      <!-- <router-link to="/posts"></router-link> -->
    </div>
    <router-view/>
  </div>
</template>

<style>
body {
  margin: 0;
}
#app {
  margin: 0;
  background-color: #0077B6;
  height: 100vh;
}
</style>