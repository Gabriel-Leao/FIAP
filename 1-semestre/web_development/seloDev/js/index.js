const date = new Date()

setInterval(() => {
    let date = new Date()
    const clock = document.querySelector('p.footer-p')
    clock.innerText = `${date.toLocaleDateString("pt-BR")} ${('0' + date.getHours()).slice(-2)}:${('0' + date.getMinutes()).slice(-2)}:${('0' + date.getSeconds()).slice(-2)}`
}, 1000)