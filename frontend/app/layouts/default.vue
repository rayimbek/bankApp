
<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white shadow-sm border-b">
      <div class="container mx-auto px-4 py-4">
        <div class="flex justify-between items-center">
          <NuxtLink to="/" class="text-xl font-bold text-blue-600">
            🏦 Bank App
          </NuxtLink>

          <nav class="flex items-center space-x-4">
            <NuxtLink
              to="/banks"
              class="text-gray-600 hover:text-gray-900 transition-colors"
            >
              Банки
            </NuxtLink>

            <NuxtLink
              v-if="authStore.isAdmin"
              to="/admin"
              class="text-gray-600 hover:text-gray-900 transition-colors"
            >
              Админка
            </NuxtLink>

            <NuxtLink
              v-if="authStore.isAuthenticated"
              to="/profile"
              class="text-gray-600 hover:text-gray-900 transition-colors"
            >
              Профиль
            </NuxtLink>

            <button
              v-if="authStore.isAuthenticated"
              @click="logout"
              class="text-gray-600 hover:text-gray-900 transition-colors"
            >
              Выйти
            </button>

            <NuxtLink
              v-else
              to="/login"
              class="text-gray-600 hover:text-gray-900 transition-colors"
            >
              Войти
            </NuxtLink>
          </nav>
        </div>
      </div>
    </header>

    <main class="container mx-auto px-4 py-8">
      <slot />
    </main>

    <footer class="bg-white border-t mt-12">
      <div class="container mx-auto px-4 py-6 text-center text-gray-600">
        © 2024 Bank App. Все права защищены.
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../stores/auth'

const authStore = useAuthStore()

const logout = () => {
  authStore.logout()
  if (process.client) {
    navigateTo('/')
  }
}
</script>
