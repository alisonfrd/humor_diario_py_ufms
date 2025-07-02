import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import axios from './services/axios'
const pinia = createPinia()

const app = createApp(App)
app.use(router)
app.use(pinia)
app.use(axios)
app.mount('#app')