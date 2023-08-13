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
const CreatePanneau = defineAsyncComponent(() => import('../views/CreatePanneau.vue'))
const CreateAnnonceur = defineAsyncComponent(() => import('../views/CreateAnnonceur.vue'))



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
      path: '/CreatePanneau',
      name: 'CreatePanneau',
      components: {
        navbar: Navbar,
        default: CreatePanneau
      }
    },
    {
      path: '/CreateAnnonceur',
      name: 'CreateAnnonceur',
      components: {
        navbar: Navbar,
        default: CreateAnnonceur
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
    }
  ]
})

export default router
