<!-- create vue 3 component -->
<script setup>
import { ref, watch, onMounted } from 'vue';
import axios from 'axios'
import { useTokenStore } from '../stores/token';
import { useRouter } from 'vue-router';
import { useThemeStore } from '../stores/darkmode.js'
import { initFlowbite } from 'flowbite'
import { storeToRefs } from 'pinia';

const themeStore = useThemeStore();
const { changeMode } = storeToRefs(themeStore)

onMounted(() => {
    initFlowbite()
    themeStore.changeMode()
})

// use useRouter to get a router instance
const router = useRouter();

const error = ref(null);
const loading = ref(false);
// define variables for the form data
const email = ref('');
const emailError = ref(false)
function validateEmail() {
    if (!email.value) {
        emailError.value = true
    }
    else {
        // make sure the follows a valid email format
        emailError.value = !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(email.value)
    }
}
const password = ref('');
const passwordError = ref(false)
function validatePassword() {
    if (!password.value) {
        passwordError.value = true
    } else {
        passwordError.value = false
    }
}

// make email and password fields appear normal when the user start typing
watch(email, () => {
    validateEmail()
})
watch(password, () => {
    validatePassword()
})

const login = async (event) => {
    event.preventDefault();
    // validate email
    validateEmail();
    if (emailError.value) {
        return;
    }
    // validate password
    validatePassword();
    if (passwordError.value) {
        return;
    }

    loading.value = true;
    error.value = null;

    // build the form data
    const formData = new FormData();
    formData.append('username', email.value);
    formData.append('password', password.value);

    axios.post('login', formData)
        .then((response) => {
            // get token from response
            const token = response.data.access_token;
            const user = response.data.user;
            const authStore = useTokenStore();
            authStore.setToken(token);
            authStore.setUser(user);
            router.push('/');
        })
        .catch((_error) => {
            // if network error
            console.log(_error);
            if (_error.code && _error.code === 'ERROR_NETWORK') {
                error.value = 'Network Error';
            } else {
                console.log(_error);
                if ('data' in _error.response && 'detail' in _error.response.data) {
                    error.value = _error.response.data.detail;
                }
                else {
                    error.value = _error.message;
                }

            }
        })
        .finally(() => {
            loading.value = false;
        })
}
</script>

<template>
    <section class="bg-gray-50 dark:bg-gray-900">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
            <img class="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="logo">
            Ads Regulator
        </a>
        <div
            class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                    Sign in to your account
                </h1>
                <div v-if="error" class="mb-4 p-2 rounded border border-red-500 bg-red-100 text-red-700">
                    {{ error }}
                </div>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>
                <form class="space-y-4 md:space-y-6" action="#">
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your
                            email</label>
                        <input type="email" name="email" id="email" v-model="email"
                            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                placeholder="name@company.com" required="">
                        </div>
                        <div>
                            <label for="password"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                            <input type="password" name="password" id="password" v-model="password" placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                required="">
                        </div>
                        <div class="flex items-center justify-between">
                            <div class="flex items-start">
                                <div class="flex items-center h-5">
                                    <input id="remember" aria-describedby="remember" type="checkbox"
                                        class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800">
                                </div>
                                <div class="ml-3 text-sm">
                                    <label for="remember" class="text-gray-500 dark:text-gray-300">Remember me</label>
                                </div>
                            </div>
                            <a href="#"
                                class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">Forgot
                                password?</a>
                        </div>
                        <button @click="login"
                            class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Sign
                            in</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>