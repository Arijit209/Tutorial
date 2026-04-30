//===================================================================Constructor Function====================================================================//
/* A constructor function is a special type of function that is used to create and initialize objects. 
    It is typically defined with a capitalized name to indicate that it is a constructor. 
*/ 
function Person(name) {
    this.name= name,
    this.sayHello = function() {
        console.log(`Hello, my name is ${this.name}.`);
    }
}

const person1 = new Person("Alice");
person1.sayHello(); // Output: Hello, my name is Alice.

const person2 = new Person("Bob");
person2.sayHello(); // Output: Hello, my name is Bob.

//===================================================================Factory Function====================================================================//
/* A factory function is a function that creates and returns an object. It is a simple way to create multiple instances of similar objects without 
    using the `new` keyword. Factory functions can be used to encapsulate the object creation logic and provide a more flexible way to create objects. 
    They can also be used to create objects with private properties and methods, which are not accessible from outside the factory function.
*/
function createPerson(name) {
    return {
        name: name,
        sayHello: function() {
            console.log(`Hello, my name is ${name}.`);
        }
    };
}

const person3 = createPerson("Alice");
person3.sayHello(); // Output: Hello, my name is Alice.


//===================================================================Module Pattern===================================================================//
/* The module pattern is a design pattern that encapsulates related code into a single unit, providing a way to organize and manage code effectively. 
    It allows for the creation of private and public members, helping to prevent global namespace pollution and enhancing code maintainability.
    In JavaScript, the module pattern can be implemented using an Immediately Invoked Function Expression (IIFE) to create a private scope. 
    Inside this scope, you can define private variables and functions that are not accessible from outside the module. The module can then return an 
    object that exposes public members, allowing controlled access to the internal functionality.
    Here's an example of the module pattern in JavaScript: 
*/
const PersonModule = (function() {
    function createPerson(name) {
        return {
            name: name,
            sayHello: function() {
                console.log(`Hello, my name is ${name}.`);
            }
        };
    }
    return {
        createPerson: createPerson
    };
})();

const person4 = PersonModule.createPerson("Bob");
person4.sayHello(); // Output: Hello, my name is Bob.