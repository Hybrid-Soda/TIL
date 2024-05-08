<template>
<div>
  <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
  <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
  <h1>UserView</h1>
  <h2>{{ userId }}번 User 페이지</h2>
  <button @click="goHome">Home</button>
  <button @click="routeUpdate">100번 유저 페이지</button>
  <hr>
  <RouterView />
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function () {
  router.push({ name: 'home' })
  // router.replace({ name: 'home' }) -> 뒤로가기 못함 (history stack에 안쌓임)
}

// 컴포넌트 가드 1
onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

const routeUpdate = function () {
  router.push({ name: 'user', params: { id: 100 } })
}

// 컴포넌트 가드 2
onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>

<style scoped>

</style>