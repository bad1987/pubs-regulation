<script setup>
import { ref, onMounted, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { initFlowbite } from 'flowbite'
import { Modal } from 'flowbite-vue'
import VueBasicAlert from 'vue-basic-alert'
import axios from 'axios'
import { quartierApi } from '../../api/api'
import { useQuartierStore } from "../../stores/quartierStore"

const quartierStore = useQuartierStore()
const typesOfTiers = ref([])
const loadingZones = ref(true)
const router = useRouter()
const alert = ref(null)

const props = defineProps({
    onTiersCreated: Function,
    show: Boolean
})
const showModal = ref(props.show)
const onCancel = () => {
    console.log("Cancelling the modal");
    showModal.value = false
    // TODO: Perform some action
}

onMounted(() => {
    // Initialize flowbite
    initFlowbite()

    // Load types of tiers only if not loaded
    if (!typesOfTiers.value.length) {
        loadingTypesOfTiers.value = true
        quartierApi.getTypesOfTiers()
            .then(response => {
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
                    typesOfTiers.value = response
                }
                loadingTypesOfTiers.value = false
                loading.value = false
            })
    }

    // Close the modal when the component is unmounted
    return () => {
        showModal.value = false
    }
})

const CodeTiers = ref('')
const LibelleTiers = ref('')
const AdresseTiers = ref('')
const TelephoneTiers = ref('')
const UpdatedAt = ref('')
const CreatedAt = ref('')
const IDTypeTiers = ref('')
const NumCont = ref('')
const EmailTiers = ref('')
const Logo = ref('')
const SigleTiers = ref('')

const loading = ref(false)
const buttonDisabled = ref(false)

// Define a function to create a new Tiers
const createTiers = () => {
    // TODO: Perform some action to create a new Tiers
    if (!LibelleTiers.value || !AdresseTiers.value || !TelephoneTiers.value) {
        return
    }
    // Additional validation and data preparation if needed

    loading.value = true
    buttonDisabled.value = true

    // Create a new Tiers object
    const newTiers = {
        LibelleTiers: LibelleTiers.value,
        AdresseTiers: AdresseTiers.value,
        TelephoneTiers: TelephoneTiers.value,
        UpdatedAt: UpdatedAt.value,
        CreatedAt: CreatedAt.value,
        IDTypeTiers: IDTypeTiers.value,
        NumCont: NumCont.value,
        EmailTiers: EmailTiers.value,
        Logo: Logo.value,
        SigleTiers: SigleTiers.value
    }

    // Send a post request to the server
    axios.post('tiers', newTiers)
        .then((response) => {
            console.log(response)
            // Notify the parent component
            props.onTiersCreated()
        })
        .catch((error) => {
            // Handle error cases
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
    <Modal persistent v-if="showModal" @close="onCancel">
        <template #header>
            <div class="flex items-center text-lg text-center">
                Nouveau Tiers
            </div>
        </template>
        <template #body>
            <div class="px-6 py-6 lg:px-8">
                <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Créer un nouveau Tiers</h3>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>

                <form class="space-y-6" @submit.prevent="createTiers">
                    <div>
                        <label for="libelleTiers"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Libellé Tiers</label>
                        <input type="text" v-model="LibelleTiers" name="libelleTiers" id="libelleTiers"
                            placeholder="libellé tiers"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="adresseTiers"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Adresse Tiers</label>
                        <input type="text" v-model="AdresseTiers" name="adresseTiers" id="adresseTiers"
                            placeholder="adresse tiers"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="telephoneTiers"
                            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Téléphone Tiers</label>
                        <input type="text" v-model="TelephoneTiers" name="telephoneTiers" id="telephoneTiers"
                            placeholder="téléphone tiers"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="idTypeTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">ID
                            Type Tiers</label>
                        <input type="text" v-model="IDTypeTiers" name="idTypeTiers" id="idTypeTiers"
                            placeholder="ID type tiers"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white">
                    </div>
                    <div>
                        <label for="numCont" class="block mb-2 text-sm font-mediumtext-gray-900 dark:text-white">Numéro de
                            Contact</label>
                        <input type="text" v-model="NumCont" name="numCont" id="numCont" placeholder="numéro de contact"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white">
                    </div>
                    <div>
                        <label for="emailTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email
                            Tiers</label>
                        <input type="text" v-model="EmailTiers" name="emailTiers" id="emailTiers" placeholder="email tiers"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white">
                    </div>
                    <div>
                        <label for="logo" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Logo</label>
                        <input type="text" v-model="Logo" name="logo" id="logo" placeholder="logo"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white">
                    </div>
                    <div>
                        <label for="sigleTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Sigle
                            Tiers</label>
                        <input type="text" v-model="SigleTiers" name="sigleTiers" id="sigleTiers" placeholder="sigle tiers"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white">
                    </div>

                    <label for="typesOfTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Types
                        of Tiers</label>
                    <select id="typesOfTiers" v-model="IDTypeTiers"
                        :class="typesOfTiers.length === 0 ? 'border-red-500' : 'border-gray-300'"
                        class="bg-gray-50 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option value="" disabled selected>Select a type</option>
                        <option v-for="type_tiers in typesOfTiers" :key="type_tiers.IDTypeTiers"
                            :value="type_tiers.IDTypeTiers">{{ type_tiers.LibelleTypeTiers }}</option>
                    </select>
                    <div v-if="typesOfTiers.length === 0" class="text-red-500 text-sm m-0">
                        No types found.
                    </div>

                    <div class="flex justify-end">
                        <button type="submit" :disabled="buttonDisabled"
                            class="px-4 py-2 text-sm font-medium text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
                            Créer Tiers
                        </button>
                    </div>
                </form>
            </div>
        </template>
    </Modal>
</template>