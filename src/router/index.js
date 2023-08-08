import { createRouter, createWebHistory } from 'vue-router'
import { defineAsyncComponent } from 'vue'

// define components as async components
const HomeView = defineAsyncComponent(() => import('../views/HomeView.vue'))
const Login = defineAsyncComponent(() => import('../views/Login.vue'))
const RegistrationVue = defineAsyncComponent(() => import('../views/RegistrationVue.vue'))
const Navbar = defineAsyncComponent(() => import('../components/Navbar.vue'))
const Sidebar = defineAsyncComponent(() => import('../components/Sidebar.vue'))

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: HomeView,
        navbar: Navbar,
        sidebar: Sidebar
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
      component: RegistrationVue
    }
  ]
})

export default router
