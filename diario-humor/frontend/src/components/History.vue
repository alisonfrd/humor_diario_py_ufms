<template>
    <h3 class="text-md font-medium text-purple-300 mb-2">Registros Recentes</h3>
        <div v-if="entries.length === 0" class="text-gray-500 text-center py-4">
          Nenhum registro encontrado
        </div>
        <div v-else class="space-y-3">
          <div 
            v-for="entry in entries.slice(0, 5)" 
            :key="entry.id" 
            class="bg-gray-700/50 p-3 rounded-md hover:bg-gray-700 cursor-pointer"
             @click="viewEntry(entry)"
          >
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="text-xl">{{ entry.mood }}</span>
                <span class="text-sm text-purple-300">{{ formatEntryDate(entry.date) }}</span>
              </div>
              <button @click.stop="deleteEntry(entry.id)" class="text-gray-400 hover:text-red-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-trash-2"><path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/><line x1="14" x2="14" y1="11" y2="17"/></svg>
              </button>
            </div>
            <p class="text-sm text-gray-300 line-clamp-1 mt-1">{{ entry.text }}</p>

          </div>
        </div>
</template>

<script setup lang="ts">
import { useHistoryStore } from '@/store/useHistoryStore';
import { ref, computed } from 'vue'

const emit = defineEmits(['viewEntry']);

const historyStore = useHistoryStore();
const entries = computed(() => historyStore.getEntries);

function formatEntryDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('pt-BR', { 
    weekday: 'short', 
    day: 'numeric', 
    month: 'short' 
  });
}

function deleteEntry(id: number) {
  historyStore.removeEntrie(id);
  // const  = entries.value.filter(entry => entry.id !== id);
 
  
  // if (viewingEntry.value && viewingEntry.value.id === id) {
  //   viewingEntry.value = null;
  // }
}

function viewEntry(entrie){
  emit('viewEntry', entrie)
}

// interface Config {
//     entries: []
// }

// const props = defineProps<Config>();

</script>