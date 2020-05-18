//인티케이터 초기화
var indicator = document.querySelectorAll('.indicator button');
var lightbox = document.querySelectorAll('#lightbox');
var block = document.querySelector('#block');

// 라이트박스 표시 
function lightbox_open(num){
    lightbox.setAttribute('class', 'active');
}

// 라이트박스 닫기
function lightbox_close(){
    lightbox.removeAttribute('class')
}
