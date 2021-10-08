<template>
  <div class="divCon">
    <h1>Sign In</h1>
    <form @submit.prevent="onSubmit" >
      <div>
        <h2>Username:</h2>
        <input type="username" :value="username" @input="handleChange"  />
      </div>
      <div>
        <h2>Password:</h2>
        <input type="password" :value="password" @input="handlePass" />
      </div>
      <div>
        <a href="/">New Account?</a>
      </div>
      <button type="submit" :disabled="username ==='' || password === ''">Sign In</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"
import {BASE_URL} from '../globals'
export default {
  name: 'SignIn',
  components: {},
  data: () => ({
    username: '',
    password: '',
  }),
  methods: {
    handleChange(event){
      this.username = event.target.value
    },
    handlePass(event){
      this.password = event.target.value
    },
    async onSubmit(){
      try {
      const res = await axios.post(`${BASE_URL}user/login`, {"user_name": this.username, "password": this.password})
      if (res.data){
        localStorage.setItem('token', res.data)
        this.password = ''
        this.$router.push({ path: `/home`, props: this.username })
      } else {
        alert("unauthorized")
      }
      } catch (err) {
        alert("an error occurred when attempting to sign in")
      }
    }
  }
}
</script>

<style scoped>
input {
  background-color: aqua;
  padding: 10px;
}
.divCon {
  text-align: center;
}
</style>