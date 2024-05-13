<template>
  <div 
    v-for="article, idx  in store.articles"
    :key="article.id"
    >
    <h3>{{ idx+1 }}번 게시글</h3>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p><hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

defineProps({
  article: Object
})
</script>

<style lang="scss" scoped>

</style>