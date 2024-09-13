<script setup>

import LayoutNav from '@/layout/components/LayoutNav.vue'
import LayoutHeader from '@/layout/components/LayoutHeader.vue'
import LayoutFooter from '@/layout/components/LayoutFooter.vue'

</script>

<template>


<!--  主页面整体布局-->
  <LayoutNav />
  <LayoutHeader />
  <LayoutFooter />


</template>






<style scoped lang="scss">


header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
