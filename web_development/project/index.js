const menu = document.querySelector("nav")

const activeScroll = () => {
    menu.classList.toggle('active', scrollY > 50)
}

window.addEventListener('scroll', activeScroll)