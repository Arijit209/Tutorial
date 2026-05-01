/*
    1. For Loop Syntax
    for (initialization; condition; increment/decrement) {
        code to be execute
    }
    use in iteration number and array using index
*/
for (let i = 0; i < 5; i++) {
    console.log(`Arijit Dutta : ${i}`)
}

/*
    2. For In Loop Syntax
    for (variable in object) {
        code to be execute
    }
    Note: use in object
*/
let person = {
    'fname' : 'Arijit',
    'lname' : 'Dutta',
    'age' : 38 
}
for (let key in person) {
    console.log(`${key} : ${person[key]}`)
}

/*
    3. For of Loop Syntax
    for (variable of iterable) {
        code to be execute
    }
    Note: use in simple array and string
*/
let fruits = ['apple', 'banana', 'mango']
for (let fruit of fruits) {
    console.log(`${fruit}`)
}

/*
    4. While Loop Syntax
    variable initialize
    while(condition) {
        code block to be executed
    }
    Note: based on condition loop running
*/
let i = 1
while(i < 5) {
    console.log(i)
    i++
}

/*
    5. Do-While Loop Syntax
    variable initialize
    do {
        code block to be executed
    } while(condition)
    Note: one time run then check conditions
*/
let a = 0;
do {
    console.log(a);
    a++
} while(a < 5)
