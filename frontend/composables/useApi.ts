
export const useApi = () => {
  const { $api } = useNuxtApp()
  return $api
}

export const useAuthApi = () => {
  const config = useRuntimeConfig()
  const authStore = useAuthStore()

  const api = $fetch.create({
    baseURL: config.public.apiBase,
    headers: {
      'Content-Type': 'application/json',
    },
    onRequest({ options }) {
      if (process.client && authStore.token) {
        options.headers = options.headers || {}
        options.headers.Authorization = `Bearer ${authStore.token}`
      }
    },
    onResponseError({ error }) {
      if (error.status === 401) {
        authStore.logout()
        if (process.client) {
          navigateTo('/login')
        }
      }
    }
  })

  return api
}
