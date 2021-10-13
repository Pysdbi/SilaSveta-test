<template>
  <div
    class="value"
    v-text="paramValue"
  />
</template>

<script>
export default {
  name: 'ValueQueryParam',
  props: {
    paramName: {
      type: String,
      required: true
    }
  },

  computed: {
    paramValue () {
      return this.$route.query[this.paramName] || 'Ничего не найдено'
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
