<template>
    <div class="w-full bg-purple-900 p-4 shadow-lg">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold text-purple-200">Diário de Humor</h1>
            <span class="text-purple-300 text-sm">{{ formattedDate }}</span>
          </div>
    </div>
</template>

<script setup>
import { computed } from "vue"
// Data formatada
const formattedDate = computed(() => {
  const now = new Date();
  return now.toLocaleDateString('pt-BR', { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });
});
</script>