<script setup>
import { storeToRefs } from 'pinia';
import { useThemeStore } from '../stores/darkmode.js'
import { initFlowbite } from 'flowbite'
import { onBeforeMount, onMounted, ref } from 'vue';
import { RouterLink } from 'vue-router';

// initialize components based on data attribute selectors
  onMounted(() => {
      initFlowbite();
  })
const themeStore = useThemeStore()

const { isDark } = storeToRefs(themeStore)
const actual = 'en'

const user = ref(null)

function changeLanguage (lang) {

}


onMounted(async () => {
  initFlowbite()

  const btnToggle = document.getElementById("btn-toggle-sidebar")
  const sidebar = document.getElementById("logo-sidebar")
  const overlay = document.getElementById("app-overlay")

  if(btnToggle){
    btnToggle.addEventListener("click", function (e) {
    e.stopPropagation()
    sidebar.classList.toggle("-translate-x-full")
    overlay.classList.toggle("hidden")
  })
  }

  if(overlay){
    overlay.addEventListener("click", function(e) {
    e.stopPropagation()
    sidebar.classList.toggle("-translate-x-full")
    overlay.classList.toggle("hidden")
  })
  }
})


// logout
const handleLogout = event => {
}
</script>

<template>
 
</template> 