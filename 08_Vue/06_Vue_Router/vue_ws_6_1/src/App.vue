<template>
  <header class="container py-2 mb-5">
    <div class="card m-4">
      <h1 class="card-header py-4">Quiz 퀴즈</h1>
      <div class="card-body py-5">
        <h5 class="card-text">
          여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전하세요!
        </h5>
      </div>
    </div>

    <nav class="navbar navbar-expand bg-dark m-4" data-bs-theme="dark">
      <div class="container-fluid">
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav m-auto">
            <li class="nav-item">
              <RouterLink :to="{ name: 'home' }" class="nav-link">HOME</RouterLink>
            </li>
            <li class="navbar-text"> | </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <main class="container">
    <RouterView />
  </main>
</template>

<script setup>
import { ref } from 'vue'

</script>

<style scoped>
header {
  text-align: center;
  background-color: whitesmoke;
  font-weight: 600;
  width: 1000px;
}
.card-header {
  background-color: orange;
  color: white;
  font-weight: 600;
}
</style>