// createRouter：创建router实例对象
// createWebHistory：创建history模式的路由

import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/login/index.vue'
import Layout from '@/views/layout/index.vue'
import Demo from '@/views/demo/index.vue'
import AiAgent from '@/views/AiAgent/index.vue'
import JavaSection from "@/views/AiAgent/components/JavaSection.vue";
import AutoGenerageQuestion from "@/views/AiAgent/components/AutoGenerageQuestion.vue";
import ComputerNetwork from "@/views/AiAgent/components/ComputerNetwork.vue";
import StudyGuide from "@/views/AiAgent/components/StudyGuide.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // path和component对应关系的位置
  routes: [
    {
      path: '/',
      component: Layout,

    },

    // demo
    {
      path:'/demo',
      component:Demo,
    },

    // AiAgent
    {
      path:'/AiAgent',
      component:AiAgent,
    },

    // 卡片详细页数
    {
      path:'/CardDetail',

      children:[
        {
          path:'1',
          component:Demo
        },

        {
          path:'2',
          component:AutoGenerageQuestion
        },

        {
          path: '3',
          component:JavaSection
          // beforeEnter() {
          // // 直接跳转到外部网址
          // window.location.href = 'https://zh.wikipedia.org/wiki/Java';
          // },
        },

        {
          path: '4',
          component:ComputerNetwork
        },

        {
          path: '7',
          component:StudyGuide
        }

      ]
    },

    //登陆界面(无用)
    {
      path: '/login',
      component: Login
    },

  ]
})

export default router