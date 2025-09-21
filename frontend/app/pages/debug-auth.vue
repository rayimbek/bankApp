<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold mb-6">Отладка аутентификации</h1>
    
    <div class="card mb-6">
      <h2 class="text-xl font-semibold mb-4">Состояние Auth Store</h2>
      <div class="space-y-2">
        <p><strong>isAuthenticated:</strong> {{ authStore.isAuthenticated }}</p>
        <p><strong>isAdmin:</strong> {{ authStore.isAdmin }}</p>
        <p><strong>Token:</strong> {{ authStore.token ? 'exists' : 'null' }}</p>
        <p><strong>User:</strong> {{ authStore.user ? JSON.stringify(authStore.user, null, 2) : 'null' }}</p>
      </div>
    </div>

    <div class="card mb-6">
      <h2 class="text-xl font-semibold mb-4">LocalStorage</h2>
      <div class="space-y-2">
        <p><strong>Token:</strong> {{ localStorageToken }}</p>
        <p><strong>User:</strong> {{ localStorageUser }}</p>
      </div>
    </div>

    <div class="card mb-6">
      <h2 class="text-xl font-semibold mb-4">Действия</h2>
      <div class="space-x-4">
        <button @click="reinitializeStore" class="btn-primary">
          Переинициализировать Store
        </button>
        <button @click="checkLocalStorage" class="btn-secondary">
          Проверить LocalStorage
        </button>
        <button @click="logout" class="btn-danger">
          Выйти
        </button>
      </div>
    </div>

    <div class="card">
      <h2 class="text-xl font-semibold mb-4">Тестовые ссылки</h2>
      <div class="space-x-4">
        <NuxtLink to="/profile" class="btn-primary">Профиль</NuxtLink>
        <NuxtLink to="/admin" class="btn-primary">Админка</NuxtLink>
        <NuxtLink to="/login" class="btn-secondary">Логин</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()
const localStorageToken = ref('')
const localStorageUser = ref('')

const checkLocalStorage = () => {
  if (process.client) {
    localStorageToken.value = localStorage.getItem('token') || 'null'
    localStorageUser.value = localStorage.getItem('user') || 'null'
  }
}

const reinitializeStore = () => {
  console.log('Reinitializing store...')
  authStore.initialize()
  checkLocalStorage()
  console.log('Store reinitialized')
}

const logout = () => {
  console.log('Logging out...')
  authStore.logout()
  checkLocalStorage()
  console.log('Logged out')
}

onMounted(() => {
  checkLocalStorage()
})
</script>
