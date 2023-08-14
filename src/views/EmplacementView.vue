<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreateEmplacement = defineAsyncComponent(() => import('../components/emplacement/CreateEmplacement.vue'));
const ListEmplacement = defineAsyncComponent(() => import('../components/emplacement/ListEmplacement.vue'));
const showCreateEmplacement = ref(false);
const alert = ref(null);
const toggleCreateEmplacement = () => {
    showCreateEmplacement.value = !showCreateEmplacement.value;
}
const onEmplacementCreated = () => {
    showCreateEmplacement.value = false;
    alert.value.showAlert("success", "Zone created successfully", "success!!")
}
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <!-- Add and style the main container -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
        <!-- Add and style the main header for this page with the page title:Zones. And a button to create a new zone at the right -->
        <header class="flex items-center justify-between w-full px-4 py-2 bg-white dark:bg-gray-800 shadow-lg">
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Emplacements</h1>
            <button @click="toggleCreateEmplacement"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Créer un
                emplacement</button>
        </header>
        <main class="m-auto px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create zone component -->
            <CreateEmplacement v-if="showCreateEmplacement" :onEmplacementCreated="onEmplacementCreated"
                :show="showCreateEmplacement" />
            <!-- List of emplacements -->
            <ListEmplacement />
    </main>
</div></template>