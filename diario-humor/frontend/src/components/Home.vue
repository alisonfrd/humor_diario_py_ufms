<template>
  <div class="min-h-screen min-w-screen bg-gray-900 text-gray-100 flex flex-col">
    <!-- Header -->
    <header class="bg-purple-900 p-4 shadow-lg">
      <div class="container mx-auto flex justify-between items-center">
        <h1 class="text-2xl font-bold text-purple-200">Diário de Humor</h1>
        <span class="text-purple-300 text-sm">{{ formattedDate }}</span>
      </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto flex-grow p-4 md:p-6">
      <!-- New Entry Form -->
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
      
      <!-- History -->
      <div class="bg-gray-800 rounded-lg shadow-lg p-6 border border-purple-700/30">
        <h2 class="text-xl font-semibold text-purple-300 mb-4">Histórico de Humor</h2>
        
        <!-- Calendar View -->
        <div class="grid grid-cols-7 gap-1 mb-6">
          <div v-for="day in 7" :key="`header-${day}`" class="text-center text-xs text-purple-400 font-medium p-1">
            {{ ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'][day-1] }}
          </div>
          <div 
            v-for="day in calendarDays" 
            :key="`day-${day.date}`" 
            class="aspect-square p-1 relative"
          >
            <div 
              class="w-full h-full flex flex-col items-center justify-center rounded-md cursor-pointer hover:bg-gray-700"
              :class="day.entry ? 'bg-gray-700/50' : 'bg-gray-800/50'"
              @click="viewEntry(day.entry)"
            >
              <span class="text-xs text-gray-400">{{ day.dayNumber }}</span>
              <span v-if="day.entry" class="text-xl">{{ day.entry.mood }}</span>
            </div>
          </div>
        </div>
        
        <!-- Recent Entries -->
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
            <p class="text-sm text-gray-300 line-clamp-1 mt-1">{{ entry.description }}</p>
          </div>
        </div>
      </div>
    </main>
    
    <!-- Modal for viewing entry details -->
    <div v-if="viewingEntry" class="fixed inset-0 bg-black/70 flex items-center justify-center p-4 z-50">
      <div class="bg-gray-800 rounded-lg shadow-xl p-6 max-w-md w-full border border-purple-700/30">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-semibold text-purple-300">Detalhes do Registro</h3>
          <button @click="viewingEntry = null" class="text-gray-400 hover:text-gray-200">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
          </button>
        </div>
        <div v-if="viewingEntry" class="space-y-4">
          <div class="flex items-center gap-3">
            <span class="text-4xl">{{ viewingEntry.mood }}</span>
            <span class="text-purple-300">{{ formatEntryDate(viewingEntry.date) }}</span>
          </div>
          <p class="text-gray-200 whitespace-pre-line">{{ viewingEntry.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

// Estado
const selectedMood = ref('');
const description = ref('');
const entries = ref([]);
const viewingEntry = ref(null);

// Lista de humores disponíveis
const moods = [
  { value: 'feliz', emoji: '😄', color: 'bg-yellow-500' },
  { value: 'calmo', emoji: '😌', color: 'bg-green-500' },
  { value: 'neutro', emoji: '😐', color: 'bg-blue-500' },
  { value: 'triste', emoji: '😔', color: 'bg-indigo-500' },
  { value: 'irritado', emoji: '😠', color: 'bg-red-500' },
];

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

// Dias do calendário
const calendarDays = computed(() => {
  const today = new Date();
  const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
  const lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0);
  
  const days = [];
  const startOffset = firstDayOfMonth.getDay(); // 0 = domingo
  
  // Dias do mês anterior para preencher o início
  for (let i = 0; i < startOffset; i++) {
    const prevMonthDay = new Date(today.getFullYear(), today.getMonth(), -i);
    days.unshift({
      date: prevMonthDay.toISOString().split('T')[0],
      dayNumber: prevMonthDay.getDate(),
      isCurrentMonth: false,
      entry: findEntryByDate(prevMonthDay.toISOString().split('T')[0])
    });
  }
  
  // Dias do mês atual
  for (let i = 1; i <= lastDayOfMonth.getDate(); i++) {
    const currentDate = new Date(today.getFullYear(), today.getMonth(), i);
    const dateString = currentDate.toISOString().split('T')[0];
    days.push({
      date: dateString,
      dayNumber: i,
      isCurrentMonth: true,
      isToday: i === today.getDate(),
      entry: findEntryByDate(dateString)
    });
  }
  
  // Preencher até completar 42 dias (6 semanas)
  const remainingDays = 42 - days.length;
  for (let i = 1; i <= remainingDays; i++) {
    const nextMonthDay = new Date(today.getFullYear(), today.getMonth() + 1, i);
    const dateString = nextMonthDay.toISOString().split('T')[0];
    days.push({
      date: dateString,
      dayNumber: i,
      isCurrentMonth: false,
      entry: findEntryByDate(dateString)
    });
  }
  
  return days;
});

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