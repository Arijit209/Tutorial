// Lexical Scope
function outer () {
    let name = "Arijit"
    function inner () {
        console.log(name)
    }
    inner()
    console.log(name)
}
outer()

// Clouser
function greet(name) {
    return function () {
        console.log(`Hello : ${name}`)
    }
}
const greetArijit = greet('Arijit')
greetArijit()