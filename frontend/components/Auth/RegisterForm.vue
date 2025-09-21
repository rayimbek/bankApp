
<template>
  <div>
    <h2 class="text-2xl font-bold text-center mb-6">Регистрация</h2>

    <form @submit.prevent="handleRegister" class="space-y-4">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Имя</label>
          <input
            v-model="form.first_name"
            type="text"
            class="input-field"
            placeholder="Ваше имя"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Фамилия</label>
          <input
            v-model="form.last_name"
            type="text"
            class="input-field"
            placeholder="Ваша фамилия"
          >
        </div>
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
        <input
          v-model="form.email"
          type="email"
          required
          class="input-field"
          placeholder="email@example.com"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Логин</label>
        <input
          v-model="form.username"
          type="text"
          required
          class="input-field"
          placeholder="Придумайте логин"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Пароль</label>
        <input
          v-model="form.password"
          type="password"
          required
          class="input-field"
          placeholder="Не менее 8 символов"
        >
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Подтверждение пароля</label>
        <input
          v-model="form.password_confirm"
          type="password"
          required
          class="input-field"
          placeholder="Повторите пароль"
        >
      </div>

      <button
        type="submit"
        :disabled="loading"
        class="btn-primary w-full"
      >
        {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
      </button>

      <div v-if="error" class="text-red-600 text-sm text-center p-2 bg-red-50 rounded">
        {{ error }}
      </div>

      <div v-if="success" class="text-green-600 text-sm text-center p-2 bg-green-50 rounded">
        Регистрация успешна! Перенаправление...
      </div>
    </form>

    <div class="mt-4 text-center">
      <NuxtLink to="/login" class="text-primary-600 hover:text-primary-700 text-sm">
        Уже есть аккаунт? Войти
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
const form = reactive({
  username: '',
  email: '',
  password: '',
  password_confirm: '',
  first_name: '',
  last_name: ''
})

const loading = ref(false)
const error = ref('')
const success = ref(false)

const handleRegister = async () => {
  if (form.password !== form.password_confirm) {
    error.value = 'Пароли не совпадают'
    return
  }

  loading.value = true
  error.value = ''

  try {
    const config = useRuntimeConfig()
    await $fetch(`${config.public.apiBase}/auth/register/`, {
      method: 'POST',
      body: form
    })

    success.value = true
    setTimeout(() => navigateTo('/login'), 2000)
  } catch (err: any) {
    error.value = err.data?.message || 'Ошибка регистрации'
  } finally {
    loading.value = false
  }
}
</script>
