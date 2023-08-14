<script setup>
import { ref, onMounted, defineAsyncComponent, defineProps } from 'vue'
import { initFlowbite } from 'flowbite'
import { Modal } from 'flowbite-vue'
import VueBasicAlert from 'vue-basic-alert'
import axios from 'axios'

const alert = ref(null)

const props = defineProps({
    onAnnonceurCreated: Function,
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

const codeTiers = ref('')
const libelleTiers = ref('')
const adresseTiers = ref('')
const telephoneTiers = ref('')
const iDTypeTiers = ref('')
const numCont = ref('')
const emailTiers = ref('')
const logo = ref('')
const sigleTiers = ref('')

const loading = ref(false)
const buttonDisabled = ref(false)

// define a function to create a new Annonceur
const createAnnonceur = () => {
    // TODO: perform some action to create a new Annonceur
    if (!CodeTiers.value || !LibelleTiers.value) {
        return
    }
    loading.value = true
    buttonDisabled.value = true
    // create a new zone
    const newAnnonceur = {
        CodeTiers: codeTiers.value,
        LibelleTiers: libelleTiers.value,
        AdresseTiers: adresseTiers.value,
        TelephoneTiers: telephoneTiers.value,
        IDTypeTiers: iDTypeTiers.value,
        NumCont: numCont.value,
        EmailTiers: emailTiers.value,
        SigleTiers: sigleTiers.value
    }

    // post request to the server
    axios.post('tiers', newAnnonceur)
    .then((response) => {
            console.log(response)
            // notify the parent component
            props.onAnnonceurCreated()
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
                Nouvel Annonceur
            </div>
        </template>
        <template #body>

            <div class="px-6 py-6 lg:px-8">
                <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Fiche Annonceur</h3>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>

                <form class="space-y-6" @submit.prevent="createAnnonceur">
                    <div>
                        <label for="codeTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Code Annonceur</label>
                        <input type="text" v-model="codeTiers" name="codeTiers" id="codeTiers" placeholder="code Tiers"
                            maxlength="6"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="libelleTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Libelle</label>
                        <input type="text" v-model="libelleTiers" name="libelleTiers" id="libelleTiers" placeholder="Nom Annonceur"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="adresseTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Adresse</label>
                        <input type="text" v-model="adresseTiers" name="adresseTiers" id="adresseTiers" placeholder="Adresse"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="telephoneTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Téléphone</label>
                        <input type="text" v-model="telephoneTiers" name="telephoneTiers" id="telephoneTiers" placeholder="Téléphone"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="emailTiers" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
                        <input type="text" v-model="emailTiers" name="emailTiers" id="emailTiers" placeholder="Email"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    <div>
                        <label for="numCont" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">N° Contribuable</label>
                        <input type="text" v-model="numCont" name="numCont" id="numCont" placeholder="N° Contribuable"
                            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                            required>
                    </div>
                    
                    <button type="submit" :disabled="buttonDisabled"
                        class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Create
                        Créer</button>
                </form>
            </div>
        </template>
        <template #footer>
            <button @click="onCancel" type="button" :disabled="buttonDisabled"
                class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">
                Annuler
            </button>
        </template>
</Modal>
</template>