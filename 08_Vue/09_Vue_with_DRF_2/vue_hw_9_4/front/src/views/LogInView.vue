<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username"><br>

        <label for="password">password : </label>
        <input type="password" id="password" v-model.trim="password"><br>

        <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
  username: username.value,
  password: password.value,
  }
  store.logIn(payload)
}
</script>