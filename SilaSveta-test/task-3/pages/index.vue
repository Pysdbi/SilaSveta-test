<template>
  <div class="app">
    <div id="id_toChange">
      Текст
    </div>
    <button @click="toChange">
      Изменить
    </button>
  </div>
</template>

<script>
const Img = {
  src: 'https://i.pinimg.com/originals/e1/92/62/e1926225f3613de044c897241e60d47e.jpg',
  width: 400
}

export default {
  methods: {
    toChange () {
      const img = `<img src="${Img.src}" width="${Img.width}" alt="">`
      $('#id_toChange').html(img)
    }
  }
}
</script>

<style lang="scss">
.app {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 2rem;

  #id_toChange{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 200px;
  }

  button {
    font-size: 1.5rem;
    min-width: 320px;
    background: #b4e7fd;
  }
}
</style>
