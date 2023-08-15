<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreateProduit = defineAsyncComponent(() => import('../components/produit/CreateProduit.vue'));
const showCreateProduit = ref(false);
const alert = ref(null);
const toggleCreateProduit = () => {
    showCreateProduit.value = !showCreateProduit.value;
}
const onProduitCreated = () => {
    showCreateProduit.value = false;
    alert.value.showAlert("success", "Produit created successfully", "success!!")
}
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <!-- Add and style the main container -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
        <!-- Add and style the main header for this page with the page title:Zones. And a button to create a new zone at the right -->
        <header class="flex items-center justify-between w-full px-4 py-2 bg-white dark:bg-gray-800 shadow-lg">
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Produits Concession</h1>
            <button @click="toggleCreateProduit"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Créer Produit</button>
        </header>
        <main class="px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create Produit component -->
            <div class="flex items-center justify-center  overflow-x-auto shadow-md sm:rounded-lg">
                <table class="w-around text-sm text-left text-gray-500 dark:text-gray-400">
                    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        <tr>
                            <th scope="col" class="px-10 py-3">Code</th>
                            <th scope="col" class="px-6 py-3">Dispositif publicitaire</th>
                            <th scope="col" class="px-6 py-3">Unite facturation</th>
                            <th scope="col" class="px-6 py-3">Tarification</th>
                            <th scope="col" class="px-6 py-3">Observations</th>
                            <th scope="col" class="px-6 py-3">Durée</th>
                             <!--<th scope="col" class="px-6 py-3">Specificité</th>
                           <th scope="col" class="px-6 py-3">Taux spécifique</th>
                            <th scope="col" class="px-6 py-3">Surface minimum</th>
                            <th scope="col" class="px-6 py-3">Durée minimum</th> -->
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">A.1</th>
                                <td class="px-6 py-4">Panneaux Classiques</td>
                                <td class="px-6 py-4">m²</td>
                                <td class="px-6 py-4">10 000</td>
                                <td class="px-6 py-4">RAS</td>
                                <td class="px-6 py-4">Mois</td>
                        </tr>
                        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">A.2</th>
                                <td class="px-6 py-4">Panneaux Lumineux</td>
                                <td class="px-6 py-4">m²</td>
                                <td class="px-6 py-4">10 000</td>
                                <td class="px-6 py-4">RAS</td>
                                <td class="px-6 py-4">Mois</td>
                        </tr>
                        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">A.3</th>
                                <td class="px-6 py-4">Panneaux Design/Relooké</td>
                                <td class="px-6 py-4">m²</td>
                                <td class="px-6 py-4">10 000</td>
                                <td class="px-6 py-4">RAS</td>
                                <td class="px-6 py-4">Mois</td>
                        </tr>
                        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">A.4</th>
                                <td class="px-6 py-4">Panneaux de proximité</td>
                                <td class="px-6 py-4">m²</td>
                                <td class="px-6 py-4">10 000</td>
                                <td class="px-6 py-4">RAS</td>
                                <td class="px-6 py-4">Mois</td>
                        </tr>
                        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">A.5</th>
                                <td class="px-6 py-4">Panneaux de proximite lumineux</td>
                                <td class="px-6 py-4">m²</td>
                                <td class="px-6 py-4">10 000</td>
                                <td class="px-6 py-4">RAS</td>
                                <td class="px-6 py-4">Mois</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <CreateProduit v-if="showCreateProduit" :onProduitCreated="onProduitCreated" :show="showCreateProduit"/>
        </main>
    </div>

</template>