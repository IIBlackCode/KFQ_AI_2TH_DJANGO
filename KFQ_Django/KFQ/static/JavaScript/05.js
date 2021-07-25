class User {
    constructor(firstName, lastname, age){
        this.firstName = firstName;
        this.lastname = lastname;
        this.age = age;
    }

    set age(v) {
        if(v < 0){
            v = 0;
        }
        this._age = v;
    }

    get age() {
        return this._age;
    }
}

const user = new User('Steve','Job', -1)
console.log(user.firstName);
console.log(user.age);

