import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
// 引用初始化样式文件

// 导入vuetify
import vuetify from './plugins/vuetify';

// 简化api请求路径
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:8000/api/';

const app = createApp(App)

app.use(router)
app.use(vuetify)

app.mount('#app')
