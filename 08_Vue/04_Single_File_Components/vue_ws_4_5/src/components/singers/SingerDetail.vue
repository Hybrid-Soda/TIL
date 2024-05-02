<template>
<div class="card">
  <h1>가수 이름</h1>
  <img src="@/assets/singer.jpg" alt="singer">
  <p>가수 소개글</p>
  <div>
    <SingerAlbum />
    <SingerAlbum />
  </div>
</div>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue';
</script>

<style scoped>
img {
  width: 200px;
  border-radius: 100px;
}

.card {
  text-align: center;
  border: 1px solid black;
  padding: 20px 0;
}

.album-title {
  display: inline-block;
  border: 1px solid rgb(231, 231, 231);
  box-shadow: 2px 2px 2px rgb(187, 187, 187);
  background-color: whitesmoke;
  border-radius: 8px;
  padding: 5px;
  margin-inline: 10px;
}

</style>