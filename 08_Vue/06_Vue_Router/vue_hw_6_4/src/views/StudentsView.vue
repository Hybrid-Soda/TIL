<template>
<div>
  <h1>학생 상세 정보 목록 입니다.</h1>
  <RouterLink
  v-for="student in students" :key="student.name"
  :to="{ name: 'studentDetail',
  params: {'name': student.name} }"
  >
    <p>{{ student.name }} 학생 정보 보기</p>
  </RouterLink>
</div>
</template>

<script setup>
import { ref } from 'vue'
import router from '../router'

const students = [
  { name: '김하나' },
  { name: '김두리' },
  { name: '김서이' },
]
</script>

<style scoped>
</style>