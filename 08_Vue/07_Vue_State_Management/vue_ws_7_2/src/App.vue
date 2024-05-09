<template>
  <header class="header">
    <div>
      <nav class="nav">
        <RouterLink :to="{ name: 'home' }" class="nav-link">Home</RouterLink>
        <RouterLink :to="{ name: 'products' }" class="nav-link">Products</RouterLink>
        <RouterLink :to="{ name: 'favorite' }" class="nav-link">Favorite</RouterLink>
      </nav>
    </div>
  </header>

  <main class="main">
    <RouterView />
  </main>
</template>

<script setup>
import { ref } from 'vue'

</script>

<style scoped>
.header {
  background-color: #333;
  color: white;
  padding: 10px 0;
}

.wrapper {
  max-width: 1200px;
  margin: 0 auto;
}

.nav {
  display: flex;
  justify-content: center;
}

.nav-link {
  color: white;
  text-decoration: none;
  margin: 0 15px;
  font-size: 18px;
}

.main {
  padding: 20px;
}
</style>