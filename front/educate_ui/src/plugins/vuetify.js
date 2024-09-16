// src/plugins/vuetify.js

// 1. 导入必要的模块
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

// 2. 定义自定义主题
const customTheme = {
  dark: false,
  colors: {
    primary: '#119DA4',
    secondary: '#171b34',
    accent: '#3D87E4',
  },
}

// 3. 创建 Vuetify 实例
const vuetify = createVuetify({
  theme: {
    defaultTheme: 'customTheme',
    themes: {
      customTheme,
    },
  },
})

export default vuetify
