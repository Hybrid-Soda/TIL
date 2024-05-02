<template>
  <div>
    <h1>가수 목록</h1>
    <SingerDetail v-for="i in singers" :key="singer-id" />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/singers/SingerDetail.vue'

const singers = [
  { name : 'adele' },
  { name : 'maroon5' },
  { name : 'Dua Lipa' },
]
</script>

<style scoped>
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
}

h1 {
  color: orangered;
}
</style>