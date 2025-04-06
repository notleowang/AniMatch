<script>
export default {
  data() {
    return {
      text: ''
    }
  },
  methods: {
    onStartNowClick() {
      this.text = "Going to Home Page"
    },
    onAniListClick() {
      this.text = "Logged in with AniList"
    },
    onMalClick() {
      this.text = "Logged in with MAL"
    }
  }
}
</script>

<template>
  <h1>AniMatch</h1>
  <button @click="onStartNowClick">Start Now</button>
  <button @click="onAniListClick">Connect with AniList</button>
  <button @click="onMalClick">Connect with MAL</button>
  <p>{{ text }}</p>
</template>

<style>

</style>
