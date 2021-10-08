<template>
  <div>
    <div>
      <h2>Your Thoughts?</h2>
    </div>
    <div class="postFormContainer">
      <form >
        <input
          :value="postTitle"
          @input="handleChange"
        />
        <input
          :value="postBody"
          @input="handleChange"
        />
        <button class="postSubmit">Post</button>
      </form>
    </div>
  </div>
</template>

<script>
// import Post from './Post.vue'
export default {
  // components: { Post },
  name: 'CreatePost',
  // props: ['username']
  data: () => ({
  postTitle: '',
  postBody: '',
  user_name: ''
  }),
  methods:{
    // handleChange(event){
      // event.target.value = event.target.value
    // },
    onSubmit(){
      // body = {
      //   "user_name": this.user_name,
      //   "body": this.postBody,
      //   "title": this.postTitle
      // }
      // Client.post('/post', body)
    },
  }
}
</script>