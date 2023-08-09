<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
import { onBeforeMount, onMounted } from 'vue';
import { useTokenStore } from './stores/token';
import axios from 'axios';
import { useRouter } from 'vue-router';


onBeforeMount(() => {
  // use useRouter to get a router instance
  const router = useRouter();
  const authStore = useTokenStore();
  // check if the user is already loaded in the store. if not, get him from the backend
  if (!authStore.user) {
    axios.get("http://localhost:8000/auth/user/data")
    .then(response =>{
      authStore.setUser(response.data.user)
    })
    .catch(err=>{
      console.log(err)
      if('response' in err && err.response.status == 401){
        router.push("/login")
      }
      else{
        console.log("conditions not met");
      }
    })
  }
});

</script>

<template>
  <!-- Render the navbar component -->
  <router-view name="navbar"></router-view>
  
  <!-- Render the sidebar component -->
  <router-view name="sidebar"></router-view>
  <div :class="{'mt-14': $route.name !== 'login'}" class="rounded-lg dark:border-gray-700">
    <!-- Render the default component -->
    <router-view class="min-h-screen"></router-view>
  </div>
</template>
