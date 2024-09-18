<script setup>

// 新首页
import AboutSection from "@/views/layout/components/AboutSection.vue";
import ContactSection from "@/views/layout/components/ContactSection.vue";
import DemoSection from "@/views/layout/components/DemoSection.vue";
import FooterSection from "@/views/layout/components/FooterSection.vue";
import HomeSection from "@/views/layout/components/HomeSection.vue";
import NavigationSection from "@/views/layout/components/NavigationSection.vue";


import { ref, onMounted, watch } from 'vue';

const fab = ref(null);  // 控制“返回顶部”按钮的显示状态
const color = ref('');  // 颜色
const flat = ref(null);  // 样式

// 组件挂载时执行逻辑
onMounted(() => {
  const top = window.pageYOffset || 0;
  if (top <= 60) {
    color.value = 'transparent';
    flat.value = true;
  }
});

// 监听 fab 的变化
watch(fab, (value) => {
  if (value) {
    color.value = 'secondary';
    flat.value = false;
  } else {
    color.value = 'transparent';
    flat.value = true;
  }
});

</script>

<template>
  <v-app>
    <!-- 1. 导航栏组件 -->
    <NavigationSection :color="color" :flat="flat" />

     <!-- 2. 主要内容区域 -->
    <v-main class="pt-0">
      <HomeSection />
      <AboutSection />
      <DemoSection />
      <ContactSection />
    </v-main>

    <!-- 3. 页脚组件(未完成) -->
    <!--<FooterSection />-->

  </v-app>
</template>

<style scoped>
v-main {
  background-image: url("~@/assets/img/bgMain.png");
  background-attachment: fixed;
  background-position: center;
  background-size: cover;
}
</style>