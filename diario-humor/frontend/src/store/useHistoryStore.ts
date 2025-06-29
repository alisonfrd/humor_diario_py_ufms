import { defineStore } from "pinia"
import {ref, computed} from 'vue'

export const useHistoryStore = defineStore('history', () => {
    const config = ref({
        entries: [],
        viewingEntrie: null
    })

    const getEntries = computed(() => config.value.entries);
    const getViewingEntrie = computed(() => config.value.viewingEntrie);

    function setEntrie(entrie: any) {
        config.value.entries = entrie
        localStorage.setItem('moodEntries', JSON.stringify(entrie));
    }

    function viewingEntrie(entrie: any){
        config.value.viewingEntrie = entrie;
    }

    function removeEntrie(id: number){
        const indexEntrie = config.value.entries.findIndex((item) => item.id === id);
        config.value.entries.splice(indexEntrie, 1)
        localStorage.setItem('moodEntries', JSON.stringify(config.value.entries));
    }

  return { getEntries, getViewingEntrie, setEntrie, viewingEntrie, removeEntrie}
})