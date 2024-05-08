<template>
  <div>
    <MainPage />

    <RouterLink :to="{ name: 'some' }">Some</RouterLink> |
    <RouterLink :to="{ name: 'other' }">Other</RouterLink> |
    <RouterLink :to="{ name: 'students' }">Students</RouterLink>

    <RouterView />
  </div>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import MainPage from '@/components/MainPage.vue'
</script>

<style scoped>

</style>
