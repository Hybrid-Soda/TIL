<template>
  제목: {{ post.title }}
</template>

<script setup>
defineProps({ 
  post: Object 
})
</script>