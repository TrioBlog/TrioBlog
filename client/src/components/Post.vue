<template>
  <div>
  <div>
    
  </div>
  <div>
    <!-- <Comment /> -->
  </div>
  </div>
</template>

<script>
import axios from 'axios'

// import Comment from './Comment'
export default{
name: 'Post',
// components:{
//   Comment
// },
data: () => ({
  fetchSinglePost: []
  }),
methods:{
  async getPostById() {
      // const postid = parseInt(this.$route.params.post_id)
      const res = await axios.get(``)
      this.fetchSinglePost = res.
      console.log(res)
}
}
}

</script>