

<template>
  <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
    <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ bank.name }}</h3>

    <div class="space-y-2 mb-4">
      <p class="text-gray-600">
        <span class="font-medium">Лицензия:</span> {{ bank.license_number }}
      </p>
      <p class="text-gray-600">
        <span class="font-medium">Рейтинг:</span>
        <span class="text-yellow-600 font-semibold">{{ bank.rating }}</span>
      </p>
      <p class="text-gray-600">
        <span class="font-medium">Статус:</span>
        <span :class="bank.is_active ? 'text-green-600' : 'text-red-600'">
          {{ bank.is_active ? 'Активный' : 'Неактивный' }}
        </span>
      </p>
    </div>

    <NuxtLink
      :to="`/banks/${bank.id}`"
      class="bg-blue-600 text-white w-full text-center block py-2 rounded-md hover:bg-blue-700"
    >
      Подробнее
    </NuxtLink>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  bank: any
}>()
</script>
