let names = "Arijit Dutta @ 38" // Double Quote
let name1 = 'Arijit Dutta @ 38' // Single Quote
let name2 = `Arijit Dutta @ 38` // literal
console.log(names)
console.log(name1)
console.log(name2)

// Concatination of String
let fname = "Arijit"
let lname = "Dutta"
// This is for single and double quote
console.log(fname + " " + lname) 
// This is for literal
console.log(`${fname} ${lname}`)

// Escape Character
// 1. New Line (\n)
let text = "Hello\nWorld"
console.log(text)
// 2. Single Quote (\')
let text1 = "It\'s a good day"
console.log(text1)
// 3. Double Quote (\"")
let text2 = "It\"s a good day"
console.log(text2)
// 4. Backslash Quote (\"")
let text3 = "Its a good day \\"
console.log(text3)

//====================================String Methods===================================//
// 1. Length
let str = "Arijit"
console.log(str.length)

// 2. Lower And Upper case
let str1 = "Arijit"
console.log(str1.toLowerCase())
console.log(str1.toUpperCase())

// 3. Character At
let str2 = "Arijit"
console.log(str2.charAt(0))

// 4. Index Of
let str3 = "Arijit"
console.log(str3.indexOf('i'))

// 5. Includes
let str4 = "Arijit"
console.log(str4.includes('i'))

// 6. Slice And Substring
let str5 = "Arijit"
console.log(str5.slice(0, 5)) // present and use in array, not reverse counting
console.log(str5.substring(0, 5)) // previous not use in array, reverse counting

// 7. Replace
let str6 = "Arijit"
console.log(str6.replace('Arijit', 'Dutta')) 

// 8. Split
let str7 = "Arijit Dutta"
console.log(str7.split(" ")) 

// 9. Trim
let str8 = " Arijit Dutta "
console.log(str8.trim()) 

// 9. Trim
let str91 = "Arijit"
let str92 = "Dutta"
console.log(str91.concat(str92)) 