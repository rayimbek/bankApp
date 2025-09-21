
<template>
  <div class="text-center">
    <div class="max-w-2xl mx-auto">
      <h1 class="text-4xl font-bold text-gray-900 mb-6">
        Добро пожаловать в Bank App
      </h1>

      <p class="text-xl text-gray-600 mb-8">
        Современная система для просмотра и управления информацией о банках
      </p>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
        <div class="bg-white p-6 rounded-lg shadow-md text-center">
          <div class="text-3xl mb-2">🏦</div>
          <h3 class="font-semibold mb-2">Просмотр банков</h3>
          <p class="text-gray-600 text-sm">Изучите подробную информацию о банках</p>
        </div>

        <div class="bg-white p-6 rounded-lg shadow-md text-center">
          <div class="text-3xl mb-2">🔍</div>
          <h3 class="font-semibold mb-2">Поиск и фильтрация</h3>
          <p class="text-gray-600 text-sm">Найдите нужный банк по различным критериям</p>
        </div>
      </div>

      <div class="flex justify-center space-x-4">
        <NuxtLink to="/banks" class="btn btn-primary">
          Смотреть банки
        </NuxtLink>

        <NuxtLink
          v-if="!authStore.isAuthenticated"
          to="/login"
          class="btn btn-secondary"
        >
          Войти в систему
        </NuxtLink>

        <NuxtLink
          v-if="authStore.isAuthenticated"
          to="/profile"
          class="btn btn-secondary"
        >
          Мой профиль
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()

// Инициализируем store только на клиенте
if (process.client) {
  authStore.initialize()
}
</script>
