<template>
    <div class="bg-gray-800 rounded-lg shadow-lg p-6 mb-8 border border-purple-700/30">
        <h2 class="text-xl font-semibold text-purple-300 mb-4">Como você está se sentindo hoje?</h2>
        
        <!-- Mood Selection -->
        <div class="grid grid-cols-5 gap-4 mb-6">
          <button 
            v-for="mood in moods" 
            :key="mood.value" 
            @click="selectMood(mood)"
            class="mood-btn p-3 rounded-full text-3xl transition-transform hover:scale-110"
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
          class="w-full bg-purple-600 hover:bg-purple-700 text-white font-medium py-2 px-4 rounded-md transition-colors"
          :disabled="!selectedMood"
        >
          Salvar Registro
        </button>
      </div>
</template>

<script setup>
import { ref } from 'vue'
// Lista de humores disponíveis
const moods = [
  { value: 'feliz', emoji: '😄', color: 'bg-yellow-500' },
  { value: 'calmo', emoji: '😌', color: 'bg-green-500' },
  { value: 'neutro', emoji: '😐', color: 'bg-blue-500' },
  { value: 'triste', emoji: '😔', color: 'bg-indigo-500' },
  { value: 'irritado', emoji: '😠', color: 'bg-red-500' },
];

const selectedMood = ref('');
const description = ref('');

// Funções
function selectMood(mood) {
  selectedMood.value = mood.value;
}

function saveEntry() {
  if (!selectedMood.value) return;
  
  const mood = moods.find(m => m.value === selectedMood.value);
  
  const newEntry = {
    id: Date.now().toString(),
    date: new Date().toISOString().split('T')[0],
    mood: mood.emoji,
    moodValue: selectedMood.value,
    description: description.value,
    timestamp: new Date().toISOString()
  };
  
  // Verificar se já existe uma entrada para hoje
  const todayEntry = entries.value.findIndex(e => e.date === newEntry.date);
  if (todayEntry !== -1) {
    entries.value[todayEntry] = newEntry;
  } else {
    entries.value.unshift(newEntry);
  }
  
  // Salvar no localStorage
  localStorage.setItem('moodEntries', JSON.stringify(entries.value));
  
  // Limpar formulário
  selectedMood.value = '';
  description.value = '';
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