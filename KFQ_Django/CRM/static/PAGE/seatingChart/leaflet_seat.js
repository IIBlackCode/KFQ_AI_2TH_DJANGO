// 기본설정
var map = L.map('map', {crs: L.CRS.Simple, zoomControl: false, maxZoom: 0, dragging: false});
var imgurl = '/static/PAGE/seatingChart/seatingChart.jpg' // 이미지 경로
var bounds = [[0,0], [680,1500]]; // 이미지의 해상도를 bounds로 설정한다. [y,x]
L.imageOverlay( imgurl, bounds).addTo(map); // 배경 이미지를 설정한다.

const column = [138,317,496,675,854,1033,1212,1391]; // 분단 x 좌표
const row = [253,375,498,620]; // 몇번째 자리인지 y 좌표
var set = []; // 좌석 번호가 담길 좌표 리스트
for(var i=0; i<column.length; i++) {
	for(var j=0; j<row.length; j++) {				
		set[i*row.length+j]=[i*row.length+j+1,column[i],row[j]]; // set[e] = [좌석번호, x좌표, y좌표]
		// console.log(set[i*row.length+j]);
	}
}

var color = ['green','red','orange','gray'];
// 출 결 지 조 색깔

function seat_on(seat_num, select_class, nameValue, majorValue, daily_info,state) {
	var name='"'+nameValue+'"';
	var class_name='"'+select_class+'"';
	var major='"'+majorValue+'"';
	var temperature=daily_info[1];
	var url = "'/static/img/avatars/avatar-2.jpg'";
	var img_url = "<img src="+url+">";

	var color_name = color[state];

	var popup_content = new L.Rrose({ autoPan: false, offset: new L.Point(0,-10), closeButton: false })
	.setContent("<center>"+name+"</center><br />"+img_url+"<br />\
	<br /><center>반 : "+class_name+" 반</center><br />\
	<center>전공 : "+major+"</center><br />\
	<center>체온 : "+temperature+" 도</center>");

	L.circle([set[seat_num-1][2], set[seat_num-1][1]], {color: color_name,radius: 20, fillOpacity: 0.3}).addTo(map)
	.bindTooltip(name, {permanent: true, direction: 'center'}).openTooltip()
	.bindPopup(popup_content)
	.on("mouseover", function(evt) { this.openPopup(); })
	.on("mouseout", function(evt) { this.closePopup(); });
}

// 얘는 냅둘것
map.fitBounds(bounds); // 표현 영역을 설정한다