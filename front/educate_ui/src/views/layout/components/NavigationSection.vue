<script setup>
import { ref, watch } from 'vue';
import { useDisplay } from 'vuetify';

// 接收 props
const props = defineProps({
  color: {
    type: String,
    default: 'grey darken-3', // 默认颜色
  },
  flat: {
    type: Boolean,
    default: false,
  },
});

// 定义响应式变量
const drawer = ref(false);

// 获取屏幕尺寸信息
const { xs } = useDisplay();

// 监听 xs 变化
const isXs = ref(xs.value);

watch(xs, (value) => {
  isXs.value = value;
  if (!value && drawer.value) {
    drawer.value = false;
  }
});

// 定义滚动方法
const scrollToSection = (sectionId) => {
  const section = document.querySelector(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
    drawer.value = false; // 关闭抽屉
  }
};
</script>

<template>
  <div>
    <!-- 导航抽屉（侧边栏） -->
    <v-navigation-drawer
      v-model="drawer"
      app
      temporary
      dark
      class="drawer-bg"
    >
      <!-- 分隔线 -->
      <v-divider />

      <!-- 导航菜单项 -->
      <v-list dense>
        <v-list-item
          v-for="(item, index) in navItems"
          :key="index"
          @click="scrollToSection(item.link)"
        >
          <v-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-icon>
          <v-list-item-title>{{ item.text }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 应用栏（顶部导航栏） -->
    <v-app-bar
      app
      :color="props.color"
      :flat="props.flat"
      class="px-4"
    >
      <v-spacer />

      <!-- 小屏幕下的导航按钮 -->
      <v-app-bar-nav-icon
        @click.stop="drawer = !drawer"
        v-if="isXs"
        class="mr-4"
      />

      <!-- 右上角导航菜单 -->
      <div v-else class="d-flex align-center">
        <v-btn
            text=""
          class="white--text mx-2"
          @click="scrollToSection('#hero')"
        >
          Home
        </v-btn>
        <v-btn
            text=""
          class="white--text mx-2"
          @click="scrollToSection('#features')"
        >
          Features
        </v-btn>
        <v-btn
            text=""
          class="white--text mx-2"
          @click="scrollToSection('#demo')"
        >
          Demo
        </v-btn>
        <v-btn
            text=""
          class="white--text mx-2"
          @click="scrollToSection('#pricing')"
        >
          About
        </v-btn>
        <v-btn
          outlined
          rounded
          class="white--text mx-2"
          @click="scrollToSection('#contact')"
        >
          Contact us
        </v-btn>
      </div>
    </v-app-bar>
  </div>
</template>

<style scoped>
/* 设置导航栏背景颜色为灰色 */
.v-app-bar {
  background-color: #424242 !important; /* 使用深灰色 */
}

/* 设置抽屉背景颜色为深灰色 */
.drawer-bg {
  background-color: #424242 !important;
}

/* 设置字体颜色为白色 */
.white--text {
  color: #ffffff !important;
}

/* 优化按钮间距 */
.mx-2 {
  margin-left: 8px;
  margin-right: 8px;
}

/* 优化抽屉中的图标和文字颜色 */
.v-list-item-title,
.v-icon {
  color: #ffffff !important;
}

/* 调整应用栏内边距 */
.px-4 {
  padding-left: 16px;
  padding-right: 16px;
}
</style>
