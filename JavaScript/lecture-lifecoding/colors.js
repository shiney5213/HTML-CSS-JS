var Body = {
	setColor:function(color){
		document.querySelector('body').style.color = color;
	},    
	// 객체의 property와 property를 구분할 때 콤마(,)를 찍음
	setBackgroundColor: function(color){
		document.querySelector('body').style.backgroundColor= color;
	}
  }
  
  var Links = {
	setColor: function(color){
	var alist = document.querySelectorAll('a');
	var i = 0;
	while(i<alist.length){
			// console.log(alist[i]);
			alist[i].style.color = color;
			i += 1;
		}
	  }
  }
  function nightDayHandler(self){
	var target = document.querySelector('body');
	if (self.value =='night'){
		Body.setBackgroundColor('white');
		Body.setColor('black');
		self.value = 'day';
		Links.setColor('powderblue')
		
	}else{
		Body.setBackgroundColor('black');
		Body.setColor('white');
		self.value = 'night';
		Links.setColor('blue')

	}
  }