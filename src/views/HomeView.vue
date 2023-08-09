<script setup>
import { useTokenStore } from '../stores/token';

const tokenStore = useTokenStore()
</script>

<template>
  <main>
    welcome to Ads Regulator
    <div v-if="tokenStore.user_data">{{ tokenStore.user_data.email }}</div>
  </main>
</template>
