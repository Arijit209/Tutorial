// Call Stack
function one() {
    two();
    console.log('one');
}

function two() {
    console.log('two');
}
one();

// Event Loop
console.log('Start');
setTimeout(() => {
    console.log('setTimeout');
}, 0);  
console.log('End');
