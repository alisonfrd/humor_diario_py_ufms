<template>
    <div class="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div class="bg-gray-800 rounded-lg shadow-xl p-6 max-w-md w-full border border-purple-700/30">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-semibold text-purple-300">Detalhes do Registro</h3>
          <button @click="historyStore.viewingEntrie(null)" class="text-gray-400 hover:text-gray-200">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </button>
        </div>
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <span class="text-4xl">{{ viewingEntry.mood }}</span>
            <span class="text-purple-300">{{ formatEntryDate(viewingEntry.date) }}</span>
          </div>
          <p class="text-gray-200 whitespace-pre-line">{{ viewingEntry.description }}</p>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import { useHistoryStore } from '@/store/useHistoryStore';
import { computed } from 'vue';

const historyStore = useHistoryStore();

const viewingEntry = computed(() => historyStore.getViewingEntrie);

function formatEntryDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('pt-BR', { 
    weekday: 'short', 
    day: 'numeric', 
    month: 'short' 
  });
}
</script>