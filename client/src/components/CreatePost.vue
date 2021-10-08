<template>
  <div>
    <div>
      <h2>Your Thoughts?</h2>
    </div>
    <div class="postFormContainer">
      <form @submit.prevent="onSubmit">
        <input
        name="title"
          :value="title"
          @input="handleChange"
        />
        <input
        name="body"
          :value="body"
          @input="handleChange"
        />
        <button class="postSubmit">Post</button>
      </form>
    </div>
  </div>
</template>

<script>
// import Post from './Post.vue'
// import {Client} from '../globals'
export default {
  name: 'CreatePost',
  methods:{
    handleChange(e){
      this.$emit('handleFormChange', e.target.name, e.target.value )
    },
    onSubmit(){
      this.$emit('handleSubmit')
    },
  }
}
</script>