<template>
  <div class="bg-gray-800 rounded-lg shadow-lg p-6 mb-8 border border-purple-700/30">
    <h2 class="text-xl font-semibold text-purple-300 mb-4">Como você está se sentindo hoje?</h2>

    <!-- Mood Selection -->
    <div class="grid grid-cols-5 gap-4 mb-6">
      <button 
        v-for="mood in moods" 
        :key="mood.value" 
        @click="selectMood(mood)"
        class="mood-btn flex justify-center p-3 rounded-full text-3xl transition-transform hover:scale-110 cursor-pointer"
        :class="{ 'ring-2 ring-purple-400 ring-offset-2 ring-offset-gray-800 scale-110': selectedMood === mood.value }"
      >
        {{ mood.emoji }}
      </button>
    </div>

    <!-- Description Input -->
    <div class="mb-6">
      <label for="description" class="block text-sm font-medium text-purple-300 mb-2">Descreva seu dia</label>
      <textarea 
        id="description" 
        v-model="description" 
        rows="3" 
        class="w-full bg-gray-700 border border-gray-600 rounded-md p-3 text-gray-100 focus:ring-purple-500 focus:border-purple-500"
        placeholder="Como foi seu dia hoje?"
      ></textarea>
    </div>

    <!-- Submit Button -->
    <button 
      @click="saveEntry" 
      class="w-full bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-4 rounded-md cursor-pointer transition-colors"
      :disabled="!selectedMood"
    >
      Salvar Registro
    </button>
  </div>
</template>

<script setup>
import { useHistoryStore } from '@/store/useHistoryStore';
import { computed, ref } from 'vue';
import api from '@/services/axios';

const historyStore = useHistoryStore();

const moods = [
  { value: 'feliz', emoji: '😄' },
  { value: 'calmo', emoji: '😌' },
  { value: 'neutro', emoji: '😐' },
  { value: 'triste', emoji: '😔' },
  { value: 'irritado', emoji: '😠' },
];

const selectedMood = ref('');
const description = ref('');
const entries = computed(() => historyStore.getEntries);

function selectMood(mood) {
  selectedMood.value = mood.value;
}

async function saveEntry() {
  if (!selectedMood.value) return;

  const today = new Date().toISOString().split('T')[0];
  const mood = moods.find(m => m.value === selectedMood.value);

  const newEntry = {
    entry_date: today,
    mood: mood.emoji,
    text: description.value
  };

  try {
    const response = await api.post('/diary/', newEntry);
    console.log('Registro salvo com sucesso:', response.data);

    // Atualiza store (evita duplicidade para o mesmo dia)
    const filtered = entries.value.filter(e => e.date !== today);
    const updated = [
      {
        ...newEntry,
        date: today,
        description: newEntry.text,
        created_at: new Date().toISOString(),
        id: Date.now() // opcionalmente usar ID da API
      },
      ...filtered
    ];

    historyStore.setEntries(updated);

    // Limpa campos
    selectedMood.value = '';
    description.value = '';
  } catch (error) {
    console.error('Erro ao salvar registro:', error?.response?.data || error.message);
  }
}
</script>

<style scoped>
.mood-btn {
  transition: all 0.2s ease;
}

.mood-btn:nth-child(1) { background-color: rgba(234, 179, 8, 0.2); }
.mood-btn:nth-child(2) { background-color: rgba(34, 197, 94, 0.2); }
.mood-btn:nth-child(3) { background-color: rgba(59, 130, 246, 0.2); }
.mood-btn:nth-child(4) { background-color: rgba(99, 102, 241, 0.2); }
.mood-btn:nth-child(5) { background-color: rgba(239, 68, 68, 0.2); }

.mood-btn:nth-child(1):hover { background-color: rgba(234, 179, 8, 0.3); }
.mood-btn:nth-child(2):hover { background-color: rgba(34, 197, 94, 0.3); }
.mood-btn:nth-child(3):hover { background-color: rgba(59, 130, 246, 0.3); }
.mood-btn:nth-child(4):hover { background-color: rgba(99, 102, 241, 0.3); }
.mood-btn:nth-child(5):hover { background-color: rgba(239, 68, 68, 0.3); }
</style>
