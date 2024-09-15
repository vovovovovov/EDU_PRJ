<!--未实现-->


<script setup>
import { getBannerAPI } from '@/apis/home'
import { onMounted, ref, reactive } from 'vue'

const bannerList = ref([])

const testBannerList = reactive([
  { id: 1, imgUrl: '@/assets/test_img/1.jpg' },
  { id: 2, imgUrl: '@/assets/test_img/2.jpg' },
  // ... 更多的轮播图项
])
bannerList.value = testBannerList


// const getBanner = async () => {
//   const res = await getBannerAPI()
//   console.log(res)
//   bannerList.value = res.data.result
// }
//
// onMounted(() => getBanner())

</script>



<template>
  <div class="home-banner">
    <el-carousel height="500px">
      <el-carousel-item v-for="item in bannerList.value" :key="item.id">
        <img :src="item.imgUrl" alt="">
        <li v-text="item.imgUrl"></li>  <!-- 添加这个li标签 -->
      </el-carousel-item>
    </el-carousel>
  </div>
</template>



<style scoped lang='scss'>
.home-banner {
  width: 1240px;
  height: 500px;
  position: absolute;
  left: 0;
  top: 0;
  z-index: 98;

  img {
    width: 100%;
    height: 500px;
  }
}
</style>