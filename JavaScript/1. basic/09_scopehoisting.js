//=========================================Scope====================================//
// 1. Global Scope access any where in the file
let name = 'Arijit'
function greet() {
    console.log(`Hello ${name}`)
}
greet()

// 2. Local Scope access only into a function
function greet1() {
    let name = 'Arijit'
    console.log(`Hello ${name}`)
}
greet1()

// 3. Block Scope access only within curly bracket, this is not useful in var
{
    let x = 10
    const y = 20
    console.log(x+y)
}

//=========================================Hoisting====================================//
/* 
    1. Var
    hoisting process
    var a
    console.log(a)
    a = 10
*/
var a = 10
console.log(a)

/* 
    2. Let
    hoisting process Temple Dead Zone
    console.log(a)
    let a = 10
*/
let x = 10
console.log(x)

/* 
    3. Const
    hoisting process Temple Dead Zone
    console.log(a)
    let a = 10
*/
const y = 10
console.log(y)

/* 
    4. Function
    hoisting process
*/
greet()
function greet() {
    console.log(`Hello`)
}
greet()

greet2() // No hoisting in arrow function
const greet2 = () => {
    console.log(`Hello`)
}
greet2()


greet3() // No hoisting in function expression
const greet3 = function() {
    console.log(`Hello`)
}
greet3()

