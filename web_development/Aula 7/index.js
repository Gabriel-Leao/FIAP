let date = new Date()
document.writeln(date + '<br>')

let date1 = new Date().getDate()
document.writeln(date1 + '<br>')

let date2 = new Date().getMonth() + 1
document.writeln(date2 + '<br>')

let date3 = new Date().getFullYear()
document.writeln(date3 + '<br>')

let date4 = new Date()
const weekDays = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
document.writeln(weekDays[date4.getDay()] + '<br>')

let date5 = new Date()
document.writeln(date5.toDateString() + '<br>')

let date6 = new Date()
document.writeln(date6.toLocaleDateString() + '<br>')

let date7 = new Date()
let day = ('0' + date7.getDate()).slice(-2)
let month = date7.getMonth()
const months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novevembo", "Dezembro"]
let year = date7.getFullYear()
document.writeln(`São Paulo, ${day} de ${months[month]} de ${year}` + '<br>')

setInterval(() => {
    let date = new Date()
    const clock = document.querySelector('p')
    clock.innerText = `${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}:${('0' + date.getSeconds()).slice(-2)}`
}, 1000)
