class animal {
    constructor(name, age) {
        this.name = name;
    }   
    eat() {
        console.log(`${this.name} is eating`);
    }
    sleep() {
        console.log(`${this.name} is sleeping`);
    }
}

class dog extends animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
    bark() {
        console.log(`${this.name} is barking`);
    }
    breedInfo() {
        console.log(`${this.name} is a ${this.breed}`);
    }
}
const dog1 = new dog("Tuffy", "Golden Retriever");
dog1.eat();
dog1.sleep();
dog1.bark();
dog1.breedInfo();