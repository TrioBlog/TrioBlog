<template>
  <div>
  <div>
    <CreatePost />
  </div>
  <div v-for="post in fetchSinglePost" :key="post.id">
    <Post :post="post" />
  </div>
  </div>
</template>

<script>
import Post from '../components/Post'
import CreatePost from '../components/CreatePost'
import axios from 'axios'
import BASE_URL from '../globals'

export default{
name: 'Home',
components:{
  CreatePost,
  Post
},
data: () => ({

  postList: [],
  fetchSinglePost: [],
  commentLists: [],
  singleComments: ''
  }),
  mounted(){

  },
methods:{
    async getPosts(e) {
      e.preventDefault()
      const res = await axios.get()
      this.postlist = res.data
    },
    async getPostById(e) {
      e.preventDefault()
      const postId = this.$route.params.post_id
      const res = await axios.get(`${BASE_URL}/post/${postId}`)
      this.fetchSinglePost = res.data
      console.log(res)
}
    ,
     async getComments(e) {
      e.preventDefault()
      const res = await axios.get()
      this.postlist = res.data
}
}

}
</script>