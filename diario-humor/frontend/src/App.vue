<template>
  <div class="flex justify-center items-center">
    <component :is="currentView" />
  </div>
</template>

<script setup>
import {ref, computed} from "vue"
import LoginPage from "./pages/Login.vue"
import Home from "./pages/Home.vue"

const routes = {
  '/': Home,
  '/login': LoginPage
}

const currentView = computed(() => {
  const currentPath = window.location.pathname;
  
  return routes[currentPath]
})
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
