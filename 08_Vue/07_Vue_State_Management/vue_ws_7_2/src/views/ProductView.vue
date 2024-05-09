<template>
  <div>
    <h2>상품 목록 페이지</h2>
    <div class="product-list">
      <ProductDetail
      v-for="product in store.productList"
      :key="product.name"
      :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { useProductListStore } from '@/stores/products.js'
import ProductDetail from '@/components/ProductDetail.vue';
const store = useProductListStore()
</script>

<style scoped>
.product-list {
  display: flex;
  flex-wrap: wrap;
}
</style>