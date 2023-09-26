// const h1 = document.querySelector('h1')
// let option = 3
// let option = +prompt("Digite uma opção")

// switch (option) {
//     case 1:
//         h1.innerText = "Primeira opção"
//         break
//     case 2:
//         h1.innerText = "Segunda opção"
//         break
//     case 3:
//         h1.innerText = "Terceira opção"
//         break
//     default:
//         h1.innerText = "Opção inválida"
//         break
// }

// let valor = 7
// console.log(valor)
// valor++
// console.log(valor)


// let carros = ["Fusca", "Belina", "Marea turbo", "Kombi", "Gurgel", "passat"]

// for (let i = 0; i < carros.length; i++) {
//     console.log(carros[i])
// }

// for (const carro of carros) {
//     console.log(carro)
// }

// const soma = (n1, n2) => {
//     return n1 + n2
// }

// console.log("A soma dos números é", soma(5,5))

const span = document.querySelector('span')

document.querySelector("input").addEventListener("change", (event) => {
    span.innerText = event.target.value
})

function trocar(cor){
    document.body.style.backgroundColor = cor
    document.body.style.color = "#FFF"
}