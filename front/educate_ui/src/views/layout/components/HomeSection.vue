<script setup>
import { ref, watch } from 'vue';
import bgHero from '@/assets/img/bgHero.jpg';
import icon1 from '@/assets/img/person_icon1.png';
import icon2 from '@/assets/img/real_time_icon2.png';
import icon3 from '@/assets/img/study_icon3.png';
import YouTube from 'vue3-youtube'; // 确保安装了此包

// 响应式变量
const dialog = ref(false);
const videoId = ref('i8IvvHJssWE');
const features = [
  {
    img: icon1,
    title: '个性化学习',
    text: '大语言模型个性化学习是一种根据用户的需求和学习风格，' +
        '动态调整内容和反馈的技术，能够帮助学习者更加高效地理解复杂概念，并提供个性化的学习体验，从而提高学习效果。',
  },
  {
    img: icon2,
    title: '实时交互',
    text: '大语言模型的实时交互在能够根据学生的提问和反馈，瞬时生成个性化的教学内容' +
        '和指导，帮助学生在学习过程中获得即时解惑与强化练习，从而提升学习效果与参与感。',
  },
  {
    img: icon3,
    title: '学习扩展',
    text: '大模型在教育领域的扩展学习能力，能够通过整合多种数据来源和知识体系，自动生成' +
        '跨学科的学习资源与个性化的教学内容，帮助学生在不同知识领域之间建立联系，从而深化理解并提升综合学习能力。',
  },
];

const player = ref(null);

// 方法
const ready = (event) => {
  player.value = event.target;
};

const playing = (event) => {
  // 视频正在播放
};

const change = () => {
  videoId.value = 'another video id';
};

const stop = () => {
  if (player.value) {
    player.value.stopVideo();
  }
};

const pause = () => {
  if (player.value) {
    player.value.pauseVideo();
  }
};

// 监听器
watch(dialog, (value) => {
  if (!value) {
    pause();
  }
});

// 滚动到指定部分
const goToSection = (id) => {
  const element = document.querySelector(id);
  if (element) {
    element.scrollIntoView({behavior: 'smooth'});
  }
};
</script>

<template>
  <section id="hero">
    <!-- 视差效果部分 -->
    <div class="parallax" :style="{ backgroundImage: `url(${bgHero})`, height: '750px' }">
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="center">
            <v-col cols="12" md="6" xl="8">
              <h1 class="display-2 font-weight-bold mb-4">AI 学海行</h1>
              <h1 class="font-weight-light">
                释放AI的力量，享受学习的乐趣。
              </h1>
              <v-btn rounded
                variant="outlined"
                size="large"
                color="primary"
                @click="goToSection('#features')"
                class="mt-5"
              >
                了解更多
                <v-icon class="ml-2">mdi-arrow-down</v-icon>
              </v-btn>
              <!-- 视频部分 -->

              <div class="video d-flex align-center py-4">
                <a @click.stop="dialog = true" class="playBut">
                  <!-- SVG 代码 -->
                  <!-- （在此插入您的 SVG 代码） -->
                </a>
                <p class="subheading ml-2 mb-0">Watch the video</p>
              </div>
            </v-col>
            <v-col cols="12" md="6" xl="4" class="hidden-sm-and-down"></v-col>
          </v-row>
        </v-col>
      </v-row>
      <div class="svg-border-waves text-white">
        <v-img src="@/assets/img/borderWaves.svg" />
      </div>
    </div>

    <!-- 特点部分(三个图片) -->
    <v-container fluid id="features" class="mt-2">
      <v-row align="center" justify="center">
        <v-col cols="10">
          <v-row align="center" justify="space-around">
            <v-col
              cols="12"
              sm="4"
              class="text-center"
              v-for="(feature, i) in features"
              :key="i"
            >
              <v-hover v-slot="{ isHovering }">
                <v-card
                  class="card"
                  rounded
                  :elevation="isHovering ? 10 : 4"
                  :class="{ up: isHovering }"
                >
                  <v-img
                    :src="feature.img"
                    class="d-block ml-auto mr-auto"
                    :class="{ 'zoom-effect': isHovering }"
                    style="max-width: 100px;"
                  ></v-img>
                  <h1 class="font-weight-regular">{{ feature.title }}</h1>
                  <h4 class="font-weight-regular subtitle-1">
                    {{ feature.text }}
                  </h4>
                </v-card>
              </v-hover>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

    <!-- 视频对话框 -->
    <v-dialog v-model="dialog" max-width="640">
      <v-card>
        <YouTube
          :video-id="videoId"
          @ready="ready"
          @playing="playing"
        ></YouTube>
      </v-card>
    </v-dialog>

    <!-- 底部波浪(暂时无用) -->
<!--    <div class="svg-border-waves">-->
<!--      <img src="@/assets/img/wave2.svg"  alt="波浪"/>-->
<!--    </div>-->
  </section>
</template>


<style scoped lang="scss">
.parallax {
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  position: relative;
  padding: 200px 0 0 0; /* 上、右、下、左 */
}

.playBut {
  display: inline-block;
  transition: all 0.5s ease;

  &:hover {
    .triangle {
      stroke-dashoffset: 0;
      opacity: 1;
      stroke: white;
      animation: nudge 0.7s ease-in-out;
    }

    .circle {
      stroke-dashoffset: 0;
      opacity: 1;
    }
  }
}


@keyframes nudge {
  0% {
    transform: translateX(0);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(5px);
  }
  70% {
    transform: translateX(-2px);
  }
  100% {
    transform: translateX(0);
  }
}

.card {
  min-height: 300px;
  padding: 10px;
  transition: 0.5s ease-out;
}

.card .v-image {
  margin-bottom: 15px;
  transition: 0.75s;
}

.card h1 {
  margin-bottom: 10px;
}

.zoom-effect {
  transform: scale(1.1);
}

.up {
  transform: translateY(-20px);
  transition: 0.5s ease-out;
}


.svg-border-waves img {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  margin-bottom: -2px;
  z-index: -1;
}

#hero {
  z-index: 0;
}

.svg-border-waves img {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  margin-bottom: -2px;
  z-index: -1;
}

/* 设定主标题的字体大小和颜色 */
h1.display-2 {
  font-size: 3rem; /* 字体大小 */
  color: white; /* 字体颜色 */
  line-height: 1.2;
}
/* 子标题或普通的 h1 标签 */
h1.font-weight-light {
  font-size: 2rem; /* 字体大小 */
  color: #ddd; /* 其他字体颜色 */
  line-height: 1.4;
}
/* 段落的字体大小和颜色 */
p {
  font-size: 1.2rem; /* 字体大小 */
  color: #f0f0f0; /* 字体颜色 */
}
/* 设定按钮的字体大小和颜色 */
.v-btn {
  font-size: 1.5rem; /* 字体大小 */
  color: white; /* 按钮文本颜色(这个无法控制) */

}


</style>

<style scoped>
section {
  position: relative;
}
</style>
