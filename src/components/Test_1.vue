<template>
  <el-container>
    <el-header>Header{{ title }}</el-header>
    <el-main style="">Main</el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
  export default {
    props: ["title"]
  }
</script>
