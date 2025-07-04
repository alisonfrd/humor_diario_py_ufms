<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-50 via-blue-50 to-indigo-100 p- z-1">
    <div class="fixed top-4 right-4 z-50 flex flex-col gap-3 max-w-sm w-full">
      <TransitionGroup name="toast" tag="div" class="space-y-3">
        <div
          v-for="toast in toasts"
          :key="toast.id"
          :class="getToastClasses(toast.type)"
          class="toast-item relative flex items-start gap-3 p-4 rounded-xl border-2 shadow-lg transform transition-all duration-300 ease-in-out"
        >
          <!-- Icon -->
          <component 
            :is="getToastIcon(toast.type)"
            :class="getIconClasses(toast.type)"
            class="w-5 h-5 mt-0.5 flex-shrink-0"
          />

          <!-- Content -->
          <div class="flex-1 min-w-0">
            <h4 :class="getTitleClasses(toast.type)" class="font-semibold text-sm">
              {{ toast.title }}
            </h4>
            <p 
              v-if="toast.description" 
              :class="getDescriptionClasses(toast.type)"
              class="text-sm mt-1"
            >
              {{ toast.description }}
            </p>
          </div>

          <!-- Close Button -->
          <button
            @click="removeToast(toast.id)"
            class="flex-shrink-0 p-1 rounded-lg hover:bg-black/5 transition-colors duration-200"
            aria-label="Fechar notificação"
          >
            <XIcon class="w-4 h-4 text-gray-500" />
          </button>
        </div>
      </TransitionGroup>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { CheckCircle, AlertCircle, X as XIcon } from 'lucide-vue-next'
import { useToastStore } from '@/store/useToastStore'

const toastStore = useToastStore();
const toasts = computed(() => toastStore.getToasts);

const removeToast = (id: number) => {
  toastStore.removeToast(id);
};

// Toast helper functions
const getToastClasses = (type) => {
  switch (type) {
    case 'success':
      return 'bg-emerald-50 border-emerald-200'
    case 'error':
      return 'bg-red-50 border-red-200'
    default:
      return 'bg-white border-gray-200'
  }
}

const getToastIcon = (type) => {
  return type === 'success' ? CheckCircle : AlertCircle
}

const getIconClasses = (type) => {
  switch (type) {
    case 'success':
      return 'text-emerald-600'
    case 'error':
      return 'text-red-600'
    default:
      return 'text-gray-600'
  }
}

const getTitleClasses = (type) => {
  switch (type) {
    case 'success':
      return 'text-emerald-900'
    case 'error':
      return 'text-red-900'
    default:
      return 'text-gray-900'
  }
}

const getDescriptionClasses = (type) => {
  switch (type) {
    case 'success':
      return 'text-emerald-700'
    case 'error':
      return 'text-red-700'
    default:
      return 'text-gray-700'
  }
}

</script>

<style scoped>
/* Toast animations */
.toast-enter-active {
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.toast-leave-active {
  transition: all 0.3s ease-in;
}

.toast-enter-from {
  opacity: 0;
  transform: translateX(100%) scale(0.8);
}

.toast-leave-to {
  opacity: 0;
  transform: translateX(100%) scale(0.9);
}

.toast-move {
  transition: transform 0.3s ease;
}

/* Toast item hover effects */
.toast-item {
  backdrop-filter: blur(8px);
}

.toast-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

/* Custom scrollbar for toast container */
.toast-container::-webkit-scrollbar {
  width: 4px;
}

.toast-container::-webkit-scrollbar-track {
  background: transparent;
}

.toast-container::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 2px;
}

/* Button hover effects */
button {
  position: relative;
  overflow: hidden;
}

button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

button:hover::before {
  left: 100%;
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .toast-item {
    margin: 0 1rem;
    max-width: calc(100vw - 2rem);
  }
}

/* Enhanced animations for better UX */
@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideOutRight {
  from {
    opacity: 1;
    transform: translateX(0);
  }
  to {
    opacity: 0;
    transform: translateX(100%);
  }
}

.toast-item {
  animation: slideInRight 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/* Pulse effect for icons */
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.8;
  }
}

.toast-item svg {
  animation: pulse 2s infinite;
}

/* Gradient border effect */
.toast-item::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  pointer-events: none;
}

/* Success specific styles */
.bg-emerald-50 {
  background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
}

/* Error specific styles */
.bg-red-50 {
  background: linear-gradient(135deg, #fef2f2 0%, #fef7f7 100%);
}

/* Enhanced shadow effects */
.shadow-lg {
  box-shadow: 
    0 10px 15px -3px rgba(0, 0, 0, 0.1),
    0 4px 6px -2px rgba(0, 0, 0, 0.05),
    0 0 0 1px rgba(255, 255, 255, 0.1) inset;
}
</style>