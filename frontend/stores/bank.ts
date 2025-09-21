import { defineStore } from 'pinia'
import { useAuthStore } from './auth'

export interface Bank {
  id: number
  name: string
  short_name: string
  license_number: string
  rating: string
  is_active: boolean
  address?: string
  phone?: string
  email?: string
  website?: string
  description?: string
  foundation_year?: number
}

interface Pagination {
  current: number
  total: number
  pageSize: number
}

interface Filters {
  search: string
  minRating: number | null
  maxRating: number | null
  minYear: number | null
  maxYear: number | null
  isActive: boolean | null
}

interface Sort {
  field: string
  order: 'asc' | 'desc'
}

export const useBanksStore = defineStore('banks', {
  state: () => ({
    banks: [] as Bank[],
    currentBank: null as Bank | null,
    loading: false,
    error: null as string | null,
    pagination: {
      current: 1,
      total: 0,
      pageSize: 50,
    } as Pagination,
    filters: {
      search: '',
      minRating: null,
      maxRating: null,
      minYear: null,
      maxYear: null,
      isActive: null,
    } as Filters,
    sort: {
      field: 'name',
      order: 'asc'
    } as Sort
  }),
  
  actions: {
    async fetchBanks(params: any = {}) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const authStore = useAuthStore()
        
        const queryParams = {
          page: params.page || 1,
          search: params.search || this.filters.search,
          min_rating: params.minRating || this.filters.minRating,
          max_rating: params.maxRating || this.filters.maxRating,
          min_year: params.minYear || this.filters.minYear,
          max_year: params.maxYear || this.filters.maxYear,
          is_active: params.isActive !== undefined ? params.isActive : this.filters.isActive,
          ordering: params.ordering || (this.sort.order === 'desc' ? `-${this.sort.field}` : this.sort.field),
        }
        
        const headers: any = {
          'Content-Type': 'application/json'
        }
        
        if (authStore.token) {
          headers.Authorization = `Bearer ${authStore.token}`
        }
        
        const response = await $fetch(`${config.public.apiBase}/banks/`, { 
          query: queryParams,
          headers
        })
        
        this.banks = response.results || response
        this.pagination = {
          current: params.page || 1,
          total: response.count || response.length,
          pageSize: 20
        }
      } catch (error: any) {
        this.error = error.data?.message || 'Ошибка загрузки банков'
        console.error('Error fetching banks:', error)
      } finally {
        this.loading = false
      }
    },
    
    async fetchBank(id: string) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const authStore = useAuthStore()
        
        const headers: any = {
          'Content-Type': 'application/json'
        }
        
        if (authStore.token) {
          headers.Authorization = `Bearer ${authStore.token}`
        }
        
        const response = await $fetch(`${config.public.apiBase}/banks/${id}/`, {
          headers
        })
        this.currentBank = response
      } catch (error: any) {
        this.error = error.data?.message || 'Ошибка загрузки банка'
        console.error('Error fetching bank:', error)
      } finally {
        this.loading = false
      }
    },
    
    updateFilters(newFilters: Partial<Filters>) {
      this.filters = { ...this.filters, ...newFilters }
      this.fetchBanks({ page: 1 })
    },
    
    updateSort(field: string, order: 'asc' | 'desc') {
      this.sort = { field, order }
      this.fetchBanks()
    },
    
    clearFilters() {
      this.filters = {
        search: '',
        minRating: null,
        maxRating: null,
        minYear: null,
        maxYear: null,
        isActive: null,
      }
      this.fetchBanks({ page: 1 })
    },

    async createBank(bankData: any) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const authStore = useAuthStore()
        
        const headers: any = {
          'Content-Type': 'application/json'
        }
        
        if (authStore.token) {
          headers.Authorization = `Bearer ${authStore.token}`
        }
        
        const response = await $fetch(`${config.public.apiBase}/banks/`, {
          method: 'POST',
          body: bankData,
          headers
        })
        
        await this.fetchBanks()
        return response
      } catch (error: any) {
        this.error = error.data?.message || 'Ошибка создания банка'
        console.error('Error creating bank:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async updateBank(id: number, bankData: any) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const authStore = useAuthStore()
        
        const headers: any = {
          'Content-Type': 'application/json'
        }
        
        if (authStore.token) {
          headers.Authorization = `Bearer ${authStore.token}`
        }
        
        const response = await $fetch(`${config.public.apiBase}/banks/${id}/`, {
          method: 'PUT',
          body: bankData,
          headers
        })
        
        await this.fetchBanks()
        return response
      } catch (error: any) {
        this.error = error.data?.message || 'Ошибка обновления банка'
        console.error('Error updating bank:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async deleteBank(id: number) {
      this.loading = true
      this.error = null
      
      try {
        const config = useRuntimeConfig()
        const authStore = useAuthStore()
        
        const headers: any = {
          'Content-Type': 'application/json'
        }
        
        if (authStore.token) {
          headers.Authorization = `Bearer ${authStore.token}`
        }
        
        await $fetch(`${config.public.apiBase}/banks/${id}/`, {
          method: 'DELETE',
          headers
        })
        
        await this.fetchBanks()
      } catch (error: any) {
        this.error = error.data?.message || 'Ошибка удаления банка'
        console.error('Error deleting bank:', error)
        throw error
      } finally {
        this.loading = false
      }
    }
  }
})