// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import Login from '@/pages/Login.vue'
import { computed } from 'vue'
import { useUserStore } from '@/store/useUserStore'

const routes = [
  {
     path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home', // redireciona raiz para home
    component: Home,
     meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/login'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const storeUser = useUserStore()
  const isAuthenticated = storeUser.getToken
  console.log(`Verificando autenticação: ${isAuthenticated}`)

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router