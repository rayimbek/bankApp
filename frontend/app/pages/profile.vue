
<template>
  <div class="max-w-2xl mx-auto">
    <h1 class="text-2xl font-bold text-gray-900 mb-6">Мой профиль</h1>

    <div class="card">
      <div v-if="authStore.user" class="space-y-4">
        <div class="flex items-center space-x-4 mb-6">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center">
            <span class="text-2xl text-primary-600 font-semibold">
              {{ authStore.user.first_name?.[0] }}{{ authStore.user.last_name?.[0] }}
            </span>
          </div>
          <div>
            <h2 class="text-xl font-semibold">{{ authStore.fullName }}</h2>
            <p class="text-gray-600">{{ authStore.user.email }}</p>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Логин</label>
            <p class="text-gray-900">{{ authStore.user.username }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Роль</label>
            <p class="text-gray-900 capitalize">{{ authStore.user.role }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Имя</label>
            <p class="text-gray-900">{{ authStore.user.first_name || 'Не указано' }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Фамилия</label>
            <p class="text-gray-900">{{ authStore.user.last_name || 'Не указано' }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Статус</label>
            <p :class="authStore.user.is_active ? 'text-green-600' : 'text-red-600'">
              {{ authStore.user.is_active ? 'Активный' : 'Неактивный' }}
            </p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Дата регистрации</label>
            <p class="text-gray-900">{{ formatDate(authStore.user.created_at) }}</p>
          </div>
        </div>

        <div class="pt-4 border-t">
          <button @click="authStore.logout()" class="btn-secondary">
            Выйти из системы
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()

definePageMeta({
})

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>
