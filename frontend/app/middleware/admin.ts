
export default defineNuxtRouteMiddleware((to) => {
  // Временно отключен для отладки
  // if (process.client) {
  //   const authStore = useAuthStore()

  //   if (!authStore.isAuthenticated) {
  //     return navigateTo('/login')
  //   }

  //   if (!authStore.isAdmin) {
  //     return navigateTo('/')
  //   }
  // }
})
