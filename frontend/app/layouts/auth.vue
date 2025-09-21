
<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center py-12 px-4">
    <div class="w-full max-w-md">
      <div class="text-center mb-8">
        <NuxtLink to="/" class="text-2xl font-bold text-primary-600">
          🏦 Bank App
        </NuxtLink>
      </div>

      <div class="bg-white rounded-lg shadow-md p-6">
        <slot />
      </div>
    </div>
  </div>
</template>
