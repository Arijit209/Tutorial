// Set Time Out (2000 = 2secs)
console.log('Start');
setTimeout(()=>{
    console.log('Execute code')
}, 2000)
console.log('End')

// Set Interval
console.log('Start Interval');
setInterval(()=>{
    console.log('repeat code')
}, 1000)
console.log('End Interval')

// Clear Interval
let count = 0;
const IntervalId = setInterval(()=>{
    count++
    console.log('Set Count Interval')
    if(count===5) {
        clearInterval(IntervalId)
        console.log('clear interval')
    }
}, 1000)

// Clear Time Out
const timeoutId = setTimeout(()=>{
    console.log('Set Count Time ')
    clearTimeout(timeoutId)
    console.log('clear time out')
}, 5000)
