<script setup></script>

<template>
    <div class="sidebar">
      <!-- Use router-link to create links to different routes -->
      <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
      <router-link :to="{ name: 'Profile' }">Profile</router-link>
      <router-link :to="{ name: 'Settings' }">Settings</router-link>
    </div>
  </template>