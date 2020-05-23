# jQuery

---

## 1. for문

```
 for (var i = 0; i < $time_array2.length; i++) {
	 alert($time_array2[i]);
```


## 2. Element append

```
var $createBar = $('<div></div>',{
            css: {'background-color':'red',
                'margin-left' : 0,
                'width': $canvas_position2[$array_index-1]+'%',
                },
            class: $barname,
            id: 'canvasBar',
            })
        $('.progressBar3').append($createBar)
```

## 3. Mouse handling
```
var $timeDrag2 = false;   /* Drag status */
//눌렀을 때
$('.progressBar2').mousedown(function(e) {
    $timeDrag2 = true;
    $updatebar2(e.pageX);    // e.pageX : 화면에서 x좌표
});
//떼었을 때
$(document).mouseup(function(e) {
    if($timeDrag2) {
        $timeDrag2 = false;
        $updatebar2(e.pageX);  
    }
});
//누르고 움직이는 동안 
$(document).mousemove(function(e) {
    if($timeDrag2) {
        $updatebar2(e.pageX);
    }
});
```

## 4. Array
#### 4.1. 추가

```
$time_array.push($maxduration2 * $percent / 100);
```
#### 4.2. 중복값 제거
```
$.each($time_array,function(i,value){
      if($time_array2.indexOf(value) == -1 ) $time_array2.push(value);
});
```

## 5. CSS 속성 제어
```
//1개만 제어
$('.timeBar2').css('width', $percent+'%');
//여러개 제어
$('.timeBar2').css({'background-color':'red',
                'margin-left' : 0,
                'width': $canvas_position2[$array_index-1]+'%',
                })
```

