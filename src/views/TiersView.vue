<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreateTiers = defineAsyncComponent(() => import('../components/tiers/CreateTiers.vue'));
const ListTiers = defineAsyncComponent(() => import('../components/tiers/ListTiers.vue'));
const showCreateTiers = ref(false);
const alert = ref(null);
const toggleCreateTiers = () => {
    showCreateTiers.value = !showCreateTiers.value;
}
const onTiersCreated = () => {
    showCreateTiers.value = false;
    alert.value.showAlert("success", "Tiers created successfully", "Success!!");
}
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <!-- Add and style the main container -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
        <!-- Add and style the main header for this page with the page title: Tiers. And a button to create a new tier at the right -->
        <header class="flex items-center justify-between w-full px-4 py-2 bg-white dark:bg-gray-800 shadow-lg">
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Tiers</h1>
            <button @click="toggleCreateTiers"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Create a new
                tier</button>
        </header>
        <main class="m-auto px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create tier component -->
            <div class="flex items-center justify-center  overflow-x-auto shadow-md sm:rounded-lg">
                <!-- List of Tiers -->
                <ListTiers />
            </div>
            <CreateTiers v-if="showCreateTiers" :onTiersCreated="onTiersCreated" :show="showCreateTiers" />
        </main>
    </div>
</template>