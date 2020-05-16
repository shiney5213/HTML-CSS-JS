//변수 선언
var inp = document.forms['cal'];
var input = inp.getElementsByTagName('input')
var cls_btn = document.getElementsByClassName('cls_btn')[0];
var result_btn = document.getElementsByClassName('result_btn')[0];

//계산기 초기화
function clr(){
    inp['result'].value = 0;
}

//계산기 입력 처리 함수
function cals(value){
    //입력시 0 지움
    if(inp['result'].value==0){
        inp['result'].value = '';
    }

    //입력값을 결과창에 출력
    inp['result'].value += value;
}

//계산 결과 처리 함수
function my_result(){
    var result = document.forms['cal']['result'];
    var calc = eval(result.value);  //eval: 입력된 문자열을 그대로 명령어 처리함.

    //결과창에 표시
    inp['result'].value = calc;
}

//이벤트 핸들러
//숫자 맟 사칙연산 버튼(입력하는 button의 value를 result창에 하나씩 보여주기)
for (var i = 0; i<input.length; i++){

    //숫자와 사칙 연산자만 입력 처리
    if(input[i].value != '=' && input[i].value != 'clear'){
        input[i].onclick = function(){
            cals(this.value);
        }
    }
}

//초기화 버튼(창 깨끗하게 하기)
cls_btn.onclick = function(){
    clr();
}

//결과 버튼(예외 처리)- eval()함수 처리 중 오류 나면 예외 처리로 해결
result_btn.onclick = function(){
    try{
        my_result();
    }
    catch(err){
        var result = inp['result'];
        result.value = '입력오류';
    }
}


