<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreateEmplacement = defineAsyncComponent(() => import('../components/emplacement/CreateEmplacement.vue'));
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
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Zones</h1>
            <button @click="toggleCreateEmplacement"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Créer un emplacement</button>
        </header>
        <main class="px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create zone component -->
            <div class="flex items-center justify-center  overflow-x-auto shadow-md sm:rounded-lg">
            <table class="w-around text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">N°</th>
                <th scope="col" class="px-6 py-3">Code</th>
                <th scope="col" class="px-6 py-3">Quartier</th>
            </tr>
        </thead>
        <tbody>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">1</th>
                <td class="px-6 py-4">ZP</td>
                <td class="px-6 py-4">Zone Prestige</td>
            </tr>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">2</th>
                <td class="px-6 py-4">ZS</td>
                <td class="px-6 py-4">Zone Standard</td>
            </tr>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">3</th>
                <td class="px-6 py-4">ZO</td>
                <td class="px-6 py-4">Zone Ordinaire</td>
            </tr>
        </tbody>
    </table>
</div>
            <CreateEmplacement v-if="showCreateEmplacement" :onEmplacementCreated="onEmplacementCreated" :show="showCreateEmplacement" />
        </main>
    </div>

</template>