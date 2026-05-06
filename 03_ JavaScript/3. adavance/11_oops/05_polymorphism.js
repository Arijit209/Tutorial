class animal {
    speak() {
        console.log("Animal is speaking");
    }
}

class dog extends animal {
    speak() {
        super.speak(); // Call the parent class method
        console.log("Dog is barking");
    }
}
class cat extends animal {
    speak() {
        super.speak(); // Call the parent class method
        console.log("Cat is meowing");
    }
}
// Polymorphism with individual objects
const parentSpeak = animal.prototype.speak;
const dog1 = new dog();
parentSpeak.call(dog1);
dog1.speak();
const cat1 = new cat();
parentSpeak.call(cat1);
cat1.speak();

// Polymorphism with an array of animals
const animals = [new animal(), new dog(), new cat()];
animals.forEach(animal => animal.speak());  
