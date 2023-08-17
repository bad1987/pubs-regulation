import { createRouter, createWebHistory } from 'vue-router'
import { defineAsyncComponent } from 'vue'

// Define components as async
const HomeView = defineAsyncComponent(() => import('../views/HomeView.vue'))
const Navbar = defineAsyncComponent(() => import('../components/Navbar.vue'))
const Sidebar = defineAsyncComponent(() => import('../components/Sidebar.vue'))
const RegistrationVue = defineAsyncComponent(() => import('../views/RegistrationVue.vue'))
const Login = defineAsyncComponent(() => import('../views/Login.vue'))
const ListePanneau = defineAsyncComponent(() => import('../views/ListePanneau.vue'))
const ListeRegisseur = defineAsyncComponent(() => import('../views/ListeRegisseur.vue'))
const DashBoard = defineAsyncComponent(() => import('../views/DashBoard.vue'))
const CreatePanneau = defineAsyncComponent(() => import('../components/panneau/CreatePanneau.vue'))
const AnnonceurView = defineAsyncComponent(() => import('../views/AnnonceurView.vue'))
const Error403 = defineAsyncComponent(() => import('../components/errors/Error403.vue'))
const Error404 = defineAsyncComponent(() => import('../components/errors/Error404.vue'))
const ZoneView = defineAsyncComponent(() => import('../views/ZoneView.vue'))
const QuartierView = defineAsyncComponent(() => import('../views/QuartierView.vue'))
const EmplacementView = defineAsyncComponent(() => import('../views/EmplacementView.vue'))
const ProduitView = defineAsyncComponent(() => import('../views/ProduitView.vue'))
const TypeenseigneView = defineAsyncComponent(() => import('../views/TypeenseigneView.vue'))
const TypepanneauView = defineAsyncComponent(() => import('../views/TypepanneauView.vue'))
const TiersView = defineAsyncComponent(() => import('../views/TiersView.vue'))

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
      path: '/annonceur',
      name: 'AnnonceurView',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: AnnonceurView
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
        sidebar: Sidebar,
        navbar: Navbar,
        default: DashBoard
      }
    },
    {
      path: '/createpanneau',
      name: 'createpanneau',
      components: {
        sidebar: Sidebar,
        navbar: Navbar,
        default: CreatePanneau
      }
    },
    {
      path: '/typeenseigne',
      name: 'TypeenseigneView',
      components: {
        sidebar: Sidebar,
        navbar: Navbar,
        default: TypeenseigneView
      }
    },
    {
      path: '/typepanneau',
      name: 'TypepanneauView',
      components: {
        sidebar: Sidebar,
        navbar: Navbar,
        default: TypepanneauView
      }
    },
    {
      path: '/produit',
      name: 'ProduitView',
      components: {
        sidebar: Sidebar,
        navbar: Navbar,
        default: ProduitView
      }
    },
    {
      path: '/annonceur',
      name: 'AnnonceurView',
      components: {
        sidebar: Sidebar,
        navbar: Navbar,
        default: AnnonceurView
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
      path: '/zones',
      name: 'ZoneView',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: ZoneView
      }
    },
    {
      path: '/quartier',
      name: 'QuartierView',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: QuartierView
      }
    },
    {
      path: '/emplacement',
      name: 'EmplacementView',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: EmplacementView
      }
    },
    {
      path: '/tiers',
      name: 'TiersView',
      components: {
        navbar: Navbar,
        sidebar: Sidebar,
        default: TiersView
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
  ]
})

export default router
