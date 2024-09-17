<script setup>
import ill2Image from '@/assets/img/ill2.svg';
</script>

<template>
  <section id="demo">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <!-- 左侧图片 -->
            <v-col cols="12" sm="4" class="d-none d-sm-flex">
              <img :src="ill2Image" class="center-image" style="width: 450px;" alt=""/>
            </v-col>
            <!-- 右侧内容 -->
            <v-col cols="12" sm="8" class="text-white">
              <h1 class="demo-title">Live Demo</h1>
              <h1 class="demo-subtitle">
                AI学海行是一款基于大语言模型的智能教育平台demo，旨在为学习者提供个性化、交互式的学习体验。
                通过实时生成学习资源、提供精准的答疑和深度分析，AI学海行不仅能够适应不同的学习需求，还能帮
                助学生在学术海洋中高效地导航，找到最适合的知识路径，提升学习效果。这个平台融合了大数据、人
                工智能和教育理念，致力于为学生打造一个不断进步的智能学习助手。
              </h1>
              <router-link to="/demo">
                <v-btn
                  rounded
                  variant="outlined"
                  target="_blank"
                  size="large"
                  color="white"
                  class="mt-4"
                >
                  开始使用
                </v-btn>
              </router-link>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>



<style scoped>
#demo {
  background-image: url('@/assets/img/bgDemo.jpg');
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 500px;
}

#demo .v-container,
#demo .v-row {
  height: 100%;
}

/* 自定义样式 */
.demo-title {
  font-size: 3.75rem;
  font-weight: 200;
  margin-bottom: 1rem;
}

.demo-subtitle {
  font-size: 1.5rem;
  font-weight: 300;
}

.center-image {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.d-none {
  display: none;
}

@media (min-width: 600px) {
  .d-sm-flex {
    display: flex;
  }
}
</style>
