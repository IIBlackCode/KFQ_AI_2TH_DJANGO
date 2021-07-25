const user = {
    name: 'Bill',
    age: 20,
    hasCar: true
    }
    console.log('name' in user); // true
    console.log('age' in user); // true
    console.log('random' in user); // false
    console.log(user.hasCar); // true
    console.log(user.random)

    if(user.random == undefined){
        console.log("undefined object.")
    }