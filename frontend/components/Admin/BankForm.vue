<template>
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Название банка *
        </label>
        <input
          v-model="formData.name"
          type="text"
          required
          class="input-field"
          placeholder="Введите название банка"
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Краткое название *
        </label>
        <input
          v-model="formData.short_name"
          type="text"
          required
          class="input-field"
          placeholder="Введите краткое название"
        />
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Номер лицензии *
        </label>
        <input
          v-model="formData.license_number"
          type="text"
          required
          class="input-field"
          placeholder="Введите номер лицензии"
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Рейтинг *
        </label>
        <select v-model="formData.rating" required class="input-field">
          <option value="">Выберите рейтинг</option>
          <option value="1">1 - Очень низкий</option>
          <option value="2">2 - Низкий</option>
          <option value="3">3 - Средний</option>
          <option value="4">4 - Высокий</option>
          <option value="5">5 - Очень высокий</option>
        </select>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Год основания
        </label>
        <input
          v-model="formData.foundation_year"
          type="number"
          min="1800"
          :max="new Date().getFullYear()"
          class="input-field"
          placeholder="Год основания"
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Статус
        </label>
        <select v-model="formData.is_active" class="input-field">
          <option :value="true">Активен</option>
          <option :value="false">Неактивен</option>
        </select>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Адрес
        </label>
        <textarea
          v-model="formData.address"
          rows="3"
          class="input-field"
          placeholder="Введите адрес банка"
        ></textarea>
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Телефон
        </label>
        <input
          v-model="formData.phone"
          type="tel"
          class="input-field"
          placeholder="Введите телефон"
        />
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Email
        </label>
        <input
          v-model="formData.email"
          type="email"
          class="input-field"
          placeholder="Введите email"
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">
          Веб-сайт
        </label>
        <input
          v-model="formData.website"
          type="url"
          class="input-field"
          placeholder="Введите URL веб-сайта"
        />
      </div>
    </div>

    <div>
      <label class="block text-sm font-medium text-gray-700 mb-2">
        Описание
      </label>
      <textarea
        v-model="formData.description"
        rows="4"
        class="input-field"
        placeholder="Введите описание банка"
      ></textarea>
    </div>

    <div class="flex justify-end space-x-3 pt-6 border-t">
      <button type="button" @click="$emit('cancel')" class="btn-secondary">
        Отмена
      </button>
      <button type="submit" class="btn-primary" :disabled="isSubmitting">
        {{ isSubmitting ? 'Сохранение...' : (isEdit ? 'Обновить' : 'Создать') }}
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref, reactive, watch } from 'vue'

interface BankFormData {
  name: string
  short_name: string
  license_number: string
  rating: number | string
  foundation_year: number | string
  is_active: boolean
  address: string
  phone: string
  email: string
  website: string
  description: string
}

interface Props {
  bank?: BankFormData | null
  isEdit?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  bank: null,
  isEdit: false
})

const emit = defineEmits<{
  save: [data: BankFormData]
  cancel: []
}>()

const isSubmitting = ref(false)

const formData = reactive<BankFormData>({
  name: '',
  short_name: '',
  license_number: '',
  rating: '',
  foundation_year: '',
  is_active: true,
  address: '',
  phone: '',
  email: '',
  website: '',
  description: ''
})

watch(() => props.bank, (newBank) => {
  if (newBank) {
    Object.assign(formData, {
      name: newBank.name || '',
      short_name: newBank.short_name || '',
      license_number: newBank.license_number || '',
      rating: newBank.rating || '',
      foundation_year: newBank.foundation_year || '',
      is_active: newBank.is_active !== undefined ? newBank.is_active : true,
      address: newBank.address || '',
      phone: newBank.phone || '',
      email: newBank.email || '',
      website: newBank.website || '',
      description: newBank.description || ''
    })
  }
}, { immediate: true })

const handleSubmit = async () => {
  isSubmitting.value = true
  
  try {
    if (!formData.name || !formData.short_name || !formData.license_number || !formData.rating) {
      alert('Пожалуйста, заполните все обязательные поля')
      return
    }

    const submitData = {
      ...formData,
      rating: Number(formData.rating),
      foundation_year: formData.foundation_year ? Number(formData.foundation_year) : null
    }

    emit('save', submitData)
  } catch (error) {
    console.error('Ошибка валидации формы:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>
