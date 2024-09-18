<script setup>

const icons = [
  {
    text: 'mdi-facebook',
    link: '',
  },
  {
    text: 'mdi-twitter',
    link: '',
  },
  {
    text: 'mdi-linkedin',
    link: '',
  },
  {
    text: 'mdi-instagram',
    link: 'https://instagram.com/joabson_arley/',
  },
];

const currentYear = new Date().getFullYear();

// 导入波浪图片
import borderWavesBlue from '@/assets/img/borderWavesBlue.svg';
</script>

<template>
  <div class="footer-container">
    <!-- 波浪图片 -->
    <div class="wave-image">
      <img :src="borderWavesBlue" alt="Border Waves Blue">
    </div>

    <!-- Footer 内容 -->
    <v-footer class="footer-content">
      <v-card flat class="text-center" color="transparent">
        <v-card-text>
          <v-btn
            v-for="(icon, i) in icons"
            :key="i"
            :href="icon.link"
            target="_blank"
            variant="text"
            class="mx-4 text-white"
          >
            <v-icon size="24">{{ icon.text }}</v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="text-white pt-0">
          TO DO
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="text-white">
          {{ currentYear }} — <strong>AI 学海行</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </div>
</template>



<style scoped>
.footer-container {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.wave-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: auto;
}

.wave-image img {
  width: 100%;
  height: auto;
}


.footer-content {
  position: relative;
  z-index: 1; /* 确保内容在波浪图片之上 */
  color: white;
  padding-top: 100px; /* 根据需要调整，确保内容不被波浪图片遮挡 */
}
</style>
