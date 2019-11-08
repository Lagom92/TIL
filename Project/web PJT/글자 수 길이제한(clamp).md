# 반응형 웹 페이지 제작

### 글자 수 길이 제한

- text overflow, text truncate, line-clamp라고도 한다.



### Vue-clamp

Clamping multiline text with ease.

- 문장의 길이 수에 따라서 마지막에 ... 으로 표현한다.



#### Installation

```
 npm i --save vue-clamp
```



#### Configuration(Vue CLI v3)

- vue.config.js

```
module.exports = {
	...
	
	 transpileDependencies: 
	 ['vue-clamp', 'resize-detector'
 ]
}

```



#### Code

- Portfolio.vue

```
<div class="headline"><v-clamp autoresize :max-lines="1">{{ title }}</v-clamp></div>
        <span class="grey--text"><v-clamp autoresize :max-lines="4">{{ body }}</v-clamp></span>
```



````
import VClamp from 'vue-clamp'
````



```
components: {
    VClamp
  },
```



- 추가적으로 Props 들은 사용해 보고싶지만 아직은 잘 모르겠다.

  나중에 시도 할 계획이다.





------

참고

https://justineo.github.io/vue-clamp/demo/