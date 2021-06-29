const house = {
    bathroom: 1,
    room: 2,
    address: ['제주도', '제주시', '연동'],
    persons: [
        { name: 'kim' },
        { name: 'lee' }
    ]
};

console.log(house);
delete house['bathroom'];
console.log(house);

house.animals = ['개', '고양이']
console.log(house);