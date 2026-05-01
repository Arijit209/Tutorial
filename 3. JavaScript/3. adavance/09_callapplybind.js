function greet(city) {
    console.log(`Hello, my name is ${this.name} and city is ${city}`);
}
const person = { name: 'Arijit' };

//===========================================================Call Method===========================================================
/* The call() method is a built-in JavaScript function that allows you to invoke a function with a specified 'this' value and arguments provided individually. 
 It is used to call a function with a specific context, which can be useful when you want to borrow a method from another object or when you want to set the 
'this' value explicitly.
*/
greet.call(person, 'Kolkata'); // Output: Hello, my name is Arijit and city is Kolkata

//===========================================================Apply Method===========================================================
/* The apply() method is similar to call(), but it takes the arguments as an array (or an array-like object) instead of listing them individually. 
 It is used when you want to call a function with a specific context and pass arguments as an array.
*/
greet.apply(person, ['Kolkata']); // Output: Hello, my name is Arijit and city is Kolkata

//===========================================================Bind Method===========================================================
/* The bind() method creates a new function that, when called, has its 'this' keyword set to the provided value, with a given sequence of arguments preceding any 
provided when the new function is called. It is used to create a new function with a specific context and optional arguments.
*/
const boundGreet = greet.bind(person);
boundGreet('Kolkata'); // Output: Hello, my name is Arijit and city is Kolkata

const obj1 = { 
    name: 'Alice',
    age : 30,
    greet: function() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }
};
const getval = obj1.greet.bind(obj1);
getval(); // Output: Hello, my name is Alice and I am 30 years old.