import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()
  const articles = ref([])
  const token = ref(null)

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(response => {
      console.log(response.data)
      articles.value = response.data
    })
    .catch(error => {
      console.log(error)
    })
  }

  const createArticle = function ({ title, content }) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        title,
        content,
      }
    })
    .then((res) => {
      router.push({ name: 'home' })
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: { username, password1, password2 }
    })
    .then(res => {
      const password = password1
      logIn({ username, password })
    })
    .catch(err => console.error(err))
  }

  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    })
    .then(res => {
      token.value = res.data.key
      router.push({ name: 'home' })
    })
    .catch(err => console.log(err))
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  return {
    articles, token, isLogin,
    getArticles, createArticle, signUp, logIn }
}, { persist: true })
