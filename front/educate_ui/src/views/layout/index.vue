<script setup>
import LayoutNav from '@/views/layout/components/LayoutNav.vue'
import LayoutHeader from '@/views/layout/components/LayoutHeader.vue'
import LayoutFooter from '@/views/layout/components/LayoutFooter.vue'
import LayoutFixed from "@/views/layout/components/LayoutFixed.vue";
</script>

<template>
  <LayoutFixed/>
  <LayoutNav />
  <LayoutHeader />
  <RouterView />
  <LayoutFooter />
</template>

<style scoped>

</style>