// setTimeout("location.reload()",5000)

function select_class() {
	var test = document.getElementById("select_class");
	var select_class = test.options[document.getElementById("select_class").selectedIndex].value;
	
	console.log(select_class);

	// const select_class = document.getElementById("select_class").value;
	console.log('select : ',select_class);
	
	$.ajax({
		type : 'GET',
		url : "seatingChart",
		data : {class_fk : select_class},
		success : function(context) {
			//Console 창으로 data확인
			console.log('데이터 보내기 성공',context.context);
			seatnum_length = context.context.seat_num.length;
			
			const column = [138,317,496,675,854,1033,1212,1391]; // 분단 x 좌표
			const row = [253,375,498,620]; // 몇번째 자리인지 y 좌표
			var set = []; // 좌석 번호가 담길 좌표 리스트
			var color = ['green','red','yellow','gray'];
			// 출 결 지 조 색깔

			for(var i=0; i<column.length; i++) {
				for(var j=0; j<row.length; j++) {				
					set[i*row.length+j]=[i*row.length+j+1,column[i],row[j]]; // set[e] = [좌석번호, x좌표, y좌표]
					// console.log(set[i*row.length+j]);
				}
			}

			function findstate(e) {
				if(e === 'Y') return true;
			}

			for(var i=0; i<seatnum_length; i++){
				nameValue = context.context.name[i];
				classValue = context.context.class_name[i];
				majorValue = context.context.major[i];
				seatnumValue = context.context.seat_num[i];
				daily_info_Value = context.context.daily_info[i];
				input_time_Value = context.context.daily_info[i][0];
				state = context.context.daily_info[i].slice(2).lastIndexOf('Y');
				// state = context.context.daily_info[i].findIndex(findstate);
				console.log(state);
				seat_on(seatnumValue, classValue, nameValue, majorValue, daily_info_Value,state);
			}
		}//end of success
	})//The end of Ajax
}