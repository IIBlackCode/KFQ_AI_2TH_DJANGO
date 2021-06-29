function fetchUser() {
    console.log('작업중...');
    return new Promise((resolve, reject) => {
        resolve('작업완료');
    });
}
const user = fetchUser();
user.then(result => console.log(result))
