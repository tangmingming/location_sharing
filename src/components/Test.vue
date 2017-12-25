<template>
  <test_1 :title="location"></test_1>
</template>

<script>
  import test_1 from "./Test_1.vue"
  export default {
    data(){
      return {
        location:"llll"
      }
    },
    components:{
      test_1: test_1
    }
  }
</script>
