//=================================================Stack Memory============================================//
/*
    1. Static memory
    2. Only for primitive data type
    3. Static Allocation
*/

let a = 10
let b = a
b = 20
console.log(a)
console.log(b)


//=================================================Heap Memory============================================//
/*
    1. Heap memory
    2. Only for preference data type
    3. Dynamic Allocation
    4. Its changble in the runtime
*/
let person1 = {
    name: 'Arijit',
    age: 40
}

let person2 = person1
person2.name = 'Pallabi'
console.log(person1.name)
console.log(person2.name)