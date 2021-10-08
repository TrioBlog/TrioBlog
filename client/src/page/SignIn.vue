<template>
  <div>
    <h1>Sign In</h1>
    <form @submit.prevent="onSubmit" >
      <div>
        <input type="username" :value="username" @input="handleChange"  />
      </div>
      <div>
        <input type="password" :value="password" @input="handlePass" />
      </div>
      <button type="submit" :disabled="username ==='' || password === ''">Sign In</button>
      <a href="/">New Account?</a>
    </form>
  </div>
</template>

<script>
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
    onSubmit(){
    this.$router.push(`/home`)
    }
  }
}
</script>