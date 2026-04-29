/*
    1. if-else statement
*/
let age = 38
if (age >= 18) {
    console.log('You are eligible for vote')
} else {
    console.log('You are not eligible for vote')
}

/*
    2. else-if statement
*/
let marks = 75
if (marks >= 90) {
    console.log('Grade A+')
} else if (marks >= 80) {
    console.log('Grade A')
} else if (marks >= 70) {
    console.log('Grade B')
} else if (marks >= 60) {
    console.log('Grade C')
} else if (marks >= 50) {
    console.log('Grade D')
} else {
    console.log('Grade E')
}

/*
    3. switch statement
*/
let day = 5
switch(day) {
    case 0:
        console.log('Sunday')
        break;
    case 1:
        console.log('Monday')
        break;
    case 2:
        console.log('Tuesday')
        break;
    case 3:
        console.log('Wednesday')
        break;
    case 4:
        console.log('Thursday')
        break;
    case 5:
        console.log('Friday')
        break;
    case 6:
        console.log('Saturday')
        break;
    default:
        console.log('No Day')
        break;
}

/*
    4. ternary statement
*/
let x = 40
let result = x >= 18 ? 'eligible for vote': 'not eligible for vote'
console.log(result)

let y = 20
let res = x < 18 ? 'you are  minor' : x > 60 ? 'senior citizen' : ' adult'
console.log(res)