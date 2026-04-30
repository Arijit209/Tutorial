function greet(name, callback) {
    console.log(`Hello, ${name}!`);
    callback();
}
function sayGoodbye() {
    console.log('Goodbye!');
}   
greet('Arijit', sayGoodbye); // Output: Hello, Arijit! Goodbye!

// Example with an anonymous function as a callback
greet('Pallabi', function() {
    console.log('See you later!');
}); // Output: Hello, Pallabi! See you later!

function showMessage() {
    console.log('This is a message after 2 seconds' );
}
setTimeout(showMessage, 2000); // Output: This is a message after 2 seconds (after a delay of 2 seconds)

// Using an anonymous function with setTimeout
setTimeout(function() {
    console.log('This is a message after 3 seconds' );
}, 3000); // Output: This is a message after 3 seconds (after a delay of 3 seconds)