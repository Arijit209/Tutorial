let arr = ['Apple', 'Banana', 'Mango']
console.log(arr)
console.log(arr[0])

arr[3] = 'Nothing'
console.log(arr[3])

// 1. Push (add to last)
let fruits = ['apple', 'banana', 'orange']
fruits.push('mango')
console.log(fruits);

// 2. Pop (remove from last)
let fruits1 = ['apple', 'banana', 'orange']
fruits1.pop()
console.log(fruits1);

// 3. Shift (remove from first)
let fruits2 = ['apple', 'banana', 'orange']
fruits2.shift()
console.log(fruits2);

// 4. Shift (add to first)
let fruits3 = ['apple', 'banana', 'orange']
fruits3.unshift('mango', 'kiwi')
console.log(fruits3);

//=====================================Advanced Array=================================//
/*
    5. forEach
    6. map
    7. filter
    8. find
    9. indexOf
    10. sort
    11. reduce
    12. slice
    13. splice
    14. concat
    15. flat
    16. spread operator
    17. destructing array
*/

// 5. Iteration of For Each 
let fruits4 = ['apple', 'banana', 'orange']
fruits4.forEach((fruit)=>{
    console.log(fruit)
})
fruits4.forEach((item, index)=>{
    console.log(`Item: ${item} and Index: ${index}`)
})

// 6. Transformation with Map (return new array)
let numbers = [1, 2, 3, 4, 5]
let double = numbers.map((num)=> num*2)
console.log(numbers)
console.log(double)

let double1 = numbers.map((item, index)=> item*2)
console.log(double1)

// 7. Transformation with Filter (return new array)
let numbers1 = [1, 2, 3, 4, 5]
let double11 = numbers1.filter((num)=> num%2 === 0)
console.log(numbers1)
console.log(double11)

let double2 = numbers1.filter((item, index)=> {
   return item % 2 === 0
})
console.log(double2)

// 8. Searching with Find (return first match item)
let numbers2 = [1, 2, 3, 4, 5]
let search = numbers2.find((num)=> num > 3)
console.log(numbers2)
console.log(search)

let search1 = numbers2.find((item, index)=> {
   return item > 3
})
console.log(search1)

// 9. Searching with Index Of (return first match item)
let numbers3 = [1, 2, 3, 4, 5]
let search2 = numbers3.indexOf(2)
console.log(numbers3)
console.log(search2)

// 10. Searching with Sort
let dummy = ['apple', 'mango', 'banana']
dummy.sort()
console.log(dummy);

let numbers4 = [5, 300, 8, 50, 2]
numbers4.sort((a, b)=> a-b) // this is for number only
console.log(numbers4)

// 11. Reduce method
/*
    Syntax
    array.reduce(callback(accumallator, currentvalue)=> {
        code block with accumallator and currentvalue    
    }, initialvalue)
*/
const nm = [1, 2, 3, 4, 5]
const sum = nm.reduce((acc, curr) => {
    return acc + curr
}, 0)
console.log(sum)

// 12. Slice method (create new array)
const nm1 = ['apple', 'banana', 'orange', 'date']
const slinm = nm1.slice(1, 3)
console.log(nm1)
console.log(slinm)

// 13. Splice method
const nm2 = ['apple', 'banana', 'orange', 'date']
const splinm = nm2.splice(1, 2, 'X', 'Y')
console.log(nm2)
console.log(splinm)

// 14. Concat method (join two array)
const nm3 = ['apple', 'banana', 'orange', 'date']
const nm31 = ['kiwi']
console.log(nm3.concat(nm31))

// 15. Flat method (nested array to flat array)
const nm4 = [1, 2, [3, 4], [5, [6, 7]]]
console.log(nm4.flat())
console.log(nm4.flat(2))

// 16. Spread Operator (use for copy, merge and parse in function argument)
const array1 = [1, 2, 3]
const array2 = [6, 7, 8]
const array3 = [...array1, 10, 50]
const array4 = [...array1, 10, 11, 12, ...array2] // merge array
console.log(array1)
console.log(array2)
console.log(array3)
console.log(array4) 

// 17. Destructuring method
const array11 = [1, 2, 3]
const [a, b, c] = array11
console.log(a)


