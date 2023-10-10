const { set } = require("date-fns")

// Function to simulate a loop
function simulateLoop(){
    let n = 0
    setInterval(() => {
        console.log(`Hello World ${n}`)
        n++
    }, 1000)
}

// Create a new thread-like behavior for the loop
simulateLoop() 