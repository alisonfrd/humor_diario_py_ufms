// src/store/useToastStore.ts
import { defineStore } from 'pinia'

export interface Toast {
  id: number
  type: 'success' | 'error' | 'info' | 'warning'
  title: string
  description?: string
  duration?: number
}

export const useToastStore = defineStore('toast', {
  state: () => ({
    toasts: [] as Toast[]
  }),
  actions: {
    addToast(toast: Omit<Toast, 'id'>) {
      const id = Date.now() + Math.random()
      const newToast = {
        ...toast,
        id,
        duration: toast.duration || 5000
      }
      this.toasts.push(newToast)
      setTimeout(() => {
        this.removeToast(id)
      }, newToast.duration)
    },
    removeToast(id: number) {
      this.toasts = this.toasts.filter(t => t.id !== id)
    }
  },
  getters: {
    getToasts: (state) => state.toasts
  }
})