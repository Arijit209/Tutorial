//===========================================================Number Conversion==================================//
// 1. String to number 
let text = '123'
let valueToNum = Number(text)
console.log(text) // return 123
console.log(typeof text) // return string
console.log(valueToNum) // return digit
console.log(typeof valueToNum) // return number

let text1 = '123xyz'
let valueToNum1 = Number(text1)
console.log(text1) // return 123xyz
console.log(typeof text1) // return string
console.log(valueToNum1) // return NaN
console.log(typeof valueToNum1) // return number

// 2. Null to number 
let text2 = null
let valueToNum2 = Number(text2)
console.log(text2) // return null
console.log(typeof text2) // return object
console.log(valueToNum2) // return 0
console.log(typeof valueToNum2) // return number

// 3. Undefined to number 
let text3 = undefined
let valueToNum3 = Number(text3)
console.log(text3) // return undefined
console.log(typeof text3) // return undefined
console.log(valueToNum3) // return NaN
console.log(typeof valueToNum3) // return number

// 4. Boolean to number 
let text4 = true
let valueToNum4 = Number(text4)
console.log(text4) // return true
console.log(typeof text4) // return boolean
console.log(valueToNum4) // return 1
console.log(typeof valueToNum4) // return number

//===========================================================Boolean Conversion==================================//
// 1. Boolean to boolean
let bool = true
let valueToBool = Boolean(bool)
console.log(bool) // return true
console.log(typeof bool) // return boolean
console.log(valueToBool) // return true
console.log(typeof valueToBool) // return boolean

// 2. Nubmer to boolean
let bool1 = 1
let valueToBool1 = Boolean(bool1)
console.log(bool1) // return 1
console.log(typeof bool1) // return number
console.log(valueToBool1) // return true
console.log(typeof valueToBool1) // return boolean

let bool2 = 22143
let valueToBool2 = Boolean(bool2)
console.log(bool2) // return 22143
console.log(typeof bool2) // return number
console.log(valueToBool2) // return true
console.log(typeof valueToBool2) // return boolean

// 3. String to boolean
let bool3 = '1'
let valueToBool3 = Boolean(bool3)
console.log(bool3) // return 1
console.log(typeof bool3) // return string
console.log(valueToBool3) // return true
console.log(typeof valueToBool3) // return boolean

let bool4 = '1abc'
let valueToBool4 = Boolean(bool4)
console.log(bool4) // return 1abc
console.log(typeof bool4) // return string
console.log(valueToBool4) // return true
console.log(typeof valueToBool4) // return boolean

// 4. Null to boolean
let bool5 = null
let valueToBool5 = Boolean(bool5)
console.log(bool5) // return null
console.log(typeof bool5) // return oject
console.log(valueToBool5) // return false
console.log(typeof valueToBoo5) // return undefined

// 5. Undefined to boolean
let bool6 = undefined
let valueToBool6 = Boolean(bool6)
console.log(bool6) // return undefined
console.log(typeof bool6) // return undefined
console.log(valueToBool6) // return false
console.log(typeof valueToBoo6) // return undefined

//===========================================================String Conversion==================================//
// 1. Number to string
let str = 123
let valueToString = String(str)
console.log(str) // return 123
console.log(typeof str) // return number
console.log(valueToString) // return 123
console.log(typeof valueToString) // return string

// 2. Boolean to string
let str1 = true
let valueToString1 = String(str1)
console.log(str1) // return true
console.log(typeof str1) // return boolean
console.log(valueToString1) // return true
console.log(typeof valueToString1) // return string

// 3. Null to string
let str2 = null
let valueToString2 = String(str2)
console.log(str2) // return null
console.log(typeof str2) // return object
console.log(valueToString2) // return null
console.log(typeof valueToString2) // return string

// 4. Undefined to string
let str3 = undefined
let valueToString3 = String(str3)
console.log(str3) // return undefined
console.log(typeof str3) // return undefined
console.log(valueToString3) // return undefined
console.log(typeof valueToString3) // return string