<script setup>
// 直接在 setup 中调用跳转逻辑
onMounted(() => {
  window.location.href = 'https://zh.wikipedia.org/wiki/Java\''; // 页面加载后跳转
});
</script>

<template>
  <div>
    <h1>跳转中...</h1>
    <!-- 你可以在这里展示一些跳转提示，或者加载动画 -->
  </div>
</template>

<style scoped>
h1 {
  text-align: center;
  margin-top: 20%;
  font-size: 24px;
  color: #42b983;
}
</style>
