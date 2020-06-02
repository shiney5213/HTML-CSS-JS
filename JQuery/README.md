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

## 3. form 태그를 만들고 post 방식으로 보내기
```
$('.save_btn').on('click', function(){
    //form 태그 만들고 post방식으로 보내기
    
    //정보 넘기기
    function post_to_url(params){
        var form = document.createElement('form');
        form.setAttribute('method', 'post');
        form.setAttribute('action', 'download');
        form.setAttribute('id', 'hiddenform');
        form.setAttribute('name', 'hiddenform');

        $('.hiddenform').append(form);

        for(var key in params){
            var hiddenField = document.createElement('input');
            hiddenField.setAttribute('type', 'hidden');
            hiddenField.setAttribute('name', key);
            hiddenField.setAttribute('value', params[key]);
            form.appendChild(hiddenField);
    	}
    }

    post_to_url({'startarray': $start_time_array2,
    'endarray': $end_time_array2});

//자동으로 submit하기
    document.hiddenform.submit();
```

## 4. Mouse handling

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

## 5. Array
#### 5.1. 추가
```
$time_array.push($maxduration2 * $percent / 100);
```
#### 5.2. 중복값 제거
```
$.each($time_array,function(i,value){
      if($time_array2.indexOf(value) == -1 ) $time_array2.push(value);
});
```
#### 5.3. 값 변경
```
//i번째 인텍스부터 j개의 값을 1,2,로 바꾸기
$analysis_start_array.slice(i,j,1,2)
```

## 6. CSS 속성 제어
```
//1개만 제어
$('.timeBar2').css('width', $percent+'%');
//여러개 제어
$('.timeBar2').css({'background-color':'red',
                'margin-left' : 0,
                'width': $canvas_position2[$array_index-1]+'%',
                })
```

## 7. ajax
```
$.ajax({url: 'download', 
       type: 'POST',
       data: {'starttimearray': $start_time_array2,
       		 'endtimearray': $end_time_array2,
       		 'filename': $(#myVideo).
       		},
       success: function(data){
        	alert(data['cropfilename']);
        }
        }
      );
```

