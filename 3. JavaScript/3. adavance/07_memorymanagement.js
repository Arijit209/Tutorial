let name = 'Arijit';
let person = {
    name: 'Arijit',
    age: 30,
    city: 'Kolkata'
}
console.log(name);
console.log(person.name);

/*Memory Management
    1. Memory Allocation: When a variable is declared, memory is allocated to store its value. In JavaScript, memory is allocated 
        on the heap for objects and on the stack for primitive values.
    2. Garbage Collection: JavaScript has an automatic garbage collection mechanism that frees up memory that is no longer in use. 
        The most common algorithm used for garbage collection is the Mark-and-Sweep algorithm, which identifies and removes objects that 
        are no longer reachable from the root (global) scope.
    3. Memory Leaks: A memory leak occurs when memory that is no longer needed is not released, leading to increased memory usage over time.
        Common causes of memory leaks include:
            - Unintentional global variables: Variables that are declared without the var, let, or
                const keyword become global and can lead to memory leaks if not managed properly.   
            - Closures: If a closure retains references to variables that are no longer needed, it can prevent those variables from being garbage collected.
            - Event Listeners: If event listeners are not removed when they are no longer needed, they can retain references to DOM elements and cause memory leaks.
    4. Best Practices for Memory Management:
        - Use let and const to declare variables to avoid unintentional global variables.
        - Be mindful of closures and ensure that they do not retain unnecessary references.
        - Remove event listeners when they are no longer needed.
        - Use tools like Chrome DevTools to monitor memory usage and identify potential memory leaks.   
*/

/*Memory Management Lifecycle
    1. Creation: When a variable is declared and assigned a value, memory is allocated for that variable.
    2. Usage: The variable is used in the program, and its value may be read or modified.
    3. Deletion: When a variable goes out of scope or is explicitly deleted, it becomes eligible for garbage collection.
    4. Garbage Collection: The garbage collector identifies and frees up memory that is no longer in use, allowing it to be reused for future allocations.
    Note: mark-and-sweep algorithm:
        1. Mark Phase: The garbage collector starts from the root (global) scope and marks all reachable objects as "in use."
        2. Sweep Phase: The garbage collector then traverses the heap and frees up memory for all unmarked objects, which are considered "garbage."
*/  
function markAndSweep() {
    let obj1 = { name: 'Object 1' };
    let obj2 = { name: 'Object 2' };
    let obj3 = { name: 'Object 3' };    
    // obj1 and obj2 are reachable, while obj3 is not
    console.log(obj1.name); // Output: Object 1
    console.log(obj2.name); // Output: Object 2
    // obj3 is not reachable and will be collected by the garbage collector
}

/*
Memory Leaks Example
    1. Unintentional Global Variables:
        function createGlobalVariable() {      
            globalVar = 'I am a global variable'; // This becomes a global variable
        }
        createGlobalVariable();
    2. Closures:
        function createClosure() {
            let largeData = new Array(1000000).fill('data'); // Large data that can cause memory leak
            return function() {
                console.log(largeData[0]); // Closure retains reference to largeData
            }
        }
        let closureFunction = createClosure();  
    3. Event Listeners:
        function addEventListener() {
            let button = document.getElementById('myButton');
            button.addEventListener('click', function handleClick() {
                console.log('Button clicked');
            }); 
        }
        addEventListener();
    
*/