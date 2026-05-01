// Promise [return success(resolve)/failure(reject)]
/**
    Syntax = new Promise((resolve, reject) => {
        // code block
    })

 */

let myPromise = new Promise((res, rej) => {
    let success = true
    if (success) {
        res('resolve successfully')
    } else {
        rej('reject successfully')
    }
})

myPromise
.then((message) => {
    console.log(message)
})
.catch((error) => {
    console.log(error)
})
.finally(()=>{
    console.log('Primise is completed')
})

// Async Await
/**
    
 */
async function fetchData() {
    try{
        let response = await fetch('https://jsonplaceholder.typicode.com/todos/1')
        let data = await response.json()
        console.log(data)
    } catch (error){
        console.log(error)
    }
}
fetchData()