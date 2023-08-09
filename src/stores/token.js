// the store to manage the authentication token
import { defineStore } from 'pinia'
import { useLocalStorage } from '@vueuse/core'

export const useTokenStore = defineStore('token', {
    state: () => ({
        token: useLocalStorage('token', null),
        user_data: null
    }),
    actions: {
        setToken(token) {
            this.token = token
        },
        getToken() {
            return this.token
        },
        clearToken() {
            this.token = null
            localStorage.removeItem('token')
        },
        setUser(user) {
            this.user_data = user
        },
        getUser() {
            return this.user_data
        },
        logout() {
            this.clearToken()
            this.user_data = null
        }
    }
})
