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

    axios.post('http://localhost:8000/user', postData)
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
    <Notification v-if="show_notification" :type="notification_type" :message="notification_message" :duration="notification_duration" />
    <div class="flex items-center justify-center min-h-screen  bg-green-300 dark:border-gray-700">
Liste des panneaux
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
}
</style>