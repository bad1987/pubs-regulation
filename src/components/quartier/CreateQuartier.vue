<script setup>
import { ref, onMounted, defineAsyncComponent, defineProps } from 'vue'
import { initFlowbite } from 'flowbite'
import { Modal } from 'flowbite-vue'
import VueBasicAlert from 'vue-basic-alert'
import axios from 'axios'

const alert = ref(null)

const props = defineProps({
    onQuartierCreated: Function,
    show: Boolean
})
const showModal = ref(props.show)
const openModal = () => {
    showModal.value = true
}
const onConfirm = () => {
    showModal.value = false
    // TODO: perform some action
}
const onCancel = () => {
    console.log("cancelling the modal");
    showModal.value = false
    // TODO: perform some action
}

onMounted(() => {
    // initialize flowbite
    initFlowbite()
    // open the modal
    // openModal()

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
    if (!nomQuartier.value || !sousQuartierAffich.value) {
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
            if ('data' in error.response && 'detail' in error.response.data) {
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
                <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Fiche quartier</h3>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>

                <form class="space-y-6" @submit.prevent="createQuartier">
                    <div>
                        <label for="NomQuartier" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nom du Quartier</label>
                        <input type="text" v-model="NomQuartier" name="NomQuartier" id="NomQuartier" placeholder="Nom du quartier"
                            maxlength="6"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="SousQuartierAffich" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Sous-quartier</label>
                        <input type="text" v-model="SousQuartierAffich" name="SousQuartierAffich" id="SousQuartierAffich" placeholder="Sous quartier"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="ObservationsQuartier" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Observations</label>
                        <input type="text" v-model="ObservationsQuartier" name="ObservationsQuartier" id="ObservationsQuartier" placeholder="Observations"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="ArrondissementQuartier" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Arrondissement</label>
                        <input type="text" v-model="ArrondissementQuartier" name="ArrondissementQuartier" id="ArrondissementQuartier" placeholder="Arrondissement"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
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