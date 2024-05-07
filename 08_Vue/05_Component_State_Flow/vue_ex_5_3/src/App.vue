<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList
      @add-to-cart="addToCart"
      :products="products"
    />

    <p>총 가격: {{ totalCost }}</p>
    <h2>장바구니</h2>
    <Cart
      @delete-to-cart="deleteToCart"
      :cart="cart"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])
const cart = ref([])
const totalCost = ref(0)

const addToCart = function (product) {
  cart.value.push(product)
  totalCost.value += product.price
}

const deleteToCart = function (product) {
  const index = cart.value.findIndex(item => item.id === product.id)
  if (index !== -1) {
    cart.value.splice(index, 1)
    totalCost.value -= product.price
  }
}
</script>
