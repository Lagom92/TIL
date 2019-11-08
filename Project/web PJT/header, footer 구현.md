# 반응형 웹 페이지 제작



### 개발 환경 구성(window 기준)

npm 설치(https://nodejs.or/ko/)



vue.js, vue-cli 설치

```
npm install
npm install -g yarn
npm install -g @vue/cli
npm install vue
npm install -g firebase-tools
npm run serve
```



- 주의

node.js 를 너무 최신으로 받으면 에러가 발생함



### 1-1. header, footer 구현

##### 네비게이션 바 역할을 하는 헤더와 사이트의 메타 정보가 노출되는 푸터를 구현합니다.



- header의 경우 Vuetify의 toolbar를 이용했다.



##### header

- MainHeader.vue

```
<template>
  <v-toolbar class="head">
    <!-- <v-toolbar-side-icon></v-toolbar-side-icon> -->
    <v-toolbar-title>Lagom</v-toolbar-title>
    <v-spacer></v-spacer>
      <v-btn flat>One</v-btn>
      <v-btn flat>Two</v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
export default {
  name: 'main-header'
}
</script>
<style scoped>
.head {
  position:fixed;
  left:0;
  top:0;
  width:100vw;
  z-index:200;
  height: 60px;
  text-align: left;
}
</style>
```



##### footer

- MainFooter.vue

```
<template>
    <h2>Copyright by yang</h2>
</template>

<script>
  export default {
    name: 'main-footer'
  }
</script>

<style scoped>
</style>

```



- App.vue

```
<div id="header">
    <main-header/>
</div>


<script>
import store from './store'
import MainHeader from './components/MainHeader.vue'
import MainFooter from './components/MainFooter.vue'

export default {
	name: 'App',
	store,
  components : {
    'main-header': MainHeader,
    'main-footer': MainFooter,
  },
	data() {
	...
```





- footer 다른 방법

```
<template>
  <v-footer class="pa-4">
    <v-spacer></v-spacer>
    <div>&copy; {{ new Date().getFullYear() }}</div>
  </v-footer>
</template>

```



vuetify에서 footer를 사용함



