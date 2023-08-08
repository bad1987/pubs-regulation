import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'

import App from './App.vue'
import router from './router'
import { useTokenStore } from './stores/token'

// Set up an axios interceptor that adds the token to the Authorization header
axios.interceptors.request.use((config) => {
    // get the token from the store
    const token = useTokenStore().getToken()
    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
