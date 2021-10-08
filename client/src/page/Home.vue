<template>
  <div>
  <div>
    <CreatePost />
  </div>
  <div>
    <Post />
  </div>
  </div>
</template>

<script>
import Post from '../components/Post'
import CreatePost from '../components/CreatePost'
import axios from 'axios'

export default{
name: 'Home',
components:{
  CreatePost,
  Post
},
data: () => ({

  postList: [],
  singlePost: [],
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
    //  async getPostById() {
    //   const postid = parseInt(this.$route.params.post_id)
    //   const res = await axios.get(``)
    //   this.singlePost = res.data
    //   console.log(res)
    // },
     async getComments(e) {
      e.preventDefault()
      const res = await axios.get()
      this.postlist = res.data
}
}

}
</script>