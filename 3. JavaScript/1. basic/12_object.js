const person = {
    name : "Arijit",
    age : 38,
    isTrainer : true
}

// Access Value
console.log(person.name)
console.log(person['age'])

// Addition
person.location = "India"
console.log(person)

// Update
person.age = 30
console.log(person)

// Delete
delete person.isTrainer
console.log(person)

// Nested Object
const person1 = {
    name : "Arijit",
    age : 38,
    isTrainer : true,
    location : {
        state : 'WB',
        city : 'Kolkata'
    }
}
console.log(person1)
console.log(person1.location.city)

// Array in Object
const person2 = {
    name : "Arijit",
    age : 38,
    isTrainer : true,
    location : ["WB", "Kolkata"]
}
console.log(person2)
console.log(person2.location[0])

// Method Object
const person3 = {
    name : "Arijit",
    age : 38,
    isTrainer : true,
    location : ["WB", "Kolkata"],
    getName : function () {
        return this.name;
    }
}
console.log(person3)
console.log(person3.getName())

// Loops in Object
for (let key in person3) {
    console.log(key, person3[key])
}
console.log(Object.keys(person3))
console.log(Object.values(person3))
console.log(Object.entries(person3))

// Object Destructuring
const person4 = {
    name : "Arijit",
    age : 38,
    isTrainer : true,
    location : {
        state : 'WB',
        city : 'Kolkata'
    }
}

const {name, age, isTrainer} = person4
console.log(name, age, isTrainer)
const {state, city} = person4.location
console.log(state, city)

// Object Spread Operator
const person5 = {
    ...person4,
    nation: "India"
}
console.log(person5)

// Operation Chaining (?.)
const person6 = {
    name : "Arijit",
    age : 38,
    isTrainer : true,
    location : {
        state : 'WB',
        city : 'Kolkata'
    }
}
console.log(person6.location?.city) // Kolkata
console.log(person6.location?.nation) // undefined

// Nullish Coalesing Operator (??)
const person7 = {
    name : "Arijit",
    age : 38,
    isTrainer : true,
    location : {
        state : 'WB',
        city : 'Kolkata'
    }
}
const city1 = person7.location.city ?? "No city found"
console.log(city1)




