
function search_class() {
	var name_classes = document.getElementById("select_class");
	var select_class = name_classes.options[document.getElementById("select_class").selectedIndex].value;
	
	//https://truecode-95.tistory.com/37
	$('input[name=ajax_class_name]').attr('value',select_class)
	//console.log(class_name);

	// const select_class = document.getElementById("select_class").value;
	console.log('select : ', select_class);
	
	$.ajax({
		type : 'GET',
		
		data : {
			class_name : select_class,
		},
		success : function(context) {
			//alert(context)
			//Console 창으로 data확인
			console.log('데이터 보내기 성공',context.context);
			$('#ajax_class_name').html(select_class);
		}//end of success
	})//The end of Ajax

}