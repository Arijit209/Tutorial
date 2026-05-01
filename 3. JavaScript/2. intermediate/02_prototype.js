// Prototype
// prototype use in function
function Person(name) {
    this.name = name
}
Person.prototype.getName = function () {
    console.log(`Hello ${this.name}`)
}
const user = new Person('Arijit')
user.getName()

// Prototype Chaining
// User--->Person.prototype->Object.prototype->null
// __proto__ use in object
const animal = {
    eats: 'yes'
}
const dog = {
    barks: 'no'
}
dog.__proto__ = animal //dog is the child of animal
console.log(dog.barks)
console.log(dog.eats)