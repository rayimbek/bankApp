<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-gray-900">Управление банками</h1>
      <div class="flex items-center space-x-4">
        <div class="flex items-center space-x-2">
          <label class="text-sm text-gray-600">Банков на странице:</label>
          <select v-model="pageSize" @change="changePageSize" class="input-field w-20">
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="100">100</option>
          </select>
        </div>
        <button @click="showCreateForm = true" class="btn-primary">
          <span class="mr-2">+</span>
          Добавить банк
        </button>
      </div>
    </div>

    <!-- Таблица банков -->
    <div class="card">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                <button @click="sortBy('name')" class="flex items-center space-x-1 hover:text-gray-700">
                  <span>Название</span>
                  <span v-if="sortField === 'name'" class="text-blue-600">
                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                  </span>
                </button>
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                <button @click="sortBy('license_number')" class="flex items-center space-x-1 hover:text-gray-700">
                  <span>Лицензия</span>
                  <span v-if="sortField === 'license_number'" class="text-blue-600">
                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                  </span>
                </button>
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                <button @click="sortBy('rating')" class="flex items-center space-x-1 hover:text-gray-700">
                  <span>Рейтинг</span>
                  <span v-if="sortField === 'rating'" class="text-blue-600">
                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                  </span>
                </button>
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                <button @click="sortBy('is_active')" class="flex items-center space-x-1 hover:text-gray-700">
                  <span>Статус</span>
                  <span v-if="sortField === 'is_active'" class="text-blue-600">
                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                  </span>
                </button>
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Действия
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="bank in banks" :key="bank.id" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm font-medium text-gray-900">{{ bank.name }}</div>
                <div class="text-sm text-gray-500">{{ bank.short_name }}</div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                {{ bank.license_number }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                      :class="getRatingClass(bank.rating)">
                  {{ bank.rating }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="inline-flex px-2 py-1 text-xs font-semibold rounded-full"
                      :class="bank.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'">
                  {{ bank.is_active ? 'Активен' : 'Неактивен' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button @click="editBank(bank)" class="text-indigo-600 hover:text-indigo-900 mr-3">
                  Редактировать
                </button>
                <button @click="deleteBank(bank)" class="text-red-600 hover:text-red-900">
                  Удалить
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <!-- Информация о пагинации -->
      <div class="px-6 py-3 bg-gray-50 border-t border-gray-200">
        <div class="flex justify-between items-center">
          <div class="text-sm text-gray-700">
            Показано {{ banks.length }} из {{ banksStore.pagination.total }} банков
          </div>
          <div class="text-sm text-gray-500">
            Страница {{ banksStore.pagination.current }} из {{ Math.ceil(banksStore.pagination.total / banksStore.pagination.pageSize) }}
          </div>
        </div>
      </div>
    </div>

    <!-- Модальное окно для создания/редактирования -->
    <div v-if="showCreateForm || showEditForm" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-11/12 md:w-2/3 lg:w-1/2 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <h3 class="text-lg font-medium text-gray-900 mb-4">
            {{ showCreateForm ? 'Добавить банк' : 'Редактировать банк' }}
          </h3>
          
          <BankForm 
            :bank="editingBank"
            :is-edit="showEditForm"
            @save="handleSave"
            @cancel="handleCancel"
          />
        </div>
      </div>
    </div>

    <!-- Модальное окно подтверждения удаления -->
    <div v-if="showDeleteConfirm" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
        <div class="mt-3">
          <h3 class="text-lg font-medium text-gray-900 mb-4">Подтверждение удаления</h3>
          <p class="text-sm text-gray-500 mb-6">
            Вы уверены, что хотите удалить банк "{{ deletingBank?.name }}"? Это действие нельзя отменить.
          </p>
          <div class="flex justify-end space-x-3">
            <button @click="showDeleteConfirm = false" class="btn-secondary">
              Отмена
            </button>
            <button @click="confirmDelete" class="btn-danger">
              Удалить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useBanksStore } from '../../../stores/bank'
import BankForm from '../../../components/Admin/BankForm.vue'

const banksStore = useBanksStore()

const banks = ref([])
const showCreateForm = ref(false)
const showEditForm = ref(false)
const showDeleteConfirm = ref(false)
const editingBank = ref(null)
const deletingBank = ref(null)
const pageSize = ref(50)
const sortField = ref('name')
const sortOrder = ref('asc')

const loadBanks = async () => {
  try {
    await banksStore.fetchBanks()
    banks.value = banksStore.banks
  } catch (error) {
    console.error('Ошибка загрузки банков:', error)
  }
}

const getRatingClass = (rating: number) => {
  if (rating >= 4) return 'bg-green-100 text-green-800'
  if (rating >= 3) return 'bg-yellow-100 text-yellow-800'
  return 'bg-red-100 text-red-800'
}

const editBank = (bank: any) => {
  editingBank.value = { ...bank }
  showEditForm.value = true
}

const deleteBank = (bank: any) => {
  deletingBank.value = bank
  showDeleteConfirm.value = true
}

const confirmDelete = async () => {
  if (!deletingBank.value) return
  
  try {
    await banksStore.deleteBank(deletingBank.value.id)
    await loadBanks()
    showDeleteConfirm.value = false
    deletingBank.value = null
  } catch (error) {
    console.error('Ошибка удаления банка:', error)
  }
}

const handleSave = async (bankData: any) => {
  try {
    if (showEditForm.value) {
      await banksStore.updateBank(editingBank.value.id, bankData)
    } else {
      await banksStore.createBank(bankData)
    }
    await loadBanks()
    handleCancel()
  } catch (error) {
    console.error('Ошибка сохранения банка:', error)
  }
}

const handleCancel = () => {
  showCreateForm.value = false
  showEditForm.value = false
  editingBank.value = null
}

const changePageSize = async () => {
  banksStore.pagination.pageSize = pageSize.value
  await loadBanks()
}

const sortBy = async (field: string) => {
  if (sortField.value === field) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortField.value = field
    sortOrder.value = 'asc'
  }
  
  banksStore.updateSort(field, sortOrder.value)
  await loadBanks()
}

onMounted(() => {
  loadBanks()
})
</script>
