//=================================================Primitive Data Type============================================//
/*
    string
    number
    boolean
    null
    undefined
    bigint
    symbol
*/

// String
let name = 'Arijit Dutta'
console.log(name)
console.log(typeof name)

// Number
let num = 10
console.log(num)
console.log(typeof num)

// Boolean
let bool = true
console.log(bool)
console.log(typeof bool)

// Null
let empty = null
console.log(empty)
console.log(typeof empty) // object

// Undefined
let blank
console.log(blank)
console.log(typeof blank)

// Big Integer
let big = 123456n
console.log(big)
console.log(typeof big)

// Symbol
let symb = Symbol('unique')
console.log(symb)
console.log(typeof symb)


//=================================================Reference Data Type============================================//
/*
    object
    array
    function
*/

// Object
let person = {
    name: 'Arijit',
    age: 40,
    city: 'Kolkata'
}

console.log(person)
console.log(typeof person)
console.log(person.name)
console.log(typeof person.name)
console.log(person.age)
console.log(typeof person.age)
console.log(person.city)
console.log(typeof person.city)

// Array
let fruits = ['Apple', 'Banana', 'Mango']

console.log(fruits)
console.log(typeof fruits) // object
console.log(fruits[0])
console.log(typeof fruits[0])
console.log(fruits[1])
console.log(typeof fruits[1])
console.log(fruits[2])
console.log(typeof fruits[2])

// Function
function greet() {
    console.log("Hello, Arijit Dutta")
}
greet()
console.log(greet)
console.log(typeof greet)

// Alert (It is not working in the node, because it is only for use browser, show error)
// alert('Hey, I am alert')




