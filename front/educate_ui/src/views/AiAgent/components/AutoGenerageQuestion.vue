<script setup>
import { ref } from 'vue';
import axios from 'axios';

const questionInput = ref('');
const generatedQuestion = ref(null);
const userAnswer = ref('');
const feedback = ref('');
const isCorrect = ref(false);
const loading = ref(false);
const error = ref('');

// 从后端获取问题
const generateQuestion = async () => {
  if (!questionInput.value.trim()) return;

  loading.value = true;
  error.value = '';
  generatedQuestion.value = null;
  userAnswer.value = '';
  feedback.value = '';

  try {
    const response = await axios.post('autoGenerateQ/', {
      prompt: "请生成一个与下述内容相关的问题(不需要答案)：" + questionInput.value
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.data) {
      generatedQuestion.value = response.data;
      console.log(generatedQuestion)
    } else {
      throw new Error('返回的数据格式不正确');
    }
  } catch (err) {
    console.error(err);
    error.value = '生成问题时出错，请重试！';
  } finally {
    loading.value = false;
  }
};

// 检查用户答案
const checkAnswer = async () => {
  if (!userAnswer.value.trim()) {
    feedback.value = '请先输入你的答案。';
    isCorrect.value = false;
    return;
  }

  loading.value = true;
  try {
    const response = await axios.post('autoGenerateQ/', {
      prompt: "请生成一个与下述问题相关的答案：" + generatedQuestion.value
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.data ) {
      feedback.value = response.data;
    } else {
      throw new Error('返回的数据格式不正确');
    }
  } catch (err) {
    console.error(err);
    feedback.value = '检查答案时出错，请重试！';
    isCorrect.value = false;
  } finally {
    loading.value = false;
  }
};
</script>


<template>
  <section class="ai-quiz-generator">
    <h1>AI 自动出题</h1>

    <div class="input-group">
      <input type="text" placeholder="输入主题或提示" v-model="questionInput" class="input-field"/>
      <button @click="generateQuestion" class="generate-btn" :disabled="loading">
        生成问题
      </button>
    </div>

    <div v-if="loading" class="loading">处理中，请稍候...</div>
    <div v-if="error" class="generate_error">{{ error }}</div>

    <div v-if="generatedQuestion" class="questions">
      <h2>生成的问题</h2>
     <p :style="{ color: '#110101' }">{{ generatedQuestion }}</p>

      <div class="answer-section">
        <input
          type="text"
          v-model="userAnswer"
          placeholder="输入你的答案"
          class="answer-input"
        />
        <button @click="checkAnswer" class="check-btn" :disabled="loading">
          检查答案
        </button>
      </div>

      <div v-if="feedback" class="feedback" :class="feedback">
        {{ feedback }}
      </div>
    </div>
  </section>
</template>




<style scoped>
.ai-quiz-generator {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 10px;
  background: linear-gradient(135deg, #f0f8ff, #e6f7ff);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}

h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 2rem;
}

.input-group {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 2rem;
}

.input-field {
  padding: 1rem;
  border: 2px solid #007bff;
  border-radius: 5px;
  width: 100%;
  max-width: 400px;
  margin-right: 1rem;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.input-field:focus {
  outline: none;
  border-color: #0056b3;
}

.generate-btn {
  padding: 1rem 2rem;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.generate-btn:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.generate-btn:hover:not(:disabled) {
  background-color: #0056b3;
}

.loading {
  color: #007bff;
  font-size: 1.2rem;
  margin: 1rem 0;
}

.generate_error {
  color: #cc3300;
  font-size: 1.2rem;
  margin: 1rem 0;
}

.questions {
  margin-top: 2rem;
  padding: 1.5rem;
  border: 1px solid #d9edf7;
  border-radius: 5px;
  background-color: #ffffff;
}

.questions h2 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 1rem;
}

.answer-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1rem;
}

.answer-input {
  margin-top: 0.5rem;
  padding: 0.8rem;
  width: 100%;
  max-width: 400px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.check-btn {
  margin-top: 1rem;
  padding: 0.8rem 1.5rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.check-btn:hover {
  background-color: #218838;
}

.feedback {
  margin-top: 1rem;
  font-size: 1.2rem;
}

.feedback{
  color: #28a745;
}

/* 响应式设计 */
@media (max-width: 600px) {
  .ai-quiz-generator {
    padding: 1rem;
  }

  .input-group {
    flex-direction: column;
  }

  .input-field {
    max-width: 100%;
    margin-right: 0;
    margin-bottom: 1rem;
  }

  .generate-btn {
    width: 100%;
  }

  .answer-input {
    max-width: 100%;
  }

  .check-btn {
    width: 100%;
  }
}
</style>
