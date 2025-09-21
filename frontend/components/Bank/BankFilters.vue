
<template>
  <div class="bg-white p-6 rounded-lg shadow-md mb-6">
    <h3 class="text-lg font-semibold mb-4">Фильтры и поиск</h3>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Поиск</label>
        <input
          v-model="localFilters.search"
          placeholder="Название, лицензия..."
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          @keyup.enter="applyFilters"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Рейтинг от</label>
        <input
          v-model="localFilters.minRating"
          type="number"
          min="0"
          max="5"
          step="0.1"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="0"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Рейтинг до</label>
        <input
          v-model="localFilters.maxRating"
          type="number"
          min="0"
          max="5"
          step="0.1"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="5"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Статус</label>
        <select v-model="localFilters.isActive" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
          <option :value="null">Все</option>
          <option :value="true">Активные</option>
          <option :value="false">Неактивные</option>
        </select>
      </div>
    </div>

    <div class="flex space-x-2">
      <button @click="applyFilters" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Применить
      </button>
      <button @click="clearFilters" class="bg-gray-600 text-white px-4 py-2 rounded hover:bg-gray-700">
        Сбросить
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useBanksStore } from '../../stores/bank'

const banksStore = useBanksStore()

const localFilters = reactive({
  search: banksStore.filters.search,
  minRating: banksStore.filters.minRating,
  maxRating: banksStore.filters.maxRating,
  isActive: banksStore.filters.isActive
})

const applyFilters = () => {
  banksStore.updateFilters({ ...localFilters })
}

const clearFilters = () => {
  localFilters.search = ''
  localFilters.minRating = null
  localFilters.maxRating = null
  localFilters.isActive = null
  banksStore.clearFilters()
}

watch(() => banksStore.filters, (newFilters) => {
  localFilters.search = newFilters.search
  localFilters.minRating = newFilters.minRating
  localFilters.maxRating = newFilters.maxRating
  localFilters.isActive = newFilters.isActive
})
</script>
