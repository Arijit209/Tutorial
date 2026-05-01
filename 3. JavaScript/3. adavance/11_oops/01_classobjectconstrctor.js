// Class definition with constructor and method
class person {
    constructor(name='Unknown', age=0) {
        this.name = name;
        this.age = age;
    }
    greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
}
const person1 = new person('Arijit', 30);
person1.greet(); // Output: Hello, my name is Arijit and I am 30 years old.
const person2 = new person('Pallabi', 28);
person2.greet(); // Output: Hello, my name is Pallabi and I am 28 years old.
const person3 = new person();
person3.greet(); // Output: Hello, my name is Unknown and I am 0 years old.