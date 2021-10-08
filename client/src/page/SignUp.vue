<template>
  <div>
    <h1>Sign Up</h1>
    <form @submit.prevent="onSubmit">
    <div>
      <h2>Username:</h2>
        <input type="email" :value="username" @input="handleChange" />
    </div>
    <div>
      <h2>Password:</h2>
        <input type="password" :value="password" @input="handlePass" />
    </div>
    <button type="submit" :disabled="username ==='' || password === ''">SignUp</button>
    </form>
  </div>
</template>

<script>

export default{
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
    onSubmit(){
     this.$router.push(`/home`)
    }
}


}
</script>