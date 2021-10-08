<template>
  <div>
    <div>
      <h2>Your Thoughts?</h2>
    </div>
    <div>
      <form >
        <input
          :value="typeinput"
          @input="handleChange"
        />
        <button>Post</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreatePost',
  data: () => ({
  typeinput: '',
  singlePost: []
  }),
  methods:{
    handleChange(event){
      this.typeinput = event.target.value
    },
    onSubmit(){
     this.$router.push(`/posts`)
    },

    }

  }
</script>