const data = [{ "address": ["서울", "신림"], "age": 10, "name": "A" }, { "address": ["대전", "탄방"], "age": 11, "name": "B" }, { "address": ["부산", "해운대"], "age": 12, "name": "C" }]
console.log(data[0]['name'])
console.log(data[1]['name'])

for(let i = 0; i<data.length; i++) {
    console.log(data[i]['name'])
}
for(let i of data) {
    console.log(i)
}

