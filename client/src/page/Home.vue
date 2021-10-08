<template>
  <div>
  <div>
    <CreatePost />
  </div> 
<div v-if="fetchSinglePost[0]" class="postContainer">
      <section v-for="post in fetchSinglePost" :key="post.id" class="postSection">
        <Post/>
      </section>
    </div>
  </div>
</template>

<script>
import Post from '../components/Post'
import CreatePost from '../components/CreatePost'

import BASE_URL, {Client} from '../globals'

export default{
name: 'Home',
components:{
  CreatePost,
  Post
},
data: () => ({

  // postList: [],
  fetchSinglePost: []
  // commentLists: [],
  // singleComments: ''
  }),
  mounted(){

  },
methods:{
    // async getPosts(e) {
    //   e.preventDefault()
    //   const res = await axios.get()
    //   this.postlist = res.data
    // },
    async getPostById(e) {
      e.preventDefault()
      const postId = this.$route.params.post_id
      const res = await Client.get(`${BASE_URL}/post/${postId}`)
      console.log(res)
      this.fetchSinglePost = res.data
}
    
//      async getComments(e) {
//       e.preventDefault()
//       const res = await axios.get()
//       this.postlist = res.data
// }
}
}


</script>