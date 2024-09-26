<script setup>
import { ref, reactive } from 'vue';

// 导入图片资源，确保路径正确
import borderWavesBlue from '@/assets/img/borderWavesBlue.svg';

</script>

<template>
  <section class="pb-8" id="contact">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row justify="center">
            <!-- 左侧联系信息 -->
            <v-col cols="12" sm="5">
              <h1 class="contact-title">联系我们</h1>
              <h3 class="contact-text mt-3">
                感谢您访问我们的网站！如果您对我们的产品或服务有任何疑问，或想进一步了解我们的项目，
                请随时与我们联系.
              </h3>
              <h3 class="contact-text mt-3">
                您可以通过以下联系方式与我们取得联系:
              </h3>
              <h3 class="contact-text mt-3">
                Phone: +xx (xx) xxxxx-xxxx
              </h3>
              <h3 class="contact-text">
                Email: email@email.com
              </h3>
              <h3 class="contact-text">
                Github: https://github.com/vovovovovov/EDU_PRJ
              </h3>
            </v-col>
            <!-- 右侧图片 -->
            <v-col cols="12" sm="7">
              <img src="@/assets/img/contact.svg" alt="描述" style="width: 100%; height: 400px; display: block; text-align: center;">
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <!--底部波浪-->
    <div class="svg-border-waves">
      <img :src="borderWavesBlue" alt="Border Waves Blue">
    </div>

  </section>
</template>

<style scoped>
#contact {
  background-color: #f4f7f5;
}

.svg-border-waves img {
  //position: absolute;
  bottom: 0;
  left: 0;
  height: 3rem;
  width: 100%;
  overflow: hidden;
}

/* 自定义样式 */
.contact-title {
  font-size: 3rem;
  font-weight: 300;
}

.contact-text {
  font-size: 1.25rem;
  font-weight: 300;
  margin-top: 1rem;
}

.mt-3 {
  margin-top: 1rem;
}
</style>