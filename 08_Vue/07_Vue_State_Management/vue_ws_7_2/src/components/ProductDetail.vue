<template>
  <div class="card">
    <h3>{{ product.name }}</h3>
    <img :src="product.imagePath" alt="product.name" width="300">
    <p class="product-price">₩ {{ product.price }}</p>
    <p v-if="product.isFavorite" class="favorite-icon" role="img" style="color:red">❤</p>
    <p v-else class="favorite-icon" role="img">🤍</p>
  </div>
</template>

<script setup>
defineProps({
  product: Object
})
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 20px;
  margin: 10px;
  text-align: center;
  width: 300px;
}
.product-price {
  font-size: 18px;
  margin-bottom: 10px;
}

.favorite-icon {
  cursor: pointer;
  font-size: 24px;
  margin-top: 10px;
}
</style>