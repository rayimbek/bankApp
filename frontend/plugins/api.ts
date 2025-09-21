
export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()

  const api = $fetch.create({
    baseURL: config.public.apiBase,
    headers: {
      'Content-Type': 'application/json',
    },
    onRequest({ options }) {
    },
    onRequestError({ error }) {
      console.error('API Request Error:', error)
    },
    onResponseError({ error }) {
      console.error('API Response Error:', error)
    }
  })

  return {
    provide: {
      api
    }
  }
})
