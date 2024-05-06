<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ childrenProp.name }}</p>
    <p>나이 : {{ childrenProp.age }}</p>
    <p>용돈 : {{ childrenProp.balance }}</p>
    <button @click="giveMeAllowance(childrenProp)">용돈 주세요.</button>
  </div>
</template>

<script setup>
  const emit = defineEmits(['giveMeAllowance'])
  const giveMeAllowance = function (children) {
    emit('giveMeAllowance', children)
  }

  defineProps({
    childrenProp: Object
  })
</script>

<style scoped>
</style>