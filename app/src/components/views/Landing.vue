<script>
export default {
  data() {
    return {
      response: ''
    }
  },
  methods: {

  }
}
</script>

<template>
  <div class="flex justify-center">
    <div class="flex flex-col gap-6 text-center w-1/2 p-10">
      <h1 class="text-4xl">AniMatch</h1>
      <div class="flex flex-col gap-2 text-lg items-center">
        <RouterLink to="/home" class="rounded-lg bg-gray-500 w-56 py-2">Start Now</RouterLink>
        <RouterLink :to="{ name: 'authentication', params: { type: 'anilist' } }" class="rounded-lg bg-gray-500 w-56 py-2">Connect with AniList</RouterLink>
        <RouterLink :to="{ name: 'authentication', params: { type: 'mal' } }" class="rounded-lg bg-gray-500 w-56 py-2">Connect with MAL</RouterLink>
      </div>
    </div>
  </div>
</template>