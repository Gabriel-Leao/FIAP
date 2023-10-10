const form = document.querySelector('form')
const email = document.querySelector('input[type="email"]')
const password = document.querySelector('input[type="password"]')
const button = document.querySelector('button[type="submit"]')

form.addEventListener('change', () => {
    if ( email.value.toLowerCase()
    .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    ) && password.value.match(/^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*\d).*$/)) button.disabled = false
    else button.disabled = true
})

form.addEventListener('submit', (event) => {
    event.preventDefault()
    console.log(email.value, password.value)
    form.reset()
})
