
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { useAuthStore } from "../stores/auth"

const authStore = useAuthStore()

onMounted(() => {
  authStore.initialize()
})
</script>

<style>
@import url('../assets/css/main.css');
</style>
