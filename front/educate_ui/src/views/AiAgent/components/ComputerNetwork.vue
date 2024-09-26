<script setup>
import { reactive } from 'vue';

const topics = reactive([
  {
    title: '1. 计算机网络概述',
    description: '计算机网络是指通过通信设备和线路将地理位置不同的、功能独立的多台计算机连接起来，以功能完善的网络软件（操作系统和协议）实现资源共享和信息传递的系统。',
    points: [
      '资源共享',
      '提高可靠性',
      '分布式处理',
    ],
  },
  {
    title: '2. 网络分层模型',
    description: '为了简化网络的设计和实现，采用了分层的方式。常见的模型有 OSI 七层模型和 TCP/IP 四层模型。',
    points: [
      '物理层',
      '数据链路层',
      '网络层',
      '传输层',
      '会话层',
      '表示层',
      '应用层',
    ],
  },
  {
    title: '3. 传输介质',
    description: '传输介质是网络中用于传输信息的物理通道，包括有线和无线两大类。',
    points: [
      '双绞线',
      '同轴电缆',
      '光纤',
      '无线电波',
    ],
  },
  {
    title: '4. IP 地址与子网掩码',
    description: 'IP 地址用于标识网络中的主机，子网掩码用于划分网络和主机部分。',
    points: [
      'IPv4 地址格式',
      'IPv6 地址格式',
      '公有 IP 和私有 IP',
      '子网划分',
    ],
  },
  {
    title: '5. TCP 和 UDP 协议',
    description: '传输层的两个主要协议，用于不同的传输需求。',
    points: [
      'TCP：面向连接，可靠传输',
      'UDP：无连接，不可靠传输',
      '应用场景对比',
    ],
  },
  {
    title: '6. 常见网络设备',
    description: '网络中使用的各种硬件设备。',
    points: [
      '集线器（Hub）',
      '交换机（Switch）',
      '路由器（Router）',
      '网关（Gateway）',
    ],
  },
  {
    title: '7. 网络安全',
    description: '保障网络和数据安全的技术和策略。',
    points: [
      '防火墙',
      '加密技术',
      '入侵检测',
      '身份认证',
    ],
  },
  {
    title: '8. 无线网络',
    description: '利用无线通信技术实现的网络。',
    points: [
      'Wi-Fi 技术',
      '蓝牙',
      '蜂窝移动网络',
      '物联网（IoT）',
    ],
  },
]);
</script>

<template>
  <div class="network-basics">
    <header>
      <h1>计算机网络基本知识</h1>
    </header>
    <main>
      <section v-for="(topic, index) in topics" :key="index" class="topic-section">
        <h2>{{ topic.title }}</h2>
        <p>{{ topic.description }}</p>
        <ul v-if="topic.points">
          <li v-for="(point, idx) in topic.points" :key="idx">{{ point }}</li>
        </ul>
      </section>
    </main>
    <footer>
      <p>© 计算机网络基本知识</p>
    </footer>
  </div>
</template>

<style scoped>
body, html {
  margin: 0;
  padding: 0;
  height: 100%;
}

.network-basics {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

header {
  background: linear-gradient(90deg, #4b6cb7, #182848);
  color: white;
  padding: 2rem;
  text-align: center;
}

header h1 {
  margin: 0;
  font-size: 3rem;
}

main {
  flex: 1;
  padding: 2rem;
  background-color: #f0f2f5;
}

.topic-section {
  background-color: white;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.topic-section h2 {
  color: #333;
  margin-bottom: 1rem;
}

.topic-section p {
  color: #555;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.topic-section ul {
  list-style-type: disc;
  padding-left: 1.5rem;
}

.topic-section li {
  margin-bottom: 0.5rem;
  color: #444;
}

footer {
  background-color: #f0f2f5;
  text-align: center;
  padding: 1rem;
  color: #888;
}
</style>
