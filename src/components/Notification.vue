<template>
    <div v-if="show" class="notification" :class="type">
        <span class="close" @click="close">×</span>
        <p>{{ message }}</p>
    </div>
</template>
  
<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'

// declare props using TypeScript
const props = defineProps<{
    type: string
    message: string
    duration: number
}>()

// destructure props for convenience
const { type, message, duration } = props

// define reactive state using const
const show = ref(true)

// define methods using regular functions
const close = () => {
    show.value = false
}
// define a variable to store the timeout function
//   let timer = null

//   set the timer when the component is mounted
onMounted(() => {
    let timer = setTimeout(() => {
        show.value = false
    }, duration);

    () => {
        clearTimeout(timer)
    }
})

</script>
  
<style>
.notification {
    position: fixed;
    top: 1rem;
    right: 1rem;
    padding: 1rem;
    border-radius: 0.5rem;
}

.success {
    background-color: #d4edda;
    color: #155724;
}

.error {
    background-color: #f8d7da;
    color: #721c24;
}

.warning {
    background-color: #fff3cd;
    color: #856404;
}

.info {
    background-color: #d1ecf1;
    color: #0c5460;
}

.close {
    cursor: pointer;
}
</style>
  