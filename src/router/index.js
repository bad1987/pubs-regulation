import { createRouter, createWebHistory } from 'vue-router'
import { defineAsyncComponent } from 'vue'

// Define components as async
const HomeView = defineAsyncComponent(() => import('../views/HomeView.vue'))
const Navbar = defineAsyncComponent(() => import('../components/Navbar.vue'))
const Sidebar = defineAsyncComponent(() => import('../components/Sidebar.vue'))
const RegistrationVue = defineAsyncComponent(() => import('../views/RegistrationVue.vue'))
const Login = defineAsyncComponent(() => import('../views/Login.vue'))

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: HomeView
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/registration',
      name: 'registration',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: RegistrationVue
      }
    }
  ]
})

export default router
