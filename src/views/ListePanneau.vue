<script setup>
import { defineAsyncComponent, ref } from 'vue';
import VueBasicAlert from 'vue-basic-alert';

const CreatePanneau = defineAsyncComponent(() => import('../components/panneau/CreatePanneau.vue'));
const showCreatePanneau = ref(false);
const alert = ref(null);
const toggleCreatePanneau = () => {
  showCreatePanneau.value = !showCreatePanneau.value;
}
const onZoneCreated = () => {
  showCreatePanneau.value = false;
    alert.value.showAlert("Enregistrement effectué avec succès", "Nouveau Panneau crée", "success!!")
}

</script>

<template>
    <!-- <Notification v-if="show_notification" :type="notification_type" :message="notification_message" :duration="notification_duration" /> -->
    <!--  -->

    <Notification v-if="show_notification" :type="notification_type" :message="notification_message" :duration="notification_duration" />
    <vue-basic-alert ref="alert" :duration="1000" :closeIn="5000" />
    <!-- Add and style the main container -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
        <!-- Add and style the main header for this page with the page title:Zones. And a button to create a new zone at the right -->
        <header class="flex items-center justify-between w-full px-4 py-2 bg-white dark:bg-gray-800 shadow-lg">
            <h1 class="text-xl font-bold text-gray-800 dark:text-gray-200">Liste des Annonceurs</h1>
            <button @click="toggleCreateZone"
                class="px-3 py-1 text-sm font-medium text-white bg-blue-600 rounded hover:bg-blue-700">Créer un Annonceur</button>
        </header>
        <main class="px-4 py-4 text-gray-800 dark:text-gray-200">
            <!-- create zone component -->
            <CreateZone v-if="showCreateZone" :onZoneCreated="onZoneCreated" :show="showCreateZone" />
        </main>
    </div>

    <section class="bg-gray-50 dark:bg-gray-900  flex items-center">
  <div class="max-w-screen-xl px-4 mx-auto lg:px-12 w-full">
    <!-- Start coding here -->
    <div class="flex flex-col flex-1 p-4 overflow-y-auto ml-64 min-h-screen dark:bg-gray-900 dark:border-gray-700">
    <!-- <div class="relative bg-white shadow-md dark:bg-gray-800 sm:rounded-lg"> -->
      <div class="flex flex-col items-center justify-between p-4 space-y-3 md:flex-row md:space-y-0 md:space-x-4">
        <div class="w-full md:w-1/2">
          <form class="flex items-center">
            <label for="simple-search" class="sr-only">Search</label>
            <div class="relative w-full">
              <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
                </svg>
              </div>
              <input type="text" id="simple-search" class="block w-full p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Search" required="">
            </div>
          </form>
        </div>
        <div class="flex flex-col items-stretch justify-end flex-shrink-0 w-full space-y-2 md:w-auto md:flex-row md:space-y-0 md:items-center md:space-x-3">
            <RouterLink to="/createpanneau" :class="{ 'dark:bg-green-700 bg-green-100' : $route.fullPath == '/'  }" class="flex items-center p-2 text-base text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-700">Zone</RouterLink>
            <button type="button" class="flex items-center justify-center px-4 py-2 text-sm font-medium text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
            <svg class="h-3.5 w-3.5 mr-2" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
              <path clip-rule="evenodd" fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" />
            </svg>
            Add product
          </button>
          <div class="flex items-center w-full space-x-3 md:w-auto">
            <button id="actionsDropdownButton" data-dropdown-toggle="actionsDropdown" class="flex items-center justify-center w-full px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg md:w-auto focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700" type="button">
              <svg class="-ml-1 mr-1.5 w-5 h-5" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" />
              </svg>
              Actions
            </button>
            <div id="actionsDropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
              <ul class="py-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="actionsDropdownButton">
                <li>
                  <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Mass Edit</a>
                </li>
              </ul>
              <div class="py-1">
                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Delete all</a>
              </div>
            </div>
            <button id="filterDropdownButton" data-dropdown-toggle="filterDropdown" class="flex items-center justify-center w-full px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg md:w-auto focus:outline-none hover:bg-gray-100 hover:text-primary-700 focus:z-10 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700" type="button">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" class="w-4 h-4 mr-2 text-gray-400" viewbox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M3 3a1 1 0 011-1h12a1 1 0 011 1v3a1 1 0 01-.293.707L12 11.414V15a1 1 0 01-.293.707l-2 2A1 1 0 018 17v-5.586L3.293 6.707A1 1 0 013 6V3z" clip-rule="evenodd" />
              </svg>
              Filter
              <svg class="-mr-1 ml-1.5 w-5 h-5" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                <path clip-rule="evenodd" fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" />
              </svg>
            </button>
            <!-- Dropdown menu -->
            <div id="filterDropdown" class="z-10 hidden w-48 p-3 bg-white rounded-lg shadow dark:bg-gray-700">
              <ul class="space-y-2 text-sm" aria-labelledby="dropdownDefault">
                <li class="flex items-center">
                  <input id="apple" type="checkbox" value=""
                    class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                  <label for="apple" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-100">
                    Apple (56)
                  </label>
                </li>
                <li class="flex items-center">
                  <input id="fitbit" type="checkbox" value=""
                    class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                  <label for="fitbit" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-100">
                    Fitbit (56)
                  </label>
                </li>
                <li class="flex items-center">
                  <input id="dell" type="checkbox" value=""
                    class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                  <label for="dell" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-100">
                    Dell (56)
                  </label>
                </li>
                <li class="flex items-center">
                  <input id="asus" type="checkbox" value="" checked
                    class="w-4 h-4 bg-gray-100 border-gray-300 rounded text-primary-600 focus:ring-primary-500 dark:focus:ring-primary-600 dark:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                  <label for="asus" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-100">
                    Asus (97)
                  </label>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
    <!--  -->
    <div class="flex items-center justify-center mt-25px bg-yellow-300 dark:border-gray-700">
Liste des regisseurs
    </div>
<div class="flex items-center justify-center  overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-around text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">Product name</th>
                <th scope="col" class="px-6 py-3">Color</th>
                <th scope="col" class="px-6 py-3">Category</th>
                <th scope="col" class="px-6 py-3">Price</th>
                <th scope="col" class="px-6 py-3">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">Apple MacBook Pro 17"</th>
                <td class="px-6 py-4">Silver</td>
                <td class="px-6 py-4">Laptop</td>
                <td class="px-6 py-4">$2999</td>
                <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a></td>
            </tr>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">Microsoft Surface Pro</th>
                <td class="px-6 py-4">White</td>
                <td class="px-6 py-4">Laptop PC</td>
                <td class="px-6 py-4">$$1999</td>
                <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a></td>
            </tr>
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">Microsoft Surface Pro</th>
                <td class="px-6 py-4">White</td>
                <td class="px-6 py-4">Laptop PC</td>
                <td class="px-6 py-4">$1999</td>
                <td class="px-6 py-4"><a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a></td>
            </tr>
        </tbody>
    </table>
</div>

</template>

<style scoped>
select {
    display: flex;
    align-items: center;
    border: 1px solid #4d4d4d;
    border-radius: 0.5rem;
    background-color: #f5f5f5;
    color: #4d4d4d;
    padding: 0.8rem 1.2rem;
    appearance: none;
    cursor: pointer;
    transition: all 0.3s ease;
}

select:hover,
select:focus {
    background-color: #e6e6e6;
    border-color: #228bec;
}

select::after {
    content: "▼";
    position: absolute;
    right: 1.2rem;
    top: 50%;
    transform: translateY(-50%);
}
</style>