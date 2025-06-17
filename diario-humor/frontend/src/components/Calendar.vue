<template>
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
</template>

<script setup>
import { computed, ref } from 'vue'
// Dias do calendário
const entries = ref([]);

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

function findEntryByDate(date) {
  return entries.value.find(entry => entry.date === date);
}
</script>