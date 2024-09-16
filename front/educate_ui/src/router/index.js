// createRouter：创建router实例对象
// createWebHistory：创建history模式的路由

import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/login/index.vue'
import Layout from '@/views/layout/index.vue'
import Home from '@/views/home/index.vue'
import AiChat from '@/views/AiChat/index.vue'
import AiAgent from '@/views/AiAgent/index.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // path和component对应关系的位置
  routes: [
    {
      path: '/',
      component: Layout,

      // 子路由
      // children: [
      //   {
      //     path:'',
      //     component:Home
      //   },
      //
      //   // AiAgent设计
      //   {
      //     path: '/AiAgent',
      //     component: AiAgent
      //   },
      // ],
    },

    //登陆界面
    {
      path: '/login',
      component: Login
    },


    // AI对话界面
    {
      path: '/AiChat',
      component: AiChat
    },

  ]
})

export default router