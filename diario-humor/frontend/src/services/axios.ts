// src/services/axios.js
import { useToastStore } from '@/store/useToastStore'
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5001',
  timeout: 10000
})

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token') // <- mais seguro aqui
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if(error.response && error.response.data && error.response.data.error) {
      const toastStore = useToastStore();
      
      toastStore.addToast({
        type: 'error',
        title: 'Erro',
        description: error.response.data.error,
        duration: 3000
      })
    }

    if (error.response && error.response.status === 401) {
      localStorage.removeItem('access_token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api
