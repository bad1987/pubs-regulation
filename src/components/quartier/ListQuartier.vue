<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { initFlowbite } from 'flowbite'
import VueBasicAlert from 'vue-basic-alert'

const quartiers = ref([])
const loading = ref(true)
const alert = ref(null)
const router = useRouter()

onMounted(() => {
    initFlowbite()

    // load zones from the database
    loading.value = true
    axios.get('quartierAffichages')
        .then(response => {
            console.log(response.data)
            quartiers.value = response.data
        })
        .catch(error => {
            console.log(error)
            if ('response' in error && error.response.status === 401) {
                router.push('/login')
            }
            else if ('response' in error && error.response.status === 403) {
                router.push('/error/403')
            }
            else if ('response' in error && 'data' in error.response && 'detail' in error.response.data) {
                alert.value.showAlert("error", error.response.data.detail, "error!!")
            }
            else {
                alert.value.showAlert("error", error.message, "error!!")
            }
        })
        .finally(() => {
            loading.value = false
        })
})
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <main class="mx-auto my-auto">
        <div v-if="loading"
            class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
            <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
        </div>
        <div v-if="!loading">
            <table v-if="quartiers.length > 0" class="w-around text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">N°</th>
                        <th scope="col" class="px-6 py-3">Nom</th>
                        <th scope="col" class="px-6 py-3">Sous Quartier</th>
                        <th scope="col" class="px-6 py-3">Observations</th>
                        <th scope="col" class="px-6 py-3">Arrondissement</th>
                        <th scope="col" class="px-6 py-3">Zone</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="quartier in quartiers" :key="quartier.IDQuartierAffichage">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 dark:text-white whitespace-nowrap">{{
                            quartier.IDQuartierAffichage }}</th>
                        <td class="px-6 py-4">{{ quartier.NomQuartier }}</td>
                        <td class="px-6 py-4">{{ quartier.SousQuartierAffich }}</td>
                        <td class="px-6 py-4">{{ quartier.ObservationsQuartier }}</td>
                        <td class="px-6 py-4">{{ quartier.ArrondissementQuartier }}</td>
                        <td class="px-6 py-4">{{ quartier.zone_affichage.LibelleZone }}</td>
                    </tr>
                </tbody>
            </table>
            <!-- if no quartiers in the database show a message -->
            <div v-else>
                <p>Aucun quartier dans la base de donnees</p>
            </div>
        </div>
    </main>
</template>