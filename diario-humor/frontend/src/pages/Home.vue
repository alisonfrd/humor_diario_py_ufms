<template>
  <div class="flex justify-center items-center min-h-screen min-w-screen bg-gray-900 text-gray-100 flex flex-col">
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
        <Calendar :entries="entries" @view-entry="viewEntry" />

        <!-- Entradas recentes -->
        <History :entries="entries" @view-entry="viewEntry" />
      </div>
    </main>

    <!-- Modal detalhes da entrada  -->
    <ModalEntries v-if="viewingEntry" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import Calendar from "../components/Calendar.vue";
import History from "../components/History.vue";
import ModalEntries from "../components/ModalEntries.vue";
import RegisterMood from "../components/RegisterMood.vue";
import Header from "../components/Header.vue";
import { useHistoryStore } from '@/store/useHistoryStore';
import api from '@/services/axios';

// Estado
const historyStore = useHistoryStore();

const viewingEntry = computed(() => historyStore.getViewingEntrie);
const entries = computed(() => historyStore.getEntries);

function viewEntry(entry) {
  if (entry) {
    historyStore.viewingEntrie(entry);
  }
}

// Carregar dados do backend ao iniciar
onMounted(async () => {
  await getEntries();
});

// Carrega entradas do backend e atualiza o estado global
async function getEntries() {
  try {
    const res = await api.get('/diary/');
    if (res.data) {
      // 🚀 Corrige o mapeamento da propriedade
      const normalized = res.data.map(entry => ({
        ...entry,
        date: entry.entry_date,         // necessário para <Calendar> e <History>
        description: entry.text         // necessário para <History>
      }));
      historyStore.setEntries(normalized);
    }
  } catch (error) {
    console.error("Erro ao carregar entradas:", error);
  }
}
</script>
