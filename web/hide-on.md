# 반응형 웹 페이지 제작



### 반응형 웹 사이트 구현



##### 1. 모바일 사이즈에서 Home 화면의 About Me 이미지가 미노출 되어야 한다.

- @media 를 사용하는 방법과 hide-on 을 사용하거나 hidden을 사용하는 방법이 있다.

  
  
  이 중에서 나는 hide-on 을 사용했다.



- HomePage.vue

```
<v-flex sm4 class="hide-on-xs-only">
    <v-img :src="getImgUrl('profile.png')" aspect-ratio="1.5"/>
</v-flex>
```



- Material Design Viewport Breakpoints

xs : < 600 px

sm : 600px > < 960px

md : 960px > < 1264*

lg : 1264 > < 1904px*

xl : > 1904px*





##### 2. 모바일 사이즈에서 Home 화면의 About Me 텍스트 가운데 정렬이 되어야 한다

- text-xs-center는 xs 크기 이상은 전부 가운데 정렬
- text-sm-left는 sm크기 이상부터는 전부 왼쪽 정렬
- 위 두개를 동시에 써서 xs크기 일때만 가운데 정렬을 하도록 하였다.



- HomePage.vue

```
<h2 class="headline mb-3 text-xs-center text-sm-left">About Me</h2>
```





##### 3. 가로 사이즈에 따라 텍스트 사이즈가 자동 조절 되도록 한다.

- HomePage.vue

```
<div class="reactive_size">
	<p> ...
```



```
<style>
  .reactive_size {
    font-size: 3vw;
  }
  ...
```



