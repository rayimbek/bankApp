<template>
  <div>
    <div v-if="banksStore.loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
      <p class="mt-2 text-gray-600">Загрузка информации о банке...</p>
    </div>

    <div v-else-if="banksStore.error" class="text-center py-8">
      <div class="text-red-600 bg-red-50 p-4 rounded-lg">
        {{ banksStore.error }}
      </div>
      <NuxtLink to="/banks" class="btn-primary mt-4 inline-block">
        Назад к списку
      </NuxtLink>
    </div>

    <div v-else-if="banksStore.currentBank" class="card">
      <!-- Отладочная информация -->
<!--      <div class="mb-4 p-4 bg-gray-100 rounded text-xs">-->
<!--        <strong>Debug Info:</strong><br>-->
<!--        Is Authenticated: {{ authStore.isAuthenticated }}<br>-->
<!--        Token: {{ authStore.token ? 'exists' : 'null' }}<br>-->
<!--        Bank Data: {{ JSON.stringify(banksStore.currentBank, null, 2) }}-->
<!--      </div>-->
      
      <div class="flex justify-between items-start mb-6">
        <h1 class="text-3xl font-bold text-gray-900">{{ banksStore.currentBank.name }}</h1>
        <div :class="[
          'px-3 py-1 rounded-full text-sm font-semibold',
          banksStore.currentBank.is_active
            ? 'bg-green-100 text-green-800'
            : 'bg-red-100 text-red-800'
        ]">
          {{ banksStore.currentBank.is_active ? 'Активный' : 'Неактивный' }}
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <div>
          <h2 class="text-xl font-semibold mb-4 text-gray-900">Основная информация</h2>

          <div class="space-y-3">
            <div class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Номер лицензии:</span>
              <span class="text-gray-900">{{ banksStore.currentBank.license_number }}</span>
            </div>

            <div class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Рейтинг:</span>
              <span class="text-yellow-600 font-semibold">{{ banksStore.currentBank.rating }}</span>
            </div>

            <div v-if="banksStore.currentBank.foundation_year" class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Год основания:</span>
              <span class="text-gray-900">{{ banksStore.currentBank.foundation_year }}</span>
            </div>
          </div>
        </div>

        <div v-if="authStore.isAuthenticated">
          <h2 class="text-xl font-semibold mb-4 text-gray-900">Контактная информация</h2>

          <div class="space-y-3">
            <div v-if="banksStore.currentBank.address" class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Адрес:</span>
              <span class="text-gray-900 text-right">{{ banksStore.currentBank.address }}</span>
            </div>

            <div v-if="banksStore.currentBank.phone" class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Телефон:</span>
              <span class="text-gray-900">{{ banksStore.currentBank.phone }}</span>
            </div>

            <div v-if="banksStore.currentBank.email" class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Email:</span>
              <span class="text-gray-900">{{ banksStore.currentBank.email }}</span>
            </div>

            <div v-if="banksStore.currentBank.website" class="flex justify-between border-b pb-2">
              <span class="font-medium text-gray-700">Веб-сайт:</span>
              <a
                :href="banksStore.currentBank.website"
                target="_blank"
                class="text-primary-600 hover:text-primary-700"
              >
                Перейти
              </a>
            </div>
          </div>
        </div>
      </div>

      <div v-if="banksStore.currentBank.description && authStore.isAuthenticated" class="mb-6">
        <h2 class="text-xl font-semibold mb-3 text-gray-900">Описание</h2>
        <p class="text-gray-700 leading-relaxed">{{ banksStore.currentBank.description }}</p>
      </div>

      <div class="flex space-x-4">
        <NuxtLink to="/banks" class="btn-secondary">
          ← Назад к списку
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useBanksStore } from '../../../stores/bank'
import { useAuthStore } from '../../../stores/auth'

const route = useRoute()
const banksStore = useBanksStore()
const authStore = useAuthStore()

const bankId = computed(() => route.params.id as string)

onMounted(() => {
  if (process.client) {
    banksStore.fetchBank(bankId.value)
  }
})

watch(bankId, (newId) => {
  if (process.client) {
    banksStore.fetchBank(newId)
  }
})
</script>