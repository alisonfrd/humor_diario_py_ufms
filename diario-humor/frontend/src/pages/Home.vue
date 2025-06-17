<template>
  <div class="min-h-screen min-w-screen bg-gray-900 text-gray-100 flex flex-col">
    <!-- Header -->
    <Header />

    <!-- Main -->
    <main class="container mx-auto flex-grow p-4 md:p-6">
      <!-- Registro -->
      <RegisterMood />
      
      <!-- Histórico -->
      <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-purple-700/30">
        <h2 class="text-xl font-semibold text-purple-300 mb-4">Histórico de Humor</h2>
        
        <!-- Calendário -->
        <Calendar />
        
        <!-- Entradas recentes -->
        <History :entries="entries" />
      </div>
    </main>
    
    <!-- Modal detalhes da entrada  -->
    <Modal v-if="viewingEntry" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import Calendar from "../components/Calendar.vue";
import History from "../components/History.vue";
import ModalEntries from "../components/ModalEntries.vue";
import RegisterMood from "../components/RegisterMood.vue";
import Header from "../components/Header.vue";

// Estado
const entries = ref([]);
const viewingEntry = ref(null);

function deleteEntry(id) {
  entries.value = entries.value.filter(entry => entry.id !== id);
  localStorage.setItem('moodEntries', JSON.stringify(entries.value));
  
  if (viewingEntry.value && viewingEntry.value.id === id) {
    viewingEntry.value = null;
  }
}

function viewEntry(entry) {
  if (entry) {
    viewingEntry.value = entry;
  }
}

function findEntryByDate(date) {
  return entries.value.find(entry => entry.date === date);
}

function formatEntryDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('pt-BR', { 
    weekday: 'short', 
    day: 'numeric', 
    month: 'short' 
  });
}

// Carregar dados do localStorage ao iniciar
onMounted(() => {
  const savedEntries = localStorage.getItem('moodEntries');
  if (savedEntries) {
    entries.value = JSON.parse(savedEntries);
  }
});
</script>