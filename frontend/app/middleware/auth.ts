
export default defineNuxtRouteMiddleware((to) => {
  // Временно отключен для отладки
  // if (process.client) {
  //   const authStore = useAuthStore()

  //   if (!authStore.isAuthenticated && to.path !== '/login' && to.path !== '/register') {
  //     return navigateTo('/login')
  //   }
  // }
})
