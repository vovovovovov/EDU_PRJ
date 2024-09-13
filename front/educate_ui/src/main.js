
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
// 引用初始化样式文件
import '@/styles/common.scss'

const app = createApp(App)

app.use(router)

app.mount('#app')
// createApp(App).mount('#app')
