function getApple() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('🍎');
        }, 1000)
    });
}
function getKiwi() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve('🥝');
        }, 1000)
    });
}
function sell() {
    return getApple().then(apple => {
        return getKiwi().then(kiwi => `${apple} + ${kiwi}`);
    });
}
sell().then(res => console.log(res));