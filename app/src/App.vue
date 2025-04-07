<script setup>
</script>

<template>
  <p> Current Route Path: {{ $route.fullPath }} </p>
  <RouterLink to="/">Back to Landing</RouterLink>
  <RouterView />
</template>
