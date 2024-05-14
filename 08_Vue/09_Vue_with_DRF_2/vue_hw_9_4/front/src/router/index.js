import { createRouter, createWebHistory } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import HomeView from '@/views/HomeView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signUp',
      name: 'signUp',
      component: SignUpView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin) {
          window.alert('이미 로그인이 되어있습니다.')
          return { name: 'home' }
        }
      },
    },
    {
      path: '/logIn',
      name: 'logIn',
      component: LogInView,
      beforeEnter: (to, from) => {
        const store = useArticleStore()
        if (store.isLogin) {
          window.alert('이미 로그인이 되어있습니다.')
          return { name: 'home' }
        }
      },
    },
  ]
})

export default router
