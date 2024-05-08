<template>
  <div>
    <h3>{{ username }}이 작성한 게시글</h3>
    <ol>
      <li v-for="post in posts" :key="post.id">
        <RouterLink :to="{ name: 'post-detail', params: {'username': username, 'id':post.id } }">
          <PostListItem :post="post" />
        </RouterLink>
      </li>
    </ol>
  </div>
  <hr>
  <RouterView />
</template>

<script setup>
import { ref } from 'vue'
import { RouterView, useRoute } from 'vue-router'
import PostListItem from '@/components/PostListItem.vue'

const route = useRoute()
const username = ref(route.params.username)

const posts = ref([
  { id: 1, title: 'Post 1', content: 'Content 1', },
  { id: 2, title: 'Post 2', content: 'Content 2', },
  { id: 3, title: 'Post 3', content: 'Content 3', },
])
</script>

<style scoped>

</style>