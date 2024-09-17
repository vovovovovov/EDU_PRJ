<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';  // 导入 axios

const router = useRouter();

// 返回首页
const goBack = () => {
  router.push('/');
};

// 当前选中的聊天ID
const activeChatId = ref(null);
const chatHistory = ref([]);  // 初始化为空数组

// 聊天消息
const messages = ref([]);
const inputMessage = ref('');
const chatContainer = ref(null);

// 获取聊天记录列表
const fetchChatHistory = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/chat-sessions/');
    chatHistory.value = response.data;
    if (chatHistory.value.length > 0) {
      activeChatId.value = chatHistory.value[0].id;
      await fetchMessages(activeChatId.value);
    }
  } catch (error) {
    console.error('获取聊天记录失败', error);
  }
};

// 获取指定聊天的消息
const fetchMessages = async (chatSessionId) => {
  try {
    const response = await axios.get(`http://localhost:8000/api/chat-sessions/${chatSessionId}/`);
    messages.value = response.data.messages;
    scrollToBottom();
  } catch (error) {
    console.error('获取聊天消息失败', error);
  }
};

// 选择聊天时，加载对应的消息
const selectChat = async (id) => {
  activeChatId.value = id;
  await fetchMessages(id);
};

// 创建新聊天
const createNewChat = async () => {
  try {
    const response = await axios.post('http://localhost:8000/api/chat-sessions/', {
      title: `新的聊天 ${chatHistory.value.length + 1}`,
    });
    const newChat = response.data;
    chatHistory.value.unshift(newChat);
    activeChatId.value = newChat.id;
    messages.value = [];
  } catch (error) {
    console.error('创建新聊天失败', error);
  }
};

// 删除聊天
const deleteChat = async (id) => {
  try {
    await axios.delete(`http://localhost:8000/api/chat-sessions/${id}/`);
    chatHistory.value = chatHistory.value.filter((chat) => chat.id !== id);
    if (activeChatId.value === id && chatHistory.value.length > 0) {
      activeChatId.value = chatHistory.value[0].id;
      await fetchMessages(activeChatId.value);
    } else if (chatHistory.value.length === 0) {
      activeChatId.value = null;
      messages.value = [];
    }
  } catch (error) {
    console.error('删除聊天失败', error);
  }
};

// 发送消息
const sendMessage = async () => {
  if (inputMessage.value.trim() !== '') {
    const userContent = inputMessage.value;
    inputMessage.value = '';

    // 在前端显示用户的消息
    const userMessage = {
      id: Date.now(),
      sender: 'user',
      content: userContent,
      timestamp: new Date().toISOString(),
    };
    messages.value.push(userMessage);
    scrollToBottom();

    try {
      // 向后端发送用户消息，获取 AI 回复
      const response = await axios.post('generate-reply/', {
        chat_session: activeChatId.value,
        content: userContent,
      });

      const aiMessage = response.data;
      messages.value.push(aiMessage);
      scrollToBottom();
    } catch (error) {
      console.error('发送消息失败', error);
      // 您可以在此处显示错误提示
    }
  }
};

// 滚动到底部
const scrollToBottom = () => {
  nextTick(() => {
    if (chatContainer.value) {
      chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    }
  });
};

// 在组件挂载时，获取聊天记录
onMounted(async () => {
  await fetchChatHistory();
});
</script>



<template>
  <div class="chat-interface">
    <!-- 左侧聊天记录侧边栏 -->
    <div class="sidebar">
      <div class="sidebar-header">
        <h3>聊天记录</h3>
        <button @click="createNewChat">
          <span>＋ 新建聊天</span>
        </button>
      </div>
      <ul>
        <li
          v-for="chat in chatHistory"
          :key="chat.id"
          :class="{ active: chat.id === activeChatId }"
          @click="selectChat(chat.id)"
        >
          <i class="icon-chat"></i>
          <span>{{ chat.title }}</span>
          <button class="delete-button" @click.stop="deleteChat(chat.id)">
            <i class="icon-delete"></i>
          </button>
        </li>
      </ul>
    </div>


    <!-- 主聊天区域 -->
    <div class="main-chat">
      <!-- 返回主页按钮 -->
      <button class="back-button" @click="goBack">返回主页</button>

      <div class="header">
        <h2>AI 学海行</h2>
      </div>
      <div class="chat-container" ref="chatContainer">
        <div
          v-for="message in messages"
          :key="message.id"
          :class="['message', message.type === 'ai' ? 'ai-message' : 'user-message']"
        >
          <div class="avatar">
            <img :src="message.type === 'ai' ? 'ai-avatar.png' : 'user-avatar.png'" alt="avatar">
          </div>
          <div class="content">
            <div class="bubble">{{ message.content }}</div>
          </div>
        </div>
      </div>

      <div class="input-container">
        <input
          v-model="inputMessage"
          type="text"
          placeholder="请输入消息..."
          @keyup.enter="sendMessage"
        />
        <button @click="sendMessage">
          <svg viewBox="0 0 24 24">
            <path d="M2 21l21-9L2 3v7l15 2-15 2v7z"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>





