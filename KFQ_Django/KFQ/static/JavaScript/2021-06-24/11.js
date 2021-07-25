$.ajax({
    //url주소를 변수처럼 사용
    // url:'http://ggoreb.com/ajax/cors1.jsp',
    url:'http://ggoreb.com/ajax/cors2.jsp',
    //success를 넣어주어야 동작, 비동기로 전송요청이 성공했을 때 동작
    success: function(result) {
        console.log('result :',result);
        for(let obj of result) {
            console.log('obj :',obj,' obj.kind :',obj.kind)
            let dinosaurs = obj['dinosaurs'];
            for(let dinosaur of dinosaurs){
                // console.log('dinosaur :',dinosaur,' dinosaur.title',dinosaur.title);
                console.log(' dinosaur.title',dinosaur.title);
            }
        }
    }
})