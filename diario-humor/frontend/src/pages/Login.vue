<template>
  <div class="absolute top-0 min-w-screen min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-indigo-900 flex items-center justify-center p-4">
    <div class="w-full max-w-md space-y-6">
      <!-- Header com mensagem motivacional -->
      <div class="text-center space-y-4" style="margin-bottom: 8px;">
        <div class="flex justify-center items-center gap-2 mb-4">
          <div class="p-3 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full">
            <Heart class="w-6 h-6 text-white" />
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
            MoodTracker
          </h1>
        </div>

        <div
          class="bg-purple-800/30 backdrop-blur-sm rounded-2xl p-4 border border-purple-500/30 cursor-pointer transition-all hover:bg-purple-800/40"
          @click="changeMessage"
          style="margin-top: 8px;"
        >
          <div class="flex items-center justify-center gap-2 text-purple-200">
            <Sparkles class="w-4 h-4" />
            <p class="text-sm font-medium">{{ currentMessage }}</p>
            <Sparkles class="w-4 h-4" />
          </div>
          <p class="text-xs text-purple-300 mt-1">Clique para uma nova mensagem</p>
        </div>
      </div>

      <!-- Cards -->
      <div class="border border-purple-500/20 shadow-2xl bg-gray-800/80 backdrop-blur-sm rounded-xl overflow-hidden">

        <div class="text-center pb-4 pt-6 px-6">
          <h2 class="text-xl text-white font-semibold">{{ step === 1 ? 'Bem-vindo de volta!' : 'Realize seu cadastro!' }}</h2>
          <p class="text-gray-300" v-if="step === 1">Entre para continuar sua jornada de autoconhecimento</p>
        </div>

        <div class="px-6 pb-6">
          <div class="space-y-4">
             <div v-if="step === 2" class="space-y-2">
              <label for="name" class="text-gray-200 font-medium">Nome</label>
              <input
                id="name"
                v-model="name"
                type="name"
                placeholder="Digite seu nome"
                class="w-full bg-gray-700/50 border border-purple-400/30 focus:border-purple-400 focus:ring-purple-400 text-white placeholder:text-gray-400 rounded px-3 py-2"
                :required="step === 2"
              />
            </div>

            <div class="space-y-2 mb-2">
              <label for="email" class="text-gray-200 font-medium">Email</label>
              <input
                id="email"
                v-model="email"
                type="text"
                placeholder="Digite seu email"
                class="w-full bg-gray-700/50 border border-purple-400/30 focus:border-purple-400 focus:ring-purple-400 text-white placeholder:text-gray-400 rounded px-3 py-2"
                required
              />
            </div>

            <div class="space-y-2 mb-2">
              <label for="password" class="text-gray-200 font-medium">Senha</label>
              <input
                id="password"
                v-model="password"
                type="password"
                placeholder="Digite sua senha"
                class="w-full bg-gray-700/50 border border-purple-400/30 focus:border-purple-400 focus:ring-purple-400 text-white placeholder:text-gray-400 rounded px-3 py-2"
                required
              />
            </div>

            <button
              class="w-full bg-gradient-to-r from-purple-500 to-purple-700/30 hover:from-purple-600 hover:to-pink-600 text-white font-medium py-2.5 transition-all duration-200 rounded cursor-pointer"
              style="margin-top: 12px;"
              :disabled="isLoading"
              @click="handleSubmit"
            >
              <div v-if="isLoading" class="flex items-center gap-2 justify-center">
                <div class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                Entrando...
              </div>
              <div v-else class="flex items-center gap-2 justify-center">
                <!-- <Sun class="w-4 h-4" /> -->
                Entrar
              </div>
            </button>
          </div>

          <div class="mt-6 text-center space-y-3" style="margin: 16px 0 16px 0">
            <!-- <button class="text-sm text-purple-300 hover:text-purple-200 transition-colors">
              Esqueceu sua senha?
            </button> -->
            <div v-if="step === 1" class="text-sm text-gray-300">
              Não tem uma conta?
              <button @click="step = 2" class="cursor-pointer text-purple-300 hover:text-purple-200 font-medium transition-colors">
                Cadastre-se aqui
              </button>
            </div>
            <button v-else @click="step = 1" class="cursor-pointer text-purple-300 hover:text-purple-200 font-medium transition-colors">
              Voltar para login
            </button>
          </div>
        </div>
      </div>

      <!-- Footer inspiracional -->
      <div class="text-center">
        <p class="text-sm text-gray-400">
          <!-- "O primeiro passo para mudar o mundo é mudar a si mesmo" ✨ -->
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { Heart, Sparkles, Sun } from "lucide-vue-next"
import { useRouter } from 'vue-router'
import api from '@/services/axios'
import { useUserStore } from "@/store/useUserStore"

const router = useRouter()
const userStore = useUserStore()
  
const email = ref("")
const password = ref("")
const name = ref("")
const isLoading = ref(false)
const step = ref(1);

const motivationalMessages = [
  "Suas emoções são suas amigas 💜",
  "Cada sentimento tem sua importância ✨",
  "Você é mais forte do que imagina 🌟",
  "Hoje é um novo dia para se conhecer melhor 🌅",
  "Seus sentimentos são válidos e importantes 💙",
]

const currentMessage = ref(motivationalMessages[0])

const changeMessage = () => {
  const randomIndex = Math.floor(Math.random() * motivationalMessages.length)
  currentMessage.value = motivationalMessages[randomIndex]
}

const handleSubmit = async () => {
  isLoading.value = true
  const endpoint = step.value === 1 ? '/auth/login' : '/auth/register'

  try {
    const response = await api.post(endpoint, {
      name: name.value,
      email: email.value,
      password: password.value
    })

    if (step.value === 2) {
      const loginResponse = await api.post('/auth/login', {
        email: email.value,
        password: password.value
      })
      if (loginResponse.data?.access_token) {
        userStore.setToken(loginResponse.data.access_token)
        router.push('/Home')
        isLoading.value = false
        return
      }
    } else if (response.data?.access_token) {
      userStore.setToken(response.data.access_token)
      router.push('/Home')
      isLoading.value = false
      return
    }
    isLoading.value = false
  } catch (err) {
    console.error(err)
    isLoading.value = false
  }
}
</script>