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
const quartiers = ref(quartierStore.quartiers)
const router = useRouter()
const alert = ref(null)

const props = defineProps({
    onEmplacementCreated: Function,
    show: Boolean
})
const showModal = ref(props.show)
const onCancel = () => {
    showModal.value = false
    // TODO: perform some action
}

onMounted(() => {
    // initialize flowbite
    initFlowbite()

    // load quartiers if not loaded
    if (!quartiers.value.length) {
        loading.value = true
        quartierApi.getQuartiers().then(response => {
            if ('error' in response) {
                if (response.status && response.status === 401) {
                    router.push('/login')
                } else if (response.status && response.status === 403) {
                    router.push('/error/403')
                } else {
                    alert.value.showAlert("error", response.message, "error!!")
                }
                document.querySelector('button[type="submit"]').disabled = true
            } else {
                quartiers.value = response
            }
            loading.value = false
        })
    }

    // close the modal when component is unmounted
    return () => {
        showModal.value = false
    }
})

const CodeEmplacement = ref('')
const IDQuartierAffichage = ref('')
const loading = ref(false)
const buttonDisabled = ref(false)

// define a function to create a new zone
const createEmplacement = () => {
    // TODO: perform some action to create a new zone
    if (!CodeEmplacement.value) {
        alert.value.showAlert("error", "Veuillez renseigner le code de l'emplacement", "error!!")
        return
    }
    if (!IDQuartierAffichage.value) {
        alert.value.showAlert("error", "Veuillez selectionner un quartier", "error!!")
        return
    }
    loading.value = true
    buttonDisabled.value = true
    // create a new emplacement
    const newEmplacement = {
        CodeEmplacement: CodeEmplacement.value,
        IDQuartierAffichage: IDQuartierAffichage.value
    }

    // post request to the server
    axios.post('emplacementAffichage', newEmplacement)
        .then((response) => {
            // notify the parent component
            props.onEmplacementCreated()
        })
        .catch((error) => {
            console.log(error)
            if (error.response.status === 401) {
                router.push('/login')
            }
            else if (error.response.status === 403) {
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
                Nouvel Emplacement
            </div>
        </template>
        <template #body>

            <div class="px-6 py-6 lg:px-8">
                <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Fiche Emplacement</h3>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>

                <form class="space-y-6" @submit.prevent="createEmplacement">
                    <div>
                        <label for="CodeEmplacement"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Code Emplacement</label>
                        <input type="text" v-model="CodeEmplacement" name="CodeEmplacement" id="CodeEmplacement"
                            placeholder="code emplacement"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="quartier"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Quartier</label>
                        <select id="quartier" v-model="IDQuartierAffichage"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                            <option value="" disabled selected>selectionner un quartier</option>
                            <option v-for="quartier in quartiers" :key="quartier.IDQuartierAffichage"
                                :value="quartier.IDZoneAffichage">{{ quartier.NomQuartier }}</option>
                        </select>
                        <div v-if="quartiers.length === 0" class="text-red-500 text-sm m-0">
                            No quartier found.
                        </div>
                    </div>
                    <button type="submit" :disabled="buttonDisabled"
                        class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Create
                        Nouvel Emplacement</button>
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