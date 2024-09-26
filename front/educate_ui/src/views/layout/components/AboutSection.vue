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
                AI学海行 is all you need!
              </h1>
              <v-row>
                <!-- 第一段内容 -->
                <v-col cols="12" class="flex-center">
                  <img :src="icon1" alt="Icon 1" style="width: 60px; margin-right: 16px;" />

                  <p class="text-justify">
                    宏观把握学习路线，跨学科学习，确定人生发展方向。由于大语言模型掌握广泛的知识领域，
                    它们能够帮助学生建立不同学科之间的联系，促进跨学科思维和学习，从而找到属于自己热爱的方向。
                  </p>
                </v-col>
                <!-- 第二段内容 -->
                <v-col cols="12" class="flex-center">
                  <img :src="icon2" alt="Icon 1" style="width: 60px; margin-right: 16px;" />
                  <p class="text-justify">
                    实时扩展的优质教育资源。与传统的教育资源（如教科书和实验材料）不同，
                    大语言模型提供的是几乎无限的、实时更新的信息资源，这可以帮助学生接触到最前沿和最经典的学术和实践知识
                  </p>
                </v-col>
                <!-- 第三段内容 -->
                <v-col cols="12" class="flex-center">
                  <img :src="icon3" alt="Icon 1" style="width: 60px; margin-right: 16px;" />
                  <p class="text-justify">
                    个性化教育。大语言模型可以根据学生的学习速度、兴趣和需求提供个性化的教学内容和反馈，
                    从而为每位学生量身定制学习路径。这种个性化可以帮助学生更有效地掌握知识。
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
