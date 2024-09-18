<script setup>
import { ref } from 'vue';

// 导入图片资源
import icon1 from '@/assets/img/icon1.svg?url';
import icon2 from '@/assets/img/icon2.svg';
import icon3 from '@/assets/img/icon3.svg';
import ill1 from '@/assets/img/ill1.svg';
</script>

<template>
  <section id="about">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col cols="12" md="7">
              <!-- 更新标题样式 -->
              <h1 class="about-title">About</h1>
              <h1 class="about-subtitle">
                Lorem ipsum dolor!
              </h1>
              <v-row>
                <!-- 第一段内容 -->
                <v-col cols="12" class="flex-center">
                  <img :src="icon1" alt="Icon 1" style="width: 60px; margin-right: 16px;" />

                  <p class="text-justify">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                  </p>
                </v-col>
                <!-- 第二段内容 -->
                <v-col cols="12" class="flex-center">
                  <img :src="icon2" alt="Icon 1" style="width: 60px; margin-right: 16px;" />
                  <p class="text-justify">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                  </p>
                </v-col>
                <!-- 第三段内容 -->
                <v-col cols="12" class="flex-center">
                  <img :src="icon3" alt="Icon 1" style="width: 60px; margin-right: 16px;" />
                  <p class="text-justify">
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                    Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                  </p>
                </v-col>
              </v-row>
            </v-col>
            <!-- 右侧图片 -->
            <v-col cols="12" md="5" class="d-none d-md-block">
              <img :src="ill1" alt="ill1" style="width: 400px; margin-right: 16px;" class="center-block"/>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<style scoped>
#about {
  background-color: #f4f7f5;
}

/* 自定义标题样式 */
.about-title {
  font-weight: 300;
  font-size: 3.75rem;
}

.about-subtitle {
  font-weight: 300;
  font-size: 3rem;
  margin-bottom: 1rem;
}

/* Flex 布局和居中对齐 */
.flex-center {
  display: flex;
  align-items: center;
}

/* 文本两端对齐 */
.text-justify {
  text-align: justify;
}

/* 图片居中 */
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

/* 响应式显示控制 */
.d-none {
  display: none;
}

@media (min-width: 960px) {
  .d-md-block {
    display: block;
  }
}
</style>
