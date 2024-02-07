console.log("Hello World 2")

let count = 3

const newHello = () => {
  console.log(`Hello World ${count}`)
  count++
}

const button = document.querySelector("#click")

button.addEventListener("click", () => {
    newHello()
})

const h1 = document.createElement("h1")
h1.innerText = "Pedro Parque"
document.querySelector("body").appendChild(h1)
const p = document.createElement("p")
p.innerText = "Homem Arara"
document.querySelector("body").appendChild(p)

let idade
console.log(idade, typeof idade)

let idade1 = null
console.log(idade1, typeof idade1)

let idade2 = 20
console.log(idade2, typeof idade2)

let numero = "20"
console.log(numero, typeof numero)

let verdadeiro = true
console.log(verdadeiro, typeof verdadeiro)

const pi = 3.14
console.log(pi, typeof pi);

let numText = "123.5432"
console.log(numText)

let numFloat = parseFloat(numText)
console.log(numFloat);
// 
let numInt = parseInt(numFloat)
console.log(numInt)

let num = numInt.toString()
console.log(num)



// motivo para não usar var
function run() {
    var foo = "Foo"
    let bar = "Bar"
  
    console.log(foo, bar) // Foo Bar
  
    {
      var moo = "Mooo"
      let baz = "Bazz"
      console.log(moo, baz) // Mooo Bazz
    }
  
    console.log(moo) // Mooo
    console.log(baz) // ReferenceError
  }
  
//   run()