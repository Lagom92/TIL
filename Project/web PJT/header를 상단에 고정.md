# 반응형 웹 페이지 제작



### 1-3. 스크롤시 헤더가 같이 움직이도록 구현

상단에 헤더 고정시키기



##### 방법 1

- MainHeader.vue

```
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



##### 방법 2

- MainHeader.vue

```
<v-toolbar class="justify-cetner" fixed dark color="#F17F42" dense>
      <v-toolbar-side-icon class="hidden-md-and-up" @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title><router-link to="/" class="Linkstyle2"><i class="fas fa-code"></i> Lagom</router-link></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat><router-link to="/post" class="Linkstyle2">포스트</router-link></v-btn>
        <v-btn flat><router-link to="/portfolio" class="Linkstyle2">포트폴리오</router-link></v-btn>
        <v-btn flat><router-link to="/login" class="Linkstyle2">로그인</router-link></v-btn>
      </v-toolbar-items>
    </v-toolbar>
```



vuetify에서 toolbar를 이용해서 구현한다.

