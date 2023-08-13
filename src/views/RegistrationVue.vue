<script setup>
import { RouterLink } from 'vue-router'
import { ref, watch } from 'vue';
import axios from 'axios'
import { UserRoleEnum, UserStatusEnum } from '../utils/userUtils.js'
import Notification from '../components/Notification.vue'

const userRoles = Object.values(UserRoleEnum)
const userStatuses = Object.values(UserStatusEnum)
const error = ref(null);
const loading = ref(false);
// define variables for the form data
const username = ref('');
const status = ref(UserStatusEnum.ACTIVE);
const roles = ref(UserRoleEnum.OPERATOR);
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

// repeatPassword
const repeatPassword = ref('');
const repeatPasswordError = ref(false)
function validateRepeatPassword() {
    if (!repeatPassword.value) {
        repeatPasswordError.value = true
    }
    else if (password.value !== repeatPassword.value) {
        repeatPasswordError.value = true
    }
    else {
        repeatPasswordError.value = false
    }
}

// make email and password fields appear normal when the user start typing
watch(email, () => {
    validateEmail()
})
watch(password, () => {
    validatePassword()
})
watch(repeatPassword, () => {
    validateRepeatPassword()
})

// notification variables
const notification_type = ref('info')
const notification_message = ref('registration successful')
const notification_duration = ref(5000)
const show_notification = ref(false)

const register = async (event) => {
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
    // validate repeat password
    validateRepeatPassword();
    if (repeatPasswordError.value) {
        return;
    }

    loading.value = true;
    error.value = null;
    show_notification.value = false

    // build the form data
    const postData = {
        email: email.value,
        password: password.value,
        username: username.value,
        status: status.value,
        roles: roles.value
    }

    axios.post('user', postData)
        .then((response) => {
            console.log(response);
            // set the notification message
            notification_message.value = 'registration successful';
            notification_type.value = 'success';
        })
        .catch((_error) => {
            // if network error
            console.log(_error);
            if (_error.code && _error.code === 'ERROR_NETWORK' || _error.code === "ERR_NETWORK") {
                error.value = _error.message;
            } else {
                console.log(_error);
                if ('data' in _error.response && 'detail' in _error.response.data) {
                    error.value = _error.response.data.detail;
                }
                else {
                    error.value = _error.message;
                }

            }
            notification_message.value = error.value;
            notification_type.value = 'error';
        })
        .finally(() => {
            loading.value = false;
            show_notification.value = true;
        })
}
</script>

<template>
    <Notification v-if="show_notification" :type="notification_type" :message="notification_message"
        :duration="notification_duration" />
    <div class="flex items-center justify-center min-h-screen  dark:bg-gray-800 dark:border-gray-700">
        <div class="rounded-sm bg-white shadow-default  dark:bg-gray-800 dark:border-gray-700 w-2/4">
            <div class="w-full p-4 sm:p-12.5 xl:p-17.5">

                <h2
                    class="mb-9 text-lg sm:text-xl md:text-2xl lg:text-3xl font-bold text-black dark:text-white sm:text-title-xl2">
                    Sign Up to Ads Regulator
                </h2>

                <div v-if="loading"
                    class="fixed top-0 left-0 w-full h-full flex justify-center items-center bg-black bg-opacity-50 z-50">
                    <div class="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
                </div>

                <form>
                    <div class="grid gap-6 mb-6 md:grid-cols-2">
                        <div>
                            <label for="username"
                                class="mb-2.5 block font-medium text-black dark:text-white">Username</label>
                            <input type="text" placeholder="Enter your username" v-model="username"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                id="username" required />
                        </div>

                        <div>
                            <label for="email" class="mb-2.5 block font-medium text-black dark:text-white">Email</label>
                            <input type="email" id="email" placeholder="Enter your email" v-model="email"
                                :class="[emailError ? 'border-red-500' : '', 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500']" />
                        </div>

                        <div>
                            <label for="password"
                                class="mb-2.5 block font-medium text-black dark:text-white">Password</label>
                            <input type="password" id="password" placeholder="Enter your password" v-model="password"
                                :class="[passwordError ? 'border-red-500' : '', 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500']" />
                        </div>

                        <div>
                            <label class="mb-2.5 block font-medium text-black dark:text-white">Re-type Password</label>
                            <input type="password" placeholder="Enter your password" v-model="repeatPassword"
                                :class="[repeatPasswordError ? 'border-red-500' : '', 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500']" />
                        </div>

                        <div>
                            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">User Role</label>
                            <select v-model="roles"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                <option v-for="role in userRoles" :value="role" :key="role">{{ role }}</option>
                            </select>
                            <!-- <div class="relative">
                            </div> -->
                        </div>

                        <div>

                            <label for="status" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">User
                                Status</label>
                            <select v-model="status" id="status"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                <option v-for="status in userStatuses" :value="status" :key="status">{{ status }}</option>
                            </select>

                        </div>
                        <div>

                            <button @click="register"
                                class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-900">
                                Sign Up
                            </button>
                        </div>

                        <div class="mt-6 text-center">
                            <p class="font-medium text-sm text-gray-900 dark:text-white">
                                Already have an account?
                                <RouterLink to="/login"
                                    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
                                    Sign in</RouterLink>
                            </p>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
select {
    display: flex;
    align-items: center;
    border: 1px solid #4d4d4d;
    border-radius: 0.5rem;
    background-color: #f5f5f5;
    color: #4d4d4d;
    padding: 0.8rem 1.2rem;
    appearance: none;
    cursor: pointer;
    transition: all 0.3s ease;
}

select:hover,
select:focus {
    background-color: #e6e6e6;
    border-color: #228bec;
}

select::after {
    content: "▼";
    position: absolute;
    right: 1.2rem;
    top: 50%;
    transform: translateY(-50%);
}</style>