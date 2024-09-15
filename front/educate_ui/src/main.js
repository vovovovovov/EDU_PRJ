
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
// 引用初始化样式文件
import '@/styles/common.scss'

// 简化api请求路径
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:8000/api/';

const app = createApp(App)

app.use(router)

app.mount('#app')
// createApp(App).mount('#app')
