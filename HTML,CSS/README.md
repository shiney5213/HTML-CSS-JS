# HTML

---

#### 1. [css, js파일 link](https://github.com/shiney5213/Study-Programming/blob/master/JavaScript/book-JavaScript_Project/html/6-3(calculator).html)

- css파일

```
<head>
	<link rel = 'stylesheet' href = 'css/6-3(calculator).css'>
</head>
```
-  js파일

```
<body>
   html내용
   	<script type = 'text/javascript' src = 'js/6-3(calculator).js'>
</body>
```





CSS
---

## 1. overflow 

- 내용이 너무 커서 지정된 영역에 맞지 않을 때 내용을자를 것인지 스크롤 막대를 추가 할 것인지를 지정
- 참고: https://www.w3schools.com/cssref/tryit.asp?filename=trycss_overflow
- 종류
  - scroll: 항상 스크롤바 사용
  - hidden :box 이외의 부분은 안나옴.
  - auto: box를 넘어가면 스크롤바가 보이고, 아니면 스크롤바 안나옴
  - visible(default): 모두 보여주기
  - initial: 기본값 설정
  - inherit: 부모 요소 속성값 상속

## 2. Z-index
- 태그들이 겹칠 때 누가 더 위로 올라가는지 결정
- 요소들이 쌓이는 순서를 position 속성을 지정하고 z-index 속성 지정하기
- z축 상의 위치를 의미
- position 속성이 설정된 요소에 대해서만 의미를 가짐
- 원래는 나중에 나온 태그가 가장 위에 위치

- 순서:(가장 아래)... -> -2 -> -1 -> 0 -> 1 -> 2 -> ....(가장 위: 사용자와 가까움)

## 3. display
- 원소의 내부, 외부 표시 유형 설정
- 종류
	- inline: <span>처럼 한 줄에 표시하기(높이, 너비 적용 불가)
	- block: <p>처럼 요소 앞 뒤에 줄바꿈 생성
	- inline-block:한 줄에 표시하지만 높이, 너비 적용 가능
	- flex: block-level을 적용하여 배치 가능

## 4. position
- 요소들을 어떻게 위치할 것인가를 설정
- 종류
	- static(default) 
		- top, bottom, left, right의 영향안받음, 
		- 왼쪽-> 오른쪽/ 위-> 아래
	- relative
		- 기존의 static이었던 위치를 기준으로 배치
		- top, left, right, buttom 속성 사용
		- 음수: 
	- fixed
		- 뷰포트 기준으로 배치
		- 스크롤되도 항상 같은 위치에 유지
	- absolute
		- position: static속성을 갖지 않은 기준으로 배치
		- postion: relative, absolute, fixed 태그가 없다면 body 태그 기준
	- sticky: 사용자의 스크롤 위치를 기준으로 배치

## 5. padding









---
### Reference
- https://www.zerocho.com/category/CSS/post/5864f3b59f1dc000182d3ea1
- 