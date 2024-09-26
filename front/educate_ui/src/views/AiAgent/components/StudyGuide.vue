<template>
  <div class="study-guide">
    <header>
      <h1>信息检索与数据挖掘 - 智能导学系统</h1>
      <div class="progress-bar">
        <div class="progress" :style="{ width: progress + '%' }"></div>
        <span>{{ progress }}% 完成</span>
      </div>
    </header>

    <!-- 课程大纲 -->
    <nav class="course-outline">
      <h2>课程大纲</h2>
      <ul>
        <li
          v-for="(module, index) in modules"
          :key="index"
          @click="selectModule(index)"
          :class="{ active: currentModuleIndex === index }"
        >
          {{ module.title }}
        </li>
      </ul>
    </nav>

    <!-- 模块内容 -->
    <main v-if="currentModule">
      <section class="module-content">
        <h2>{{ currentModule.title }}</h2>
        <p>{{ currentModule.description }}</p>

        <!-- 学习目标 -->
        <section class="learning-goals">
          <h3>学习目标</h3>
          <ul>
            <li v-for="(goal, index) in currentModule.goals" :key="index">{{ goal }}</li>
          </ul>
        </section>

        <!-- 关键概念 -->
        <section class="key-concepts">
          <h3>关键概念</h3>
          <ul>
            <li v-for="(concept, index) in currentModule.concepts" :key="index">{{ concept }}</li>
          </ul>
        </section>

        <!-- 图片插入 -->
        <section class="module-image">
          <img src="../../../assets/img/title.png" alt="相关图示" />
        </section>

        <!-- 智能学习建议 -->
        <section class="learning-suggestions">
          <h3>学习建议</h3>
          <p>{{ currentModule.suggestions }}</p>
        </section>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// 课程模块数据
const modules = ref([
  {
    title: '模块 1: 信息检索概述',
    description: '介绍信息检索的基本概念，包括检索系统的基本组成、倒排索引等。',
    goals: ['理解信息检索的基本概念', '掌握倒排索引的原理', '熟悉基本检索系统的组成'],
    concepts: ['倒排索引', '布尔检索', '查询处理'],
    suggestions: '建议通过阅读相关文献，进一步理解信息检索的实际应用场景。',
  },
  {
    title: '模块 2: 信息检索模型',
    description: '探讨信息检索模型，包括布尔模型、向量空间模型和概率模型。',
    goals: ['掌握不同信息检索模型的特点', '理解布尔检索、向量空间模型的计算方法'],
    concepts: ['布尔模型', '向量空间模型', '概率模型'],
    suggestions: '重点关注向量空间模型的应用，尝试在实际数据集上应用这些模型。',
  },
  {
    title: '模块 3: 数据挖掘基础',
    description: '介绍数据挖掘的基本原理和方法，包括数据预处理、分类、聚类等。',
    goals: ['理解数据挖掘的基本任务', '掌握数据分类与聚类的常用算法'],
    concepts: ['分类', '聚类', '关联分析'],
    suggestions: '推荐结合课程内容，使用开源工具如Weka、Python等实践数据挖掘算法。',
  },
  {
    title: '模块 4: 数据预处理',
    description: '介绍数据挖掘中的数据预处理步骤，包括缺失值处理、数据标准化等。',
    goals: ['掌握数据预处理的各项步骤', '理解数据清洗与变换的重要性'],
    concepts: ['数据清洗', '数据标准化', '缺失值处理'],
    suggestions: '可以在真实项目中尝试进行数据预处理，如处理不完整或不一致的数据集。',
  },
]);

// 当前选择的模块
const currentModuleIndex = ref(0);
const currentModule = computed(() => modules.value[currentModuleIndex.value]);

// 学习进度，假设每完成一个模块增加25%
const progress = computed(() => ((currentModuleIndex.value + 1) / modules.value.length) * 100);

function selectModule(index) {
  currentModuleIndex.value = index;
}
</script>

<style scoped>
/* 整体布局 */
.study-guide {
  display: flex;
  flex-direction: column;
  height: 100vh;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #1e1e1e; /* 深色背景 */
  color: #f0f0f0; /* 文字颜色 */
}

header {
  background-color: #4b6cb7;
  color: white;
  padding: 1rem;
  text-align: center;
}

.progress-bar {
  background-color: #e0e0e0;
  height: 10px;
  border-radius: 5px;
  margin-top: 0.5rem;
  position: relative;
}

.progress {
  background-color: #76c7c0;
  height: 100%;
  transition: width 0.5s ease;
}

.progress-bar span {
  position: absolute;
  right: 10px;
  top: -25px;
  color: white;
}

/* 课程大纲 */
nav.course-outline {
  background-color: #343a40;
  padding: 1rem;
  overflow-y: auto;
  width: 250px;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  color: #ffffff;
}

.course-outline h2 {
  margin-top: 0;
}

.course-outline ul {
  list-style-type: none;
  padding: 0;
}

.course-outline li {
  padding: 0.5rem;
  cursor: pointer;
  margin-bottom: 10px;
  background-color: #495057;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.course-outline li.active {
  background-color: #76c7c0;
  font-weight: bold;
  color: white;
}

.course-outline li:hover {
  background-color: #6c757d;
}

/* 模块内容 */
main {
  margin-left: 260px;
  padding: 2rem;
  flex: 1;
}

.module-content {
  background-color: #2a2e35;
  padding: 2rem;
  border-radius: 10px;
}

h2 {
  margin-top: 0;
  color: #ffffff;
}

.learning-goals ul,
.key-concepts ul {
  list-style-type: disc;
  padding-left: 1.5rem;
}

.learning-suggestions {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #3e444a;
  border-left: 5px solid #4b6cb7;
}

/* 图片插入 */
.module-image img {
  max-width: 100%;
  margin-top: 2rem;
  border-radius: 10px;
}
</style>
