<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
</script>

<template>
  <div>
    <!-- Render the navbar component -->
      <router-view name="navbar"></router-view>
      
      <!-- Render the sidebar component -->
      <router-view name="sidebar"></router-view>
    
    <!-- <RouterView /> -->
    <router-view></router-view>
  </div>
</template>
