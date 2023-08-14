<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreateQuartier = defineAsyncComponent(() => import('../components/quartier/CreateQuartier.vue'));
const ListQuartier = defineAsyncComponent(() => import('../components/quartier/ListQuartier.vue'));
const showCreateQuartier = ref(false);
const alert = ref(null);
const toggleCreateQuartier = () => {
    showCreateQuartier.value = !showCreateQuartier.value;
}
const onQuartierCreated = () => {
    showCreateQuartier.value = false;
    alert.value.showAlert("success", "Quartier created successfully", "success!!")
}
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <!-- Add and style the main container -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
        <!-- Add and style the main header for this page with the page title:Quartier. And a button to create a new quartier at the right -->
        <header class="flex items-center justify-between w-full px-4 py-2 bg-white dark:bg-gray-800 shadow-lg">
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Quartier</h1>
            <button @click="toggleCreateQuartier"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Create a new
                quartier</button>
        </header>
        <main class="m-auto px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create quartier component -->
            <div class="flex items-center justify-center  overflow-x-auto shadow-md sm:rounded-lg">
                <!-- List of Quartiers -->
                <ListQuartier />
            </div>
            <CreateQuartier v-if="showCreateQuartier" :onQuartierCreated="onQuartierCreated" :show="showCreateQuartier" />
        </main>
    </div>
</template>