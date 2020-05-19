//변수 선언
var $inp = $('form[name =cal');
var $input = $inp.find('input');
var $cls_btn = $('.cls_btn');
var $result_btm = $('.reslut_btn');
var $result = $inp.find('input[name=result]');


//계산기 초기화(clear)
function clr(){
    $result.val(0);
}

//계산기 입력처리함수
function calc(value){
    //입력이 있으면 0 지우기
    if($result.val() == 0){
        $result.val('')
    }

    //입력값을 결과창에 출력
    var val = $result.val() + value;
    $result.val(val);   //result의 값에 val을 저장하라는 뜻
}

// 계산 결과 처리 함수
function my_result(){
    var calc = eval($result.val());

    //결과창에 표시
    $result.val(calc);
}

/////이벤트 핸들러
//숫자 및 사칙 연산 버튼
$('input').click(function(){
    var $input_value = $(this).val();

    //숫자와 사칙 연산자만 입력 처리
    if($input_value != '=' && $input_value!='clear'){
        calc($input_value);
    }
});

//초기화버튼
$('.cls_btn').click(function(){
    clr();
})

//결과버튼
$('.result_btn').click(function(){
    try{
        my_result();
    }
    catch(err){
        $result.val('입력오류')
    }
})