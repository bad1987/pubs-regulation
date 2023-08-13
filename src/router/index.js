import { createRouter, createWebHistory } from 'vue-router'
import { defineAsyncComponent } from 'vue'

// Define components as async
const HomeView = defineAsyncComponent(() => import('../views/HomeView.vue'))
const Navbar = defineAsyncComponent(() => import('../components/Navbar.vue'))
const Sidebar = defineAsyncComponent(() => import('../components/Sidebar.vue'))
const RegistrationVue = defineAsyncComponent(() => import('../views/RegistrationVue.vue'))
const Login = defineAsyncComponent(() => import('../views/Login.vue'))
const ListePanneau = defineAsyncComponent(() => import('../views/ListePanneau.vue'))
const ListeAnnonceur = defineAsyncComponent(() => import('../views/ListeAnnonceur.vue'))
const ListeRegisseur = defineAsyncComponent(() => import('../views/ListeRegisseur.vue'))
const DashBoard = defineAsyncComponent(() => import('../views/DashBoard.vue'))
const Error403 = defineAsyncComponent(() => import('../components/errors/Error403.vue'))
const Error404 = defineAsyncComponent(() => import('../components/errors/Error404.vue'))
const ZoneView = defineAsyncComponent(() => import('../views/ZoneView.vue'))

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
    },
    {
      path: '/ListeAnnonceur',
      name: 'ListeAnnonceur',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: ListeAnnonceur
      }
    },
    {
      path: '/ListeRegisseur',
      name: 'ListeRegisseur',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: ListeRegisseur
      }
    },
    {
      path: '/DashBoard',
      name: 'DashBoard',
      components: {
        navbar: Navbar,
        default: DashBoard
      }
    },
    {
      path: '/ListePanneau',
      name: 'ListePanneau',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: ListePanneau
      }
    }, 
    {
      path: '/error/403',
      name: '403',
      component: Error403
    },
    {
      path: '/:catchAll(.*)',
      name: '404',
      component: Error404
    },
    {
      path: '/zones',
      name: 'ZoneView',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: ZoneView
      }
    },
  ]
})

export default router
