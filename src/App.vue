<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <!-- Render the navbar component -->
    <router-view name="navbar"></router-view>
    
    <!-- Render the sidebar component -->
    <router-view name="sidebar"></router-view>

    <!-- Render the default component -->
    <router-view></router-view>
  </div>
</template>
