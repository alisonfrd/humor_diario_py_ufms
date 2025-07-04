<template>
  <Toast />
  <div class="flex justify-center items-center">

    <router-view />
  </div>
</template>

<script setup>
import Toast from './components/Toast.vue'
import { onMounted } from 'vue'
import { useToastStore } from '@/store/useToastStore'

onMounted(() => {
  // Teste: dispara um toast ao abrir o app
  const toastStore = useToastStore()
  toastStore.addToast({
    type: 'success',
    title: 'Seja bem-vindo!',
    description: 'Aproveite o Diário do Humor para registrar suas emoções diárias.',
    duration: 3000
  })
})
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
