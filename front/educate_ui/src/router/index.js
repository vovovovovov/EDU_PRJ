// createRouter：创建router实例对象
// createWebHistory：创建history模式的路由

import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/login/index.vue'
import Layout from '@/views/layout/index.vue'
import Demo from '@/views/demo/index.vue'

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


    //登陆界面(未实现)
    {
      path: '/login',
      component: Login
    },

  ]
})

export default router