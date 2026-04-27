// Variables

// Scope
{

}
// ===================================================Var=============================================//
// can redeclare and reassign
var name = 'Arijit'
var name = 'Dutta'
console.log('var: '+name)

// can redeclare in scope also and update the value
var unamev1 = 'Arijit'
{
    var unamev1 = 'Dutta'
    console.log('inner scope redeclare var: '+ unamev1)
}
console.log('outer scope redeclare var: '+ unamev1)

// can reassign in scope also and update the value
var unamev2 = 'Arijit'
{
    unamev2 = 'Dutta'
    console.log('inner scope reassign var: '+ unamev2)
}
console.log('outer scope reassign var: '+ unamev2)

// hosted (undefined)
console.log('var hosted: '+x)
var x = 6;

// hosted
let x1 = 6;
console.log('var hosted: '+x1)

//===============================================Let=====================================================//
// can reassign but not redeclare
let num = 20;
num = 30
console.log('let: '+num);

// can redeclare in scope and not update the value, both are show different value
let uname1 = 'Arijit'
{
    let uname1 = 'Dutta'
    console.log('inner scope redeclare let: '+ uname1)
}
console.log('outer scope redeclare let: '+ uname1)

// can reassign in scope and update the value
let uname2 = 'Arijit'
{
    uname2 = 'Dutta'
    console.log('inner scope reassign let: '+ uname2)
}
console.log('outer scope reassign let: '+ uname2)

// hosted (show error, not possible)
// console.log('let hosted: '+y)
// let y = 6;

// hosted (undefined)
let y1;
console.log('let hosted: '+y1)
y1 = 6;

// hosted
let y2 = 6;
console.log('let hosted: '+y2)

//==================================================Const===============================================//
// not reassign but not redeclare
const pi = 3.14;
console.log('const: '+pi);

// can redeclare in scope and update the value
const unamec1 = 'Arijit'
{
    const unamec1 = 'Dutta'
    console.log('inner scope redeclare const: '+ unamec1)
}
console.log('outer scope redeclare const: '+ unamec1)

// cannot reassign in scope (show error, not possible)
// const unamec2 = 'Arijit'
// {
//     unamec2 = 'Dutta'
//     console.log('inner scope redeclare const: '+ unamec2)
// }
// console.log('outer scope reassign const: '+ unamec2)

// hosted (show error, not possible)
// console.log('const hosted: '+z1)
// const z1 = 6;

// hosted (show error, not possible)
// const z1;
// console.log('const hosted: '+z1)
// z1 = 6;

// hosted
const z3 = 6;
console.log('const hosted: '+z3)

