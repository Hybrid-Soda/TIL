<template>
  <header class="header">
    <h1>명함 관리 페이지</h1>
  </header>

  <main class="main">
    <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    <article class="article">
      <CreateCardForm @create-card-event="updateCard"/>
      <BusinessCard :newCard="newCard" />
    </article>
  </main>
  <footer class="footer">
    <p>&copy; 2024 My Business Cards</p>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import BusinessCard from "./components/BusinessCard.vue"
import CreateCardForm from "./components/CreateCardForm.vue"

const newCard = ref({})
const updateCard = function (cardInfo) {
  newCard.value = cardInfo
}
</script>

<style scoped>
.header {
margin-inline: 35%;
display: flex;
justify-content: center;
background-color: #4a90e2;
color: white;
padding: 20px;
}

.main {
  text-align: center;
  display: flex;
  flex-direction: column;
  min-height: 100vh;

}

.article {
margin-top: 20px;
padding: 20px;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
padding: 20px;
background-color: #f4f4f4;
}
</style>
