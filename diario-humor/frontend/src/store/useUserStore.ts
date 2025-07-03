import { defineStore } from "pinia"
import {ref, computed} from 'vue'

export const useUserStore = defineStore('user', () => {
    const config = ref({
        token: '',
    })

    const getToken = computed(() => config.value.token);

    function setToken(token: string) {
        config.value.token = token
    }

  return { getToken, setToken}
})