// "use strict"
// Global Scope
console.log(this)

// Function
function thisFun() {
    console.log(this)
}
thisFun()

// Object Method
const person = {
    name : 'Arijit',
    age : 38,
    greet() {
        console.log(this.name)
    }
}
person.greet()

// Arrow Function (not work this)
const person1 = {
    name : 'Arijit',
    age : 38,
    greet :() => {
        console.log(this.name)
    }
}
person1.greet()

const person2 = {
    name : 'Arijit',
    age : 38,
    greet() {
        console.log(this.name)
        const arrow = () => {
            console.log(this.name)
        }
        arrow() // Here show
    }
}
person2.greet()

