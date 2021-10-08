<template>
  <div class="flexCon">
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
        <div class="linkdiv">
          <a href="/">New Account?</a>
        </div>
        <button type="submit" :disabled="username ==='' || password === ''">Sign In</button>
      </form>
    </div>
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
        this.$router.push({ path: `/home`, props: {"username": this.username }})
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
  background-color: #CAF0F8;
  font-size: 24px;
  width: 175px;
  border-radius: 10px;
  border: 3px solid #03055e9b;
}
button {
  background-color: #CAF0F8;
  color: #03045E;
  border-radius: 2vh;
  border: 2px solid #03055ecf;
  width: 15vh;
  height: 7vh;
  font-size: 36px;
}
h1,h2 {
  margin: 2vh;
}
.flexCon {
  display: flex;
  justify-content: center;
}
.linkdiv {
  margin: 3vh;
  text-decoration: none;
  color: #03045E;
}
.divCon {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  color: #03045E;
  background-color: #90E0EF;
  width: 50vh;
  height: 75vh;
  border-radius: 5vh;
}
</style>