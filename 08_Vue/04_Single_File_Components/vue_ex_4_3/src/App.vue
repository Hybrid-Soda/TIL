<template>
  <header>
    <Header />
  </header>

  <main class="container py-3">
    <GalleryList />
  </main>
</template>

<script setup>
import 'bootstrap/dist/css/bootstrap.min.css'
import Header from '@/components/Header.vue'
import GalleryList from '@/components/GalleryList.vue'
</script>

<style>
</style>
