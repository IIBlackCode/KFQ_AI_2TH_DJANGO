// const data = [{ "address": ["서울", "신림"], "age": 10, "name": "A" }, { "address": ["대전", "탄방"], "age": 11, "name": "B" }, { "address": ["부산", "해운대"], "age": 12, "name": "C" }]
// console.log(data[0]['name'])
// console.log(data[1]['name'])

// for(let i = 0; i<data.length; i++) {
//     console.log(data[i]['name'])
// }
// for(let i of data) {
//     console.log(i)
// }

// const value1 = false;
// const value2 = 4 < 2;
// // true를 찾으면 true 반환하며 종료
// console.log(`or: ${value1 || value2 || check()}`);
// // false를 찾으면 false 반환하며 종료
// console.log(`and: ${value1 && value2 && check()}`);
// function check() {
// for(let i = 0; i < 10; i++) {
// console.log('pass');
// }
// return true;
// }
// console.log(!value1);

//화씨(℉)를 섭씨(℃)로 변환하기
// f = c*(9/5)+32
// c = (f-32)(5/9)

let fTemp = 122;
let cTemp = (fTemp - 32) * (5 / 9)
console.log('F :', cTemp)

//-----------------------------
let num1 = 456;
let num2 = 111;
num1 = num1 - (num1 % 100);
num1 = num1 / 100;

num2 = parseInt(num2 / 100) * 100;
console.log(`${num1} ||| ${num2}`)
//-------------------------------
//각 자리 합
let num = 12345;
let total = 0;

while (true) {
    let n1 = num % 10;
    num = parseInt(num / 10);
    total += n1;
    if (num == 0) break;
}
console.log(total)

let n1 = num % 10 // 5
num = num / 10 // 1234
num_ = parseInt(num / 10) // 1234
console.log('num % 10 =', n1)
console.log('num / 10 =', num)
console.log('parseInt(num / 10) =', num_)

//---------------------------------------
//제어문
// if / else if / else
const job = 'programmer';
if (job === 'programmer') {
    console.log('Welcome, Programmer!');
} else if (job === 'designer') {
    console.log('Good!');
} else {
    console.log('Unknown');
}

//현재 시각에 따라 아침 / 점심 / 저녁 출력

const date = new Date();
let hour = date.getHours();
let min = date.getMinutes();
let sec = date.getSeconds();
console.log("현재시각 : " + hour + "시 " + min + "분 " + sec + "초");
if (hour < 12) {
    console.log("아침");
} else if (hour < 15) {
    console.log("점심");
} else {
    console.log("저녁");
}

//switch
const browser = 'IE';
switch (browser) {
    case 'IE':
        console.log('go away!');
        break;
    case 'Chrome':
    case 'Firefox':
        console.log('love you!');
        break;
    default:
        console.log('same all!');
}

//
let sum = 0;
for(let i = 1; i <= 100 ; i += 1) {
    if(i % 2 == 0){
        sum += i;
    }
}
console.log('total : ',sum)

//
for(let i = 1; i <= 5 ; i++){
    let temp = '';
    for(let j = 1; j <= i ; j ++){
        temp += '*';
    }
    console.log(temp)
}
console.log(1,2,3,4,5)

// 함수
function name(param1, param2){
    return;
}

const f = function(){
    document.write('1');
}

setInterval(f, 1000);