
navigator.geolocation.getCurrentPosition(function (pos) {
    let lat = pos.coords.latitude;
    let lng = pos.coords.longitude;
    console.log(lat, lng);
});
var container = document.getElementById('map');
var options = {
    // center: new kakao.maps.LatLng(33.450701, 126.570667),
    center: new kakao.maps.LatLng(37.480215581, 126.88161670354019),
    level: 7
};

var map = new kakao.maps.Map(container, options);

// 지도를 클릭한 위치에 표출할 마커입니다
var marker = new kakao.maps.Marker({
    // 지도 중심좌표에 마커를 생성합니다 
    position: map.getCenter()
});
// 지도에 마커를 표시합니다
marker.setMap(map);

