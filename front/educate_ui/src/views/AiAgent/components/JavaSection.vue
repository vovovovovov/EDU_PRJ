<template>
  <div class="java-basics">
    <h1>Java 基础知识</h1>
    <div class="card-container">
      <div class="card" v-for="(topic, index) in topics" :key="index">
        <h2>{{ topic.title }}</h2>
        <p>{{ topic.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

const topics = reactive([
  {
    title: '什么是 Java？',
    description: 'Java 是一种广泛使用的面向对象编程语言，具有跨平台特性。'
  },
  {
    title: '基本数据类型',
    description: 'Java 有八种基本数据类型：byte, short, int, long, float, double, char, boolean。'
  },
  {
    title: '面向对象编程',
    description: 'Java 支持封装、继承、多态等面向对象的特性。'
  },
  {
    title: '类与对象',
    description: '类是对象的模板，对象是类的实例。'
  },
  {
    title: '异常处理',
    description: 'Java 使用 try, catch, finally 进行异常处理，确保程序的健壮性。'
  },
  {
    title: 'Java 集合框架',
    description: '集合框架提供了一组接口和类，用于存储和操作数据集合，如 List, Set, Map。'
  },
  {
    title: '多线程编程',
    description: 'Java 支持多线程编程，可以提高程序的性能和响应速度。'
  },
  {
    title: '输入输出 (I/O)',
    description: 'Java 提供了丰富的 I/O 库，用于读取和写入数据流。'
  }
]);
</script>

<style scoped>
.java-basics {
  font-family: 'Arial', sans-serif;
  padding: 2rem;
  background-color: #f0f2f5;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 2rem;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.card {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 1rem;
  padding: 1.5rem;
  width: 300px;
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-5px);
}

.card h2 {
  color: #007acc;
  margin-bottom: 1rem;
}

.card p {
  color: #555;
  line-height: 1.6;
}
</style>