<style scoped lang="scss">
.chat-interface {
  display: flex;
  height: 100vh;
  background-color: #f0f0f0;
  color: #333;

  .sidebar {
    width: 250px;
    background-color: #fff;
    border-right: 1px solid #ddd;
    display: flex;
    flex-direction: column;

    .sidebar-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;

      h3 {
        margin: 0;
        font-size: 1.2em;
      }

      button {
        background-color: transparent;
        border: none;
        color: #007bff;
        font-size: 1em;
        cursor: pointer;
        display: flex;
        align-items: center;

        span {
          margin-left: 5px;
        }

        &:hover {
          color: #0056b3;
        }
      }
    }

    ul {
      flex: 1;
      list-style: none;
      padding: 0 10px;
      margin: 0;
      overflow-y: auto;

      li {
        display: flex;
        align-items: center;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        position: relative;
        transition: background-color 0.3s;

        &:hover {
          background-color: #f5f5f5;
        }

        &.active {
          background-color: #e6f7ff;
        }

        i {
          font-size: 1.2em;
          margin-right: 10px;
        }

        span {
          flex: 1;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .delete-button {
          background: none;
          border: none;
          cursor: pointer;
          padding: 5px;
          display: flex;
          align-items: center;
          color: #999;
          transition: color 0.3s;

          &:hover {
            color: #ff4d4f;
          }

          i {
            font-size: 1em;
          }
        }
      }
    }
  }

  .main-chat {
    flex: 1;
    display: flex;
    flex-direction: column;

    .back-button {
      position: fixed;
      top: 20px;
      left: 270px; /* 与侧边栏的宽度匹配 */
      padding: 8px 16px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      z-index: 1000;
    }

    .back-button:hover {
      background-color: #0056b3;
    }

    .header {
      text-align: center;
      padding: 20px 0;
      background-color: #fff;
      border-bottom: 1px solid #ddd;

      h2 {
        margin: 0;
      }
    }

    .chat-container {
      flex: 1;
      overflow-y: auto;
      padding: 20px;
      background-color: #fafafa;
    }

    .message {
      display: flex;
      margin-bottom: 15px;
      align-items: flex-end;

      &.user-message {
        flex-direction: row-reverse;
      }

      .avatar {
        width: 40px;
        height: 40px;
        margin: 0 10px;

        img {
          width: 100%;
          height: 100%;
          border-radius: 50%;
        }
      }

      .content {
        max-width: 70%;

        .bubble {
          background-color: #e6e6e6;
          padding: 10px 15px;
          border-radius: 20px;
          position: relative;
          color: #333;

          &::after {
            content: '';
            position: absolute;
            border: 10px solid transparent;
          }
        }
      }

      &.ai-message {
        .content {
          .bubble {
            background-color: #fff;
            border: 1px solid #ddd;

            &::after {
              left: -10px;
              top: 50%;
              transform: translateY(-50%);
              border-right-color: #fff;
            }
          }
        }
      }

      &.user-message {
        .content {
          .bubble {
            background-color: #007bff;
            color: #fff;

            &::after {
              right: -10px;
              top: 50%;
              transform: translateY(-50%);
              border-left-color: #007bff;
            }
          }
        }
      }
    }

    .input-container {
      display: flex;
      padding: 10px;
      background-color: #fff;
      border-top: 1px solid #ddd;

      input[type='text'] {
        flex: 1;
        padding: 10px 15px;
        border: 1px solid #ddd;
        border-radius: 30px;
        outline: none;
        margin-right: 10px;

        ::placeholder {
          color: #999;
        }
      }

      button {
        width: 50px;
        height: 50px;
        background-color: #007bff;
        border: none;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;

        svg {
          width: 24px;
          height: 24px;
          fill: #fff;
        }

        &:hover {
          background-color: #0056b3;
        }
      }
    }
  }
}

/* 图标样式 */
.icon-chat::before {
  content: '💬';
}

.icon-delete::before {
  content: '✖';
}
</style>
