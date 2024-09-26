<script setup>
import { ref, watch } from 'vue';
import { customCards } from './customData.js'; // 导入自定义数据

// 响应式状态变量
const cards = ref([]); // 存储所有卡片
const filteredCards = ref([]); // 存储过滤后的卡片
const searchTerm = ref('');
const activeFilter = ref('All');

// 初始化数据
cards.value = customCards;
filteredCards.value = cards.value;

// 按类型过滤卡片
const filterByType = (type) => {
  activeFilter.value = type;
  applyFilters();
};

// 搜索与筛选
const applyFilters = () => {
  let tempCards = cards.value;

  // 类型过滤
  if (activeFilter.value !== 'All') {
    tempCards = tempCards.filter((card) => card.type === activeFilter.value);
  }

  // 名称搜索
  if (searchTerm.value.trim() !== '') {
    const term = searchTerm.value.toLowerCase();
    tempCards = tempCards.filter((card) =>
      card.name.toLowerCase().includes(term)
    );
  }

  filteredCards.value = tempCards;
};

// 监听 searchTerm 和 activeFilter 的变化，自动应用过滤
watch([searchTerm, activeFilter], () => {
  applyFilters();
});
</script>

<template>
  <section>
    <h1>AI Agent <br /> 知识卡片学习</h1>

    <!-- 过滤选项 -->
    <div class="filter">
      <div
        class="item"
        :class="{ active: activeFilter === 'All' }"
        @click="filterByType('All')"
      >
        All
      </div>
      <div
        class="item"
        :class="{ active: activeFilter === 'AI Agent' }"
        @click="filterByType('AI Agent')"
      >
        AI Agent
      </div>
      <div
        class="item"
        :class="{ active: activeFilter === '知识卡片' }"
        @click="filterByType('知识卡片')"
      >
        知识卡片
      </div>
      <div
        class="item"
        :class="{ active: activeFilter === '自定义Agent' }"
        @click="filterByType('自定义Agent')"
      >
        自定义Agent
      </div>
    </div>

    <!-- 搜索输入框 -->
    <input
      type="text"
      placeholder="Search what you want"
      v-model="searchTerm"
    />

    <!-- 卡片展示 -->
    <div v-if="filteredCards.length > 0" class="container-cards">
      <ul class="card-list">
        <li v-for="card in filteredCards" :key="card.id" class="card">
          <!-- 展示图片   -->
          <div class="image">
            <img :src="card.image" :alt="card.name" />
          </div>

          <!-- 展示卡片标签 -->
          <router-link :to="`/CardDetail/${card.id}`" class="custom-link">
            <h2>{{ card.name }}</h2>
          </router-link>
          <!-- 展示卡片类型 -->
          <div class="status">
            <span
              :class="
                card.type === 'AI Agent' ? 'agent' :
                card.type === '知识卡片' ? 'card-knowledge' :
                'custom-agent'
              "
            ></span>
            <span>{{ card.type }}</span>
          </div>

          <!-- 展示额外信息 -->
          <div class="information">
            <p>{{ card.description }}</p>
            <div v-if="card.additionalInfo">
              <div v-for="(value, key) in card.additionalInfo" :key="key">
                <strong>{{ key }}:</strong> {{ value }}
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.custom-link {
  text-decoration: none;
  color: white;
}
section {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 0rem 10rem 0rem 10rem;
}

section > h1 {
  text-align: center;
  font-size: 45px;
  margin-top: 4rem;
}

/* 过滤的css */
section .filter {
  width: 25%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: var(--background-card);
  padding: 0.9rem;
  font-size: 15px;
  border-radius: 0.5rem;
  cursor: pointer;
  margin-bottom: 1rem;
}
section .filter :hover {
  color: var(--text-orange);
}
/*  搜索的css */
section > input {
  width: 25%;
  padding: 0.9rem;
  border-radius: 0.5rem;
  border: none;
  margin-bottom: 1rem;
  background-color: var(--text-white);
}

section .container-cards {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-list {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 四列 */
  gap: 16px; /* 卡片之间的间距 */
  width: 100%; /* 充满容器宽度 */
  box-sizing: border-box;
}

.card {
  width: 85%; /*  设置卡片占比   */
  margin: 1%;
  border-radius: 1rem;
  background-color: var(--background-card);
  box-sizing: border-box;
  text-align: center;
  overflow: hidden;
  transition: transform 200ms ease-in-out;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  height: 100%; /* 卡片高度为容器的 100% */
}
.card:hover {
  transform: scale(1.05);
  h2 {
    color: var(--text-orange);
  }
}

.card .image {
  width: 100%;
  height: 200px; /* 固定高度，您可以根据需要调整 */
}
.card .image > img {
  width: 100%;
  height: 100%;
  object-fit: contain; /* 保持图像的完整性，缩放以适应容器 */
  background-color: #f0f0f0; /* 可选：为空白区域添加背景色 */
}
.card > h2 {
  margin: 5px;
}

.status {
  margin: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
.status span {
  color: var(--text-gray);
}
.status span:first-child {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 0.5rem;
}
.agent {
  background-color: green;
}
.card-knowledge {
  background-color: red;
}
.custom-agent {
  background-color: white;
}

.card .information {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.card .information > span {
  color: var(--text-gray);
  margin: 2px;
}
.card .information > span:last-child {
  margin-bottom: 20px;
}
.item.active {
  color: orange;
}

/* MOBILE */
@media only screen and (min-width: 370px) and (max-width: 600px) {
  section {
    width: 100%;
    margin: 0;
  }
  section > h1 {
    font-size: 35px;
    margin-top: 1rem;
  }
  section .filter {
    width: 80%;
  }
  section > input {
    width: 80%;
  }
  .card {
    width: 80%;
    margin-bottom: 1rem;
  }
}
/* TABLET*/
@media only screen and (min-width: 601px) and (max-width: 768px) {
  section {
    width: 100%;
    margin: 0;
  }
  section > h1 {
    font-size: 35px;
    margin-top: 1rem;
  }
  section .filter {
    width: 86%;
  }
  section > input {
    width: 86%;
  }
  .card {
    width: 40%;
    margin-bottom: 1rem;
  }
}
/* LAPTOP */
@media only screen and (min-width: 769px) and (max-width: 1024px) {
  section {
    width: 100%;
    margin: 0;
  }
  section > h1 {
    font-size: 45px;
    margin-top: 4rem;
  }
  section .filter {
    width: 40%;
  }
  section > input {
    width: 40%;
  }
  .card {
    width: 30%;
    margin-bottom: 1rem;
  }
}
/* LARGE SCREEN */
@media only screen and (min-width: 1025px) and (max-width: 1201px) {
  section {
    width: 100%;
    margin: 0;
  }
  section > h1 {
    font-size: 45px;
    margin-top: 4rem;
  }
  section .filter {
    width: 45%;
  }
  section > input {
    width: 45%;
  }
  .card {
    width: 20%;
    margin-bottom: 1rem;
  }
}
</style>
