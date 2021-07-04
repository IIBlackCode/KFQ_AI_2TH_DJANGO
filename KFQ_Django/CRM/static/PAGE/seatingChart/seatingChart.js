// setTimeout("location.reload()",5000)

function select_class() {
	var test = document.getElementById("select_class");
	var select_class = test.options[document.getElementById("select_class").selectedIndex].value;
	
	console.log(select_class)

	// const select_class = document.getElementById("select_class").value;
	console.log('select : ',select_class)
	
	$.ajax({
		type : 'GET',
		url : "seatingChart",
		data : {class_fk : select_class},
		success : function(context) {
			//Console 창으로 data확인
			console.log('데이터 보내기 성공',context.context);

			nameValue = context.context.name
			majorValue = context.context.major

			const nameTag = document.getElementById("seat_name");
			nameTag.innerText = nameValue

			const majorTag = document.getElementById("seat_major");
			majorTag.innerText = majorValue
			
		}//end of success
	})//The end of Ajax
}