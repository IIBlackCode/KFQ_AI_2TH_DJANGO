const promise = new Promise((resolve, reject) => {
    console.log('작업중...');
    setTimeout(() => {
        resolve('작업완료');
        // reject(new Error('응답없음'));
    }, 2000);
});
console.log(promise);
promise.then(function(result){
    console.log(`promise result ${result}`);
})//,catch()

console.log('End')