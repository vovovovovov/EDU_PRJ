<script setup>

</script>

<template>
  <!-- 头部导航 -->
  <header class='app-header'>
    <div class="container">
      <h1 class="logo">
        <RouterLink to="/">小兔鲜</RouterLink>
      </h1>
      <ul class="app-header-nav">
        <li class="home">
          <RouterLink to="/">首页</RouterLink>
        </li>
        <li> <RouterLink to="/AiChat">AI对话</RouterLink> </li>
        <li> <RouterLink to="/AiAgent">AI Agent</RouterLink> </li>
        <li> <RouterLink to="/">数据分析</RouterLink> </li>
      </ul>
      <div class="search">
        <i class="iconfont icon-search"></i>
        <input type="text" placeholder="搜一搜">
      </div>


    </div>
  </header>
</template>


<style scoped lang='scss'>
.app-header {
  background: #fff;

  .container {
    display: flex;
    align-items: center;
  }

  //logo的相关css样式
  .logo {
    width: 200px;
    a {
      display: block;
      height: 160px;
      width: 100%;
      text-indent: -9999px;
      background: url('@/assets/images/logo.png') no-repeat center 18px / contain;
    }
  }

  //导航页的css样式
  .app-header-nav {
    width: 820px;
    display: flex;
    padding-left: 80px;
    position: relative;
    z-index: 998;

    li {
      margin-right: 40px;
      width: 80px;     //设置导航栏字数长度
      text-align: center;

    }
  }

  //搜索相关css样式
  .search {
    width: 170px;
    height: 32px;
    position: relative;
    border-bottom: 1px solid #e7e7e7;
    line-height: 32px;

    .icon-search {
      font-size: 18px;
      margin-left: 5px;
    }

    input {
      width: 140px;
      padding-left: 5px;
      color: #110101;
    }
  }

}
</style>
