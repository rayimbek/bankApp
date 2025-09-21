import { defineStore } from 'pinia'

export interface User {
  id: number
  username: string
  email: string
  first_name: string
  last_name: string
  role: string
  is_active: boolean
  created_at: string
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as User | null,
    token: null as string | null,
    isAuthenticated: false,
  }),
  
  actions: {
    setAuth(user: User, token: string) {
      this.user = user
      this.token = token
      this.isAuthenticated = true
      if (process.client) {
        localStorage.setItem('token', token)
        localStorage.setItem('user', JSON.stringify(user))
      }
    },
    
    logout() {
      this.user = null
      this.token = null
      this.isAuthenticated = false
      if (process.client) {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
      }
    },
    
    initialize() {
      if (process.client) {
        const token = localStorage.getItem('token')
        const user = localStorage.getItem('user')
        
        console.log('Auth store initialize:', {
          token: token ? 'exists' : 'null',
          user: user ? 'exists' : 'null'
        })
        
        if (token && user) {
          try {
            this.token = token
            this.user = JSON.parse(user)
            this.isAuthenticated = true
            
            console.log('Auth store initialized:', {
              isAuthenticated: this.isAuthenticated,
              user: this.user,
              isAdmin: this.isAdmin
            })
          } catch (error) {
            console.error('Error parsing user data:', error)
            this.logout()
          }
        }
      }
    }
  },
  
  getters: {
    isAdmin: (state) => state.user?.role === 'admin' || state.user?.role === 'staff',
    isUser: (state) => state.isAuthenticated,
    fullName: (state) => state.user ? `${state.user.first_name} ${state.user.last_name}` : '',
  }
})