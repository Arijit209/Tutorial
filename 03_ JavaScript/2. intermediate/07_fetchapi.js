// Get Fetch API
fetch('https://jsonplaceholder.typicode.com/posts')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error status: ${response}`)
        }
        response.json()
    })
    .then(data => console.log(data))
    .catch(error => console.error('error:', error))

// Post Fetch API
const data = {
        title: 'foo',
        body: "bar",
        userId: 101
    }
fetch('https://jsonplaceholder.typicode.com/posts', {
        method : 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error status: ${response}`)
        }
        response.json()
    })
    .then(data => console.log(data))
    .catch(error => console.error('error:', error))