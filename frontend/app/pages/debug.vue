    <template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold text-blue-600 mb-8">Debug Page</h1>
      
      <div class="bg-white p-6 rounded-lg shadow-md mb-6">
        <h2 class="text-xl font-semibold mb-4">Environment Info</h2>
        <div class="space-y-2">
          <p><strong>Client:</strong> {{ isClient }}</p>
          <p><strong>Server:</strong> {{ isServer }}</p>
          <p><strong>API Base:</strong> {{ apiBase }}</p>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md mb-6">
        <h2 class="text-xl font-semibold mb-4">Auth Store</h2>
        <div class="space-y-2">
          <p><strong>Is Authenticated:</strong> {{ authStore.isAuthenticated }}</p>
          <p><strong>User:</strong> {{ authStore.user ? authStore.user.username : 'null' }}</p>
          <p><strong>Token:</strong> {{ authStore.token ? 'exists' : 'null' }}</p>
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md mb-6">
        <h2 class="text-xl font-semibold mb-4">API Test</h2>
        <button 
          @click="testApi" 
          :disabled="loading"
          class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
        >
          {{ loading ? 'Testing...' : 'Test API Connection' }}
        </button>
        <div v-if="apiResult" class="mt-4 p-4 bg-gray-100 rounded">
          <pre>{{ JSON.stringify(apiResult, null, 2) }}</pre>
        </div>
        <div v-if="apiError" class="mt-4 p-4 bg-red-100 text-red-700 rounded">
          {{ apiError }}
        </div>
      </div>

      <div class="bg-white p-6 rounded-lg shadow-md">
        <h2 class="text-xl font-semibold mb-4">Console Logs</h2>
        <div class="space-y-2">
          <p>Check browser console for any errors</p>
          <button 
            @click="logTest" 
            class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
          >
            Log Test Message
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '../../stores/auth'

const authStore = useAuthStore()
const config = useRuntimeConfig()

const isClient = process.client
const isServer = process.server
const apiBase = config.public.apiBase

const loading = ref(false)
const apiResult = ref(null)
const apiError = ref('')

const testApi = async () => {
  loading.value = true
  apiError.value = ''
  apiResult.value = null

  try {
    const config = useRuntimeConfig()
    const response = await $fetch(`${config.public.apiBase}/banks/`)
    apiResult.value = response
  } catch (error: any) {
    apiError.value = error.message || 'API Error'
    console.error('API Test Error:', error)
  } finally {
    loading.value = false
  }
}

const logTest = () => {
  console.log('Test log message from debug page')
  console.log('Auth store:', authStore)
  console.log('Config:', config)
}
</script>
