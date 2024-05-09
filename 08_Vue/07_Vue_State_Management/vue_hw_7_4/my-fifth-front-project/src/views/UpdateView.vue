<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름: {{ balance.name }}</p>
    <p>잔고: {{ balance.balance }}</p>
    <button @click="store.addBalance(balance)">+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const store = useBalanceStore()
const name = ref(route.params.name)
const balance = ref(store.returnInfo(name.value))
</script>