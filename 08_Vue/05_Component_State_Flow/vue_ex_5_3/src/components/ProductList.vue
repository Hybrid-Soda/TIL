<template>
  <ul>
    <ProductListItem 
      @add-to-cart="addToCart"
      v-for="product in products" 
      :key="product.id" 
      :product="product"
    />
  </ul>
</template>

<script setup>
  import ProductListItem from '@/components/ProductListItem.vue'

  const emit = defineEmits(['addToCart'])
  const addToCart = function (product) {
    emit('addToCart', product)
  }
  defineProps({
    products: Array
  })
</script>
