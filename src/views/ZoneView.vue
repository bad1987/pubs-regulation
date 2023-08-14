<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreateZone = defineAsyncComponent(() => import('../components/zone/CreateZone.vue'));
const ListZone = defineAsyncComponent(() => import('../components/zone/ListZone.vue'));
const showCreateZone = ref(false);
const alert = ref(null);
const toggleCreateZone = () => {
    showCreateZone.value = !showCreateZone.value;
}
const onZoneCreated = () => {
    showCreateZone.value = false;
    alert.value.showAlert("success", "Zone created successfully", "success!!")
}
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <!-- Add and style the main container -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
        <!-- Add and style the main header for this page with the page title:Zones. And a button to create a new zone at the right -->
        <header class="flex items-center justify-between w-full px-4 py-2 bg-white dark:bg-gray-800 shadow-lg">
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Zones</h1>
            <button @click="toggleCreateZone"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Create a new
                zone</button>
        </header>
        <main  class="m-auto px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create zone component -->
            <CreateZone v-if="showCreateZone" :onZoneCreated="onZoneCreated" :show="showCreateZone" />
            <!-- List of Zones -->
            <ListZone />
        </main>
    </div>
</template>