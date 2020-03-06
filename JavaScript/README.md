# JavaScript

---

- [생활코딩-JavaScript](https://opentutorials.org/course/3085) 강의를 공부한 예제입니다
- 자바스크립트를 공부하는 이유: 웹 어플리케이션에도 관심이 있고,  데이터 시각화(D3js 등)를 하고 싶기 때문입니다.

---

## 1. BASIC

#### 1.1 event

-  onclick= "자바스크립트 언어"
- html: 한번 설정되면 바뀌지 않는 정적인 언어지만, JavaScript를 이용하면 바뀔 수 있는 동적인 언어임.

```
<input type = 'button' value = 'night' onclick= "
document.querySelector('body').style.backgroundColor = 'black';
document.querySelector('body').style.color = 'white';
">
<input type = 'button' value = 'day' onclick = "
document.querySelector('body').style.backgroundColor = 'white';
document.querySelector('body').style.color = 'black';
">
```

<table>
    <tr>
    <td><img src="images\1.event_1.png" /></td>
    <td><img src ="images\1.event_2.png" /></td>
    </td>
</table>



#### 1.2 CSS

- 특정 태그를 CSS로 디자인할 때, 태그 안에 style 속성 이용

  ```
   <h2 style = 'background-color: powderblue;color = white;'>JavaScript</h2>
   <p style = color:steelblue>avaScript (/ˈdʒɑːvəˌskrɪpt/),[6] often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.[7] 
          JavaScript is high-level, often just-in-time compiled, and multi-paradigm....
   </p>
  ```

   <img src = './images/1.css_1.png' width = 33%>

- Selector : 자바스크립트에서 동적으로 제어하기 위해 CSS의 태그, id, class를 선택할 수 있음.

  ```
  element = document.querySelector(selector);
  ```

- style

  ```
  document.querySelector('body').style.backgroundColor = 'black';
  document.querySelector('body').style.color = 'white';
  ```



#### 1.3. HTML vs JavaScript

- program: 예정된 순서.  -> 시간의 순서에 따라 실행되어야 할 기능

- programing: 순서를 만드는 행위 -> 시간의 순서에 따라 실행되어야 할 기능을 프로그래밍 언어로 구현하는 것.

- HTML: 컴퓨터 언어 . 웹 페이지를 묘사한 것.(시간의 순서 없이)

- JavaScript: 프로그래밍 언어, 사용자와 상호작용하기 위해 고안된 언어. 시간의 순서에 따라 웹브라우저의 여러 기능들이 실행되어야 함.

  

### ---

## 2. 조건문, 반복문

- 조건에 따라 , 반복해서 어떤 기능을 실행하고 싶을 때

---

## 3. 함수

- 순서의 배치가 복잡해짐에 따라 잘 정리정돈할 수 있음.