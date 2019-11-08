# SVG

스케일러블 벡터 그래픽스(SVG)는 2차원 벡터 그래픽을 표현하기 위한 XML 기반의 파일 형식



SVG는 확장 가능한 벡터 그래픽(Scalable Vector Graphics)의 약자로 모든 스크린에서 화질이 선명하며, 최소 용량이고, 편집과 수정이 쉽다는 장점이 있다.





### 사각형(Rectangles)

`<rect />`

x: 사각형의 좌측 상단의 x 값을 의미한다.

y: 사각형의 좌측 상단의 y 값을 의미한다.

width: 사각형의 폭을 나타낸다.

height: 사각형의 높이를 나타낸다.

rx: 사각형의 둥근 꼭짓점의 x 방향으로의 반지름을 나타낸다.

ry: 사각형의 둥근 꼭짓점의 y 방향으로의 반지름을 나타낸다.



- ex)

```
<rect x="10" y="10" width="30" height="30"/>
<rect x="60" y="10" rx="10" ry="10" width="30" height="30"/>
```







### 원(Circle)

`<circle />`

r: 원의 반지름을 의미한다.

cx: 원의 중심 중 x 값을 의미한다.

cy: 원의 중심 중 y 값을 의미한다.



- ex)

```
<circle cx="25" cy="75" r="20"/>
```





### 타원(Ellipse)

`<ellipse />`

rx: 타원의 x 방향으로의 반지름의 길이를 의미한다.

ry: 타원의 y 방향으로의 반지름의 길이를 의미한다. 

cx: 타원의 중심 중 x 값을 의미한다. 

cy: 타원의 중심 중 y 값을 의미한다. 



- ex)

```
<ellipse cx="75" cy="75" rx="20" ry="5"/>
```





### 선(Line)

`<line />`

x1: 점 1의 x 값이다. 

y1: 점 1의 y 값이다.

x2: 점 2의 x 값이다.

y2: 점 2의 y 값이다.



- ex)

```
<line x1="10" x2="50" y1="110" y2="150"/>
```







### Polyline

`<polyline />`

연결된 직선들의 그룹

모든 포인트가 하나의 속성에 포함된다.

points: 포인트들의 목록, 각 숫자는 공백, 쉼표, EOL 또는 줄 바꿈 문자로 구분된다. 각 포인트는 반드시 x 와 y로 이루어져 있다. 예를 들어 (0, 0), (1, 1) 및 (2, 2)는 "0 0, 1 1, 2 2"라고 쓸 수 있다.



- ex)

```
<polyline points="60 110, 65 120, 70 115, 75 130, 80 125, 85 140, 90 135, 95 150, 100 145"/>

```









### 다각형(Polygon)

`<polygon />`

polyline과 유사하지만 자동으로 마지막 포인트로부터 첫 번째 포인트로 직선이 그어서 닫힌 모양을 만든다.

points: 포인트들의 목록, 각 숫자는 공백, 쉼표, EOL 또는 줄 바꿈 문자로 구분된다. 각 포인트는 반드시 x 와 y로 이루어져 있다. (0,0), (1,1) 및 (2,2)는 "0 0, 1 1, 2 2"라고 쓸 수 있다. 그러면 (2,2)에서 (0,0)으로 최종 직선이 그려져서 다각형이 완성된다.



- ex)

```
<polygon points="50 160, 55 180, 70 180, 60 190, 65 205, 50 195, 35 205, 40 190, 30 180, 45 180"/>

```







### Path

`<path />`

사각형(둥근 모서리가 있거나 없는), 원, 타원, 폴리라인 및 다각형을 그릴 수 있다. 





- ex)

```
<path d="M 20 230 Q 40 205, 50 230 T 90230"/>

```

















- viewbox
- path
- fill: 색 채우기
- stroke: 외곽선의 색상
- stroke-width: 외곽선의 굵기
- stroke-linecap

- stroke-linejoin

- transform

  

- g ?: SVG에서는 <g> 엘리먼트를 사용해서 다른 엘리먼트의 그룹을 만들 수 있다.

- d







---



참고

[SVG 기본 도형_MDN](https://developer.mozilla.org/ko/docs/Web/SVG/Tutorial/%EA%B8%B0%EB%B3%B8_%EB%8F%84%ED%98%95)



[SVG path](https://developer.mozilla.org/ko/docs/Web/SVG/Tutorial/Paths)



[W3C_svg](https://www.w3schools.com/graphics/svg_intro.asp)