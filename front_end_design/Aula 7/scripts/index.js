const btnMob = document.querySelector(".btnMob")
const navbar = document.querySelector(".nav")
const html = document.querySelector("html")
const checkbox = document.querySelector("#switch")

const toggleMenu = () => {
    navbar.classList.toggle("active")
}

btnMob.addEventListener('click', toggleMenu)

checkbox.addEventListener('change', () => {
    html.classList.toggle("ligth-theme")
})

