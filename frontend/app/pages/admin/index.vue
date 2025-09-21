
<template>
  <div>
    <h1 class="text-2xl font-bold text-gray-900 mb-6">Административная панель</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <div class="card text-center">
        <div class="text-4xl mb-4">🏦</div>
        <h3 class="text-xl font-semibold mb-2">Управление банками</h3>
        <p class="text-gray-600 mb-4">Добавление, редактирование и удаление банков</p>
        <NuxtLink to="/admin/banks" class="btn-primary">
          Перейти
        </NuxtLink>
      </div>

      <div class="card text-center">
        <div class="text-4xl mb-4">👥</div>
        <h3 class="text-xl font-semibold mb-2">Управление пользователями</h3>
        <p class="text-gray-600 mb-4">Просмотр и управление пользователями системы</p>
        <a href="http://localhost:8000/admin/" target="_blank" class="btn-primary">
          Перейти в админку
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
