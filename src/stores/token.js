// the store to manage the authentication token
import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'

export const useTokenStore = defineStore('token', {
    state: () => ({
        token: useLocalStorage('token', null)
    }),
    actions: {
        setToken(token) {
            this.token = token
        },
        getToken() {
            return this.token
        }
    }
})
