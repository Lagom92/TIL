# 반응형 웹 페이지 제작

페이지 최상단 이동 버튼

#### transition

#### goTo



- 

```
<v-fab-transition>
      <v-btn
        bottom
        right
        fixed
        fab
        dark
        small
        color="#CE6D39"
        v-show="btnShow"
        @click="$vuetify.goTo('#header')"
      >
        <v-icon>fas fa-angle-double-up</v-icon>
      </v-btn>
```



```
<script>
...

methods: {
    handleScroll() {
      this.btnShow = window.scrollY > 400;
    }
  },

  beforeMount() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.handleScroll);
  }

</script>
```





----

참고

https://codepen.io/BenShelton/pen/jZeNMg