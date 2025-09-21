<template>
  <div class="bg-white p-4 rounded-lg shadow-sm border mb-6">
    <h3 class="text-lg font-semibold text-gray-900 mb-4">Сортировка</h3>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Сортировка по названию -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Название</label>
        <div class="flex space-x-1">
          <button
            @click="sortBy('name', 'asc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('name', 'asc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            А-Я
          </button>
          <button
            @click="sortBy('name', 'desc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('name', 'desc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            Я-А
          </button>
        </div>
      </div>

      <!-- Сортировка по лицензии -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Лицензия</label>
        <div class="flex space-x-1">
          <button
            @click="sortBy('license_number', 'asc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('license_number', 'asc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            ↑
          </button>
          <button
            @click="sortBy('license_number', 'desc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('license_number', 'desc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            ↓
          </button>
        </div>
      </div>

      <!-- Сортировка по рейтингу -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Рейтинг</label>
        <div class="flex space-x-1">
          <button
            @click="sortBy('rating', 'desc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('rating', 'desc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            Высокий
          </button>
          <button
            @click="sortBy('rating', 'asc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('rating', 'asc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            Низкий
          </button>
        </div>
      </div>

      <!-- Сортировка по году основания -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Год основания</label>
        <div class="flex space-x-1">
          <button
            @click="sortBy('foundation_year', 'desc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('foundation_year', 'desc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            Новые
          </button>
          <button
            @click="sortBy('foundation_year', 'asc')"
            :class="[
              'px-3 py-1 text-sm rounded border',
              isActive('foundation_year', 'asc') 
                ? 'bg-blue-600 text-white border-blue-600' 
                : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
            ]"
          >
            Старые
          </button>
        </div>
      </div>
    </div>

    <!-- Сброс сортировки -->
    <div class="mt-4 pt-4 border-t">
      <button
        @click="clearSort"
        class="px-4 py-2 text-sm bg-gray-100 text-gray-700 rounded border hover:bg-gray-200 transition-colors"
      >
        Сбросить сортировку
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useBanksStore } from '../../stores/bank'

const banksStore = useBanksStore()

const sortBy = (field: string, order: 'asc' | 'desc') => {
  banksStore.updateSort(field, order)
}

const isActive = (field: string, order: 'asc' | 'desc') => {
  return banksStore.sort.field === field && banksStore.sort.order === order
}

const clearSort = () => {
  banksStore.updateSort('name', 'asc')
}
</script>
