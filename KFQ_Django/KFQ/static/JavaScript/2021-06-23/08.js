$.ajax({
    //url주소를 변수처럼 사용
    url:'http://ggoreb.com/ajax/json/data3.jsp',
    //success를 넣어주어야 동작, 비동기로 전송요청이 성공했을 때 동작
    success: function(result) {
        console.log('result :',result)
        for(let item of result) {
            console.log('item :',item,' item.age :',item.age)
        }
    }
})