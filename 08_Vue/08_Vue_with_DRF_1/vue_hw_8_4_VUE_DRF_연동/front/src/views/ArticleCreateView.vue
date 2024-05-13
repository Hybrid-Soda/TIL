<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="store.createArticle(title, content)">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title">
      <label for="content">내용 : </label>
      <input type="text" id="content" v-model.trim="content">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'

const title = ref(null)
const content = ref(null)
const store = useArticleStore()
</script>

<style scoped>

</style>