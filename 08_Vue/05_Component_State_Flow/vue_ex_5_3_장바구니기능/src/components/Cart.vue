<template>
<ul>
  <li v-for="product in cart" :key="product.id">
    {{ product.name }} - {{ product.price }}원
    <button @click="deleteToCart(product)">삭제</button>
  </li>
</ul>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['deleteToCart'])
const deleteToCart = function (product) {
  emit('deleteToCart', product)
}
defineProps({
  cart: Array
})
</script>

<style scoped>

</style>