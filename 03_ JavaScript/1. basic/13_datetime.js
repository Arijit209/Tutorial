// Get Date
const today = new Date()
console.log(today)

const bday = new Date('1987-02-24')
console.log(bday)

const dateNow = new Date()
console.log(dateNow)
console.log(dateNow.getFullYear())
console.log(dateNow.getMonth()+1)
console.log(dateNow.getDate())
console.log(dateNow.getHours())
console.log(dateNow.getMinutes())
console.log(dateNow.getSeconds())
console.log(dateNow.getMilliseconds())
console.log(dateNow.getTime())
console.log(dateNow.getTimezoneOffset())

// Set Date
const date = new Date()
date.setFullYear(2027)
date.setMonth(11)
date.setDate(24)
date.setHours(10)
date.setMinutes(30)
date.setSeconds(30)
console.log(date)

// Format date to string
const today1 = new Date()
console.log(today1.toDateString())
console.log(today1.toTimeString())
console.log(today1.toLocaleDateString())

// Current timestamp and difference
const fdate = new Date('1987-02-24')
const edate = new Date('2026-04-29')
const timeDiff = edate.getTime() - fdate.getTime();
const dayDiff = timeDiff / (1000 * 60 * 60 * 24)
console.log(dayDiff)