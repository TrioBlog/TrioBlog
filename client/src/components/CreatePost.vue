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
    <div v-if="allPosts[0]" class="postContainer">
      <section v-for="post in allPosts" :key="post.id" class="postSection">
        <Post/>
      </section>
    </div>
  </div>
</template>

<script>
import Post from './Post.vue'
export default {
  components: { Post },
  name: 'CreatePost',
  // props: ['username']
  data: () => ({
  postTitle: '',
  postBody: '',
  allPosts: [],
  user_name: ''
  }),
  methods:{
    handleChange(event){
      event.target.value = event.target.value
    },
    onSubmit(){
      body = {
        "user_name": this.user_name,
        "body": this.postBody,
        "title": this.postTitle
      }
      Client.post('/post', body)
    },

    }

  }
</script>