<script setup>
// import LayoutNav from '@/views/layout/components/LayoutNav.vue'
// import LayoutHeader from '@/views/layout/components/LayoutHeader.vue'
// import LayoutFooter from '@/views/layout/components/LayoutFooter.vue'
// import LayoutFixed from "@/views/layout/components/LayoutFixed.vue";

// 新首页
import AboutSection from "@/views/layout/components/AboutSection.vue";
import ContactSection from "@/views/layout/components/ContactSection.vue";
import DownloadSection from "@/views/layout/components/DownloadSection.vue";
import FooterSection from "@/views/layout/components/FooterSection.vue";
import HomeSection from "@/views/layout/components/HomeSection.vue";
import NavigationSection from "@/views/layout/components/NavigationSection.vue";
// import PricingSection from "@/views/layout/components/PricingSection.vue";


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

// 定义 onScroll 方法
const onScroll = (e) => {
  if (typeof window === 'undefined') return;
  const top = window.pageYOffset || e.target.scrollTop || 0;
  fab.value = top > 60;
};

// 定义 toTop 方法
const toTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  });
};

</script>

<template>
<!--  <LayoutFixed/>-->
<!--  <LayoutNav />-->
<!--  <LayoutHeader />-->
<!--  <RouterView />-->
<!--  <LayoutFooter />-->
  <v-app>
    <!-- 1. 导航栏组件 -->
    <NavigationSection :color="color" :flat="flat" />


     <!-- 2. 主要内容区域 -->
    <v-main class="pt-0">
      <HomeSection />
      <AboutSection />
      <DownloadSection />
      <!-- <pricing /> -->
      <ContactSection />
    </v-main>

    <!-- 3. 返回顶部按钮(未完成) -->
<!--    <v-scale-transition>-->
<!--      <v-btn-->
<!--        v-if="showButton"-->
<!--        variant="fab"-->
<!--        color="secondary"-->
<!--        @click="toTop"-->
<!--        class="position-fixed bottom-4 right-4"-->
<!--      >-->
<!--        <v-icon>mdi-arrow-up</v-icon>-->
<!--      </v-btn>-->
<!--    </v-scale-transition>-->


    <!-- 4. 页脚组件(未完成) -->
<!--    <FooterSection />-->
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