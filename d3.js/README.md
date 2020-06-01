# D3.js

---

## 1. bar chart

#### 1.1 배열 지정 후, 그리기

```
var $analysis_time = data2['analysis_time'];
var $dataset = data2['rate_list']; 

var $hancan = 600 / Number($allDurationTime).toFixed(0);  //x축 한칸 크기
var $left_margin =$hancan * ($analysis_start_array2[0]).toFixed(0);
$svg.css('margin-left' ,$left_margin);
$svg.css('width',600 - $left_margin);
$graph.css('width', 600-$left_margin);

//d3.js
var svg = d3.select('svg');

svg.selectAll('bar')
    .data($dataset)  //사용할 데이터 지정
    .enter()         
    .append('rect')
    .attr('height', function(d,i) {return d* 50})  //도형 크기
    .attr('width', $hancan)
    .attr('x', function(d,i){return (($hancan) * i)})   //도형 위치
    .attr('y', function(d,i){return (100-$dataset[i]*50)}) //도형 위치
    .attr('background-color', '#cccccc');
```
#### 1.2. csv파일에서 데이터 불러오기
```


