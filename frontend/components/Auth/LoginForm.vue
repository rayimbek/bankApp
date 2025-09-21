
<template>
  <div>
    <h2 class="text-2xl font-bold text-center mb-6">Вход в систему</h2>

    <form @submit.prevent="handleLogin" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Логин</label>
        <input
          v-model="form.username"
          type="text"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Введите ваш логин"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Пароль</label>
        <input
          v-model="form.password"
          type="password"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Введите ваш пароль"
        >
      </div>

      <button
        type="submit"
        :disabled="loading"
        class="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 disabled:opacity-50"
      >
        {{ loading ? 'Вход...' : 'Войти' }}
      </button>

      <div v-if="error" class="text-red-600 text-sm text-center p-2 bg-red-50 rounded">
        {{ error }}
      </div>
    </form>

    <div class="mt-4 text-center">
      <NuxtLink to="/register" class="text-blue-600 hover:text-blue-700 text-sm">
        Нет аккаунта? Зарегистрироваться
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()

const form = reactive({
  username: '',
  password: ''
})

const loading = ref(false)
const error = ref('')

const handleLogin = async () => {
  loading.value = true
  error.value = ''

  try {
    const config = useRuntimeConfig()
    const response = await $fetch(`${config.public.apiBase}/auth/login/`, {
      method: 'POST',
      body: form
    })

    authStore.setAuth(response.user, response.access)
    navigateTo('/banks')
  } catch (err: any) {
    error.value = err.data?.error || 'Ошибка входа. Проверьте логин и пароль.'
  } finally {
    loading.value = false
  }
}
</script>
