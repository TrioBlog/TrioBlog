<template>
  <div>
  <form>
    <div>
    <input :value="typeComment"
          @input="handleChange"/>
    </div>
    <button>Add Comment</button>
  </form>
  </div>
</template>

<script>

export default{
name: 'Comment',
props:{
  
},data: () => ({
  typeComment: ''
  }),
methods:{
    handleChange(event){
      this.typeinput = event.target.value
    }
}
}

</script>