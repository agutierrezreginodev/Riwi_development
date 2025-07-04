console.log("Validar edad del usuario")

let name = prompt("Input your name: ")
let age = prompt("Input your age: ")

if (isNaN(age)) {
    console.log("You must input a number for your age.")
} else if (age > 18) {
    console.log(`Hi ${name}, you are an adult. You are ready to push your habilities in programming.`)
} else {
    console.log(`Hi ${name}, you are an under-ager. Keep learning about programming for your future.`)
}