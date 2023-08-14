<script setup>
import { ref, onMounted, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { initFlowbite } from 'flowbite'
import { Modal } from 'flowbite-vue'
import VueBasicAlert from 'vue-basic-alert'
import axios from 'axios'
import { quartierApi } from '../../api/api'
import { useQuartierStore } from "../../stores/quartierStore";

const quartierStore = useQuartierStore()
const zones = ref(quartierStore.zones)
const loadingZones = ref(true)
const router = useRouter()
const alert = ref(null)

const props = defineProps({
    onQuartierCreated: Function,
    show: Boolean
})
const showModal = ref(props.show)
const onCancel = () => {
    console.log("cancelling the modal");
    showModal.value = false
    // TODO: perform some action
}

onMounted(() => {
    // initialize flowbite
    initFlowbite()

    // load zones only if not loaded
    if (!loadingZones.value.length){
        loading.value = true
        quartierApi.getZones().then(response => {
            if ('error' in response) {
                if (response.status && response.status === 401) {
                    router.push('/login')
                }
                else if (response.status && response.status === 403) {
                    router.push('/error/403')
                }
                else {
                    alert.value.showAlert("error", response.message, "error!!")
                }
                document.querySelector('button[type="submit"]').disabled = true
            }
            else {
                zones.value = response
            }
            loadingZones.value = false
            loading.value = false
        })
    }

    // close the modal when component is unmounted
    return () => {
        showModal.value = false
    }
})

const nomQuartier = ref('')
const sousQuartierAffich = ref('')
const observationsQuartier = ref('')
const arrondissementQuartier = ref('')
const iDZoneAffichage = ref('')

const loading = ref(false)
const buttonDisabled = ref(false)

// define a function to create a new zone
const createQuartier = () => {
    // TODO: perform some action to create a new zone
    if (!nomQuartier.value || !sousQuartierAffich.value || !observationsQuartier.value || !arrondissementQuartier.value) {
        return
    }
    if(!iDZoneAffichage.value){
        alert.value.showAlert("error", "Veuillez choisir une zone", "error!!")
        return
    }
    loading.value = true
    buttonDisabled.value = true
    // create a new quartier
    const newQuartier = {
        NomQuartier: nomQuartier.value,
        SousQuartierAffich: sousQuartierAffich.value,
        ObservationsQuartier: observationsQuartier.value,
        ArrondissementQuartier: arrondissementQuartier.value,
        IDZoneAffichage: iDZoneAffichage.value
    }

    // post request to the server
    axios.post('quartierAffichages', newQuartier)
        .then((response) => {
            console.log(response)
            // notify the parent component
            props.onQuartierCreated()
        })
        .catch((error) => {
            console.log(error)
            if(error.response.status === 401){
                router.push('/login')
            }
            else if(error.response.status === 403){
                router.push('/error/403')
            }
            else if ('data' in error.response && 'detail' in error.response.data) {
                alert.value.showAlert("error", error.response.data.detail, "error!!")
            }
            else {
                alert.value.showAlert("error", error.message, "error!!")
            }
        })
        .finally(() => {
            buttonDisabled.value = false
            loading.value = false
        })

}
</script>

<template>
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <Modal persistent v-if="showModal" @close="onCancel">
        <template #header>
            <div class="flex items-center text-lg text-center">
                Nouveau Quartier
            </div>
        </template>
        <template #body>

            <div class="px-6 py-6 lg:px-8">
                <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Creer un nouveau quartier</h3>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>

                <form class="space-y-6" @submit.prevent="createQuartier">
                    <div>
                        <label for="nomQuartier" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nom
                            Quartier</label>
                        <input type="text" v-model="nomQuartier" name="nomQuartier" id="nomQuartier"
                            placeholder="nom quartier"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="sousQuartierAffiche"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Sous Quartier
                            Affichage</label>
                        <input type="text" v-model="sousQuartierAffich" name="sousQuartierAffiche" id="sousQuartierAffiche"
                            placeholder="sous quartier"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="observationQuartier"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Observations
                            Quartier</label>
                        <input type="text" v-model="observationsQuartier" name="observationQuartier"
                            id="observationQuartier" placeholder="observations quartier"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="arrondissementQuartier"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Arrondissement
                            Quartier</label>
                        <input type="text" v-model="arrondissementQuartier" name="arrondissementQuartier"
                            id="arrondissementQuartier" placeholder="arrondissement quartier"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <!-- a selection list of zones -->
                    <label for="zoneAffichages" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Zone
                        Affichage</label>
                    <select id="zoneAffichages" v-model="iDZoneAffichage"
                        :class="zones.length === 0 ? 'border-red-500' : 'border-gray-300'"
                        class="bg-gray-50 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option value="" disabled selected>Select a zone</option>
                        <option v-for="zone in zones" :key="zone.id" :value="zone.IDZoneAffichage">{{ zone.LibelleZone }}
                        </option>
                    </select>
                    <div v-if="zones.length === 0" class="text-red-500 text-sm m-0">
                        No zones found.
                    </div>


                    <button type="submit" :disabled="buttonDisabled"
                        class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Créer
                        Nouveau Quartier</button>
                </form>
            </div>
        </template>
        <template #footer>
            <button @click="onCancel" type="button" :disabled="buttonDisabled"
                class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">
                Decline
            </button>
        </template>
    </Modal>
</template>
