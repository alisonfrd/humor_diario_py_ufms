// src/store/useHistoryStore.ts

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useHistoryStore = defineStore('history', () => {
  const entries = ref([])
  const viewingEntry = ref(null)

  const getEntries = computed(() => entries.value)
  const getViewingEntrie = computed(() => viewingEntry.value)

  function setEntries(newEntries) {
    entries.value = newEntries
  }

  function addEntry(entry) {
    entries.value.unshift(entry)
  }

  function removeEntrie(id) {
    entries.value = entries.value.filter(e => e.id !== id)
  }

  function viewingEntrie(entry) {
    viewingEntry.value = entry
  }

  return {
    getEntries,
    getViewingEntrie,
    setEntries,
    addEntry,
    removeEntrie,
    viewingEntrie
  }
})
