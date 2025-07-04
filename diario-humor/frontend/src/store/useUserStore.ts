// src/store/useUserStore.ts

import { defineStore } from "pinia"
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // 🔐 Estado inicial: tenta carregar o token do localStorage
  const config = ref({
    token: localStorage.getItem('access_token') || ''
  })

  // ✅ Retorna o token atual (reativo)
  const getToken = computed(() => config.value.token)

  // 🔍 Retorna se o usuário está autenticado (útil no frontend)
  const isAuthenticated = computed(() => !!config.value.token)

  // 📝 Define o token e persiste no localStorage
  function setToken(token: string) {
    config.value.token = token
    localStorage.setItem('access_token', token)
  }

  // 🚪 Limpa o token ao fazer logout
  function logout() {
    config.value.token = ''
    localStorage.removeItem('access_token')
  }

  return {
    getToken,
    isAuthenticated,
    setToken,
    logout
  }
})
