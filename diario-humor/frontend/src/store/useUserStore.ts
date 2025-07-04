import { defineStore } from "pinia"
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // Carrega o token salvo (se existir)
  const config = ref({
    token: localStorage.getItem('access_token') || ''
  })

  const getToken = computed(() => config.value.token)

  function setToken(token: string) {
    config.value.token = token
    localStorage.setItem('access_token', token)
  }

  function logout() {
    config.value.token = ''
    localStorage.removeItem('access_token')
  }

  return { getToken, setToken, logout }
})
