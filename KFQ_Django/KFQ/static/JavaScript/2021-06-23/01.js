class Shape {
    constructor(width, height, color) {
    this.width = width;
    this.height = height;
    this.color = color;
    }

    draw() {
    console.log(`drawing ${this.color}`);
    }

    getArea() {
    return this.width * this.height;
    }
}

class Rectangle extends Shape{

}

class Triangle extends Shape{
    
}

const r = new Rectangle(10,20,'Red');
const t = new Triangle(45,50,'Blue');

r.draw
console.log(r.getArea)
t.draw
console.log(t.getArea)