<template>
  <div class="flexCon">
    <div class="divCon">
      <h1>Sign Up</h1>
      <form @submit.prevent="onSubmit">
      <div>
        <h2>Username:</h2>
          <input type="username" :value="username" @input="handleChange" />
      </div>
      <div>
        <h2>Password:</h2>
          <input type="password" :value="password" @input="handlePass" />
      </div>
      <button type="submit" :disabled="username ==='' || password === ''">SignUp</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import { BASE_URL } from '../globals'
export default {
  name: 'SignUp',
  components:{
    
  },
  data: () => ({
    username: '',
    password: ''
    }),
  methods:{
  handleChange(event){
      this.username = event.target.value
    },
    handlePass(event){
      this.password = event.target.value
    },
    async onSubmit(){
      try {
      const res = await axios.post(`${BASE_URL}/user/register`, {"user_name": this.username, "password": this.password})
      console.log(res)
        this.username = ''
        this.password = ''
        this.$router.push(`/signin`)
      } catch (err) {
        console.log(err)
        alert("an error occurred when attempting try a defferent username")
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
  margin-top: 2vh;
  background-color: #CAF0F8;
  color: #03045E;
  border-radius: 2vh;
  border: 2px solid #03055ecf;
  width: 100px;
  height: 40px;
  font-size: 20px;
}
a {
  text-decoration: none;
  color: #03045E;
  font-size: 18px;
  background-color: #CAF0F8;
  padding: 6px;
  border-radius: 10px;
  border: 2px solid #03045E;
}
h1,h2 {
  margin: 1vh;
}
.flexCon {
  display: flex;
  justify-content: center;
}
.divCon {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  color: #03045E;
  background-color: #90E0EF;
  width: 30vh;
  height: 40vh;
  border-radius: 5vh;
}
</style>