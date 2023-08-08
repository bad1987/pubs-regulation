<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- Render the navbar component -->
  <router-view name="navbar"></router-view>
  
  <!-- Render the sidebar component -->
  <router-view name="sidebar"></router-view>
  <div class="rounded-lg dark:border-gray-700 mt-14">
    <!-- Render the default component -->
    <router-view class="min-h-screen"></router-view>
  </div>
</template>
