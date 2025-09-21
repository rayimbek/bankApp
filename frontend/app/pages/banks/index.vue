
<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gray-900">Список банков</h1>

      <div class="flex items-center space-x-4">
        <!-- Быстрые кнопки сортировки -->
        <div class="flex items-center space-x-2">
          <button
            @click="quickSort('rating', 'desc')"
            class="px-3 py-1 text-sm bg-yellow-100 text-yellow-800 rounded border border-yellow-300 hover:bg-yellow-200"
          >
            ⭐ Топ рейтинг
          </button>
          <button
            @click="quickSort('name', 'asc')"
            class="px-3 py-1 text-sm bg-blue-100 text-blue-800 rounded border border-blue-300 hover:bg-blue-200"
          >
            🔤 А-Я
          </button>
        </div>
        
        <div v-if="banksStore.sort.field" class="text-sm text-gray-600">
          Сортировка: {{ getSortLabel() }}
        </div>
        <div class="flex items-center space-x-2">
          <span class="text-sm text-gray-600">
            Всего: {{ banksStore.pagination.total }}
          </span>
        </div>
      </div>
    </div>

    <BankFilters />
    <BankSorting />

    <div v-if="banksStore.loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
      <p class="mt-2 text-gray-600">Загрузка банков...</p>
    </div>

    <div v-else-if="banksStore.error" class="text-center py-8">
      <div class="text-red-600 bg-red-50 p-4 rounded-lg">
        {{ banksStore.error }}
      </div>
      <button @click="banksStore.fetchBanks()" class="bg-blue-600 text-white px-4 py-2 rounded mt-4">
        Попробовать снова
      </button>
    </div>

    <div v-else-if="banksStore.banks.length === 0" class="text-center py-12">
      <div class="text-6xl mb-4">🏦</div>
      <h3 class="text-xl font-semibold text-gray-900 mb-2">Банки не найдены</h3>
      <p class="text-gray-600">Попробуйте изменить параметры поиска</p>
    </div>

    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <BankCard
          v-for="bank in banksStore.banks"
          :key="bank.id"
          :bank="bank"
        />
      </div>

      <div class="flex justify-center space-x-2">
        <button
          v-for="page in totalPages"
          :key="page"
          @click="goToPage(page)"
          :class="[
            'px-3 py-1 rounded border',
            currentPage === page
              ? 'bg-blue-600 text-white border-blue-600'
              : 'bg-white text-gray-700 border-gray-300 hover:bg-gray-50'
          ]"
        >
          {{ page }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useBanksStore } from '../../../stores/bank'
import BankFilters from '../../../components/Bank/BankFilters.vue'
import BankSorting from '../../../components/Bank/BankSorting.vue'
import BankCard from '../../../components/Bank/BankCard.vue'

const banksStore = useBanksStore()

const currentPage = computed(() => banksStore.pagination.current)
const totalPages = computed(() => Math.ceil(banksStore.pagination.total / banksStore.pagination.pageSize))

onMounted(() => {
  if (process.client) {
    banksStore.fetchBanks()
  }
})

const goToPage = (page: number) => {
  banksStore.fetchBanks({ page })
}

const quickSort = (field: string, order: 'asc' | 'desc') => {
  banksStore.updateSort(field, order)
}

const getSortLabel = () => {
  const field = banksStore.sort.field
  const order = banksStore.sort.order
  
  const fieldLabels: Record<string, string> = {
    'name': 'Название',
    'license_number': 'Лицензия',
    'rating': 'Рейтинг',
    'foundation_year': 'Год основания'
  }
  
  const orderLabels: Record<string, string> = {
    'asc': 'по возрастанию',
    'desc': 'по убыванию'
  }
  
  return `${fieldLabels[field] || field} (${orderLabels[order] || order})`
}
</script>
