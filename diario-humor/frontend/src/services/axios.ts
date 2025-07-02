// src/services/axios.js
import axios from 'axios'

// Cria instância com baseURL
const api = axios.create({
  baseURL: 'http://localhost:5000', // backend
  timeout: 10000
})

// Intercepta a requisição e adiciona token (ex: da store ou localStorage)
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Intercepta respostas para lidar com erros globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Exemplo: logout automático se o token estiver inválido
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api