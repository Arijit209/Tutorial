/*
    1. Fuction Declaration or named function
    reusable code
    hosting apply
*/
function greet(name) {
    console.log(`Hello ${name}`)
}
greet('Arijit')

/*
    2. Fuction Expression define with variable and no function name
    no hosting apply
*/
const greet2 = function(name) {
    console.log(`Hello ${name}`)
}
greet2('Arijit Dutta')

/*
    3. Arrow Funcction no hosting apply
*/
const greet3 = (name) => {
    console.log(`Hello ${name}`)
}
greet3('Arijit Dutta Arrow')

const greet4 = name => console.log(`Hello ${name}`)
greet4('Arijit Dutta Arrow2')