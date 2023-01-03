<script setup>
import NavBar from './components/NavBar.vue'
</script>

<template>
  <div class="px-8 w-screen h-screen flex flex-col">
    <NavBar />
    <div class="flex-1 mt-10">
      <router-view />
    </div>
  </div>
</template>
