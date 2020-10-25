<template>
  <div id="app">
    <Properties/>
  </div>
</template>

<script>
import Properties from './components/Properties.vue'

export default {
  name: 'App',
  components: {
    Properties
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
