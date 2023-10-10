const imgElement = document.querySelector('#img-car')
const imgs = ['assets/img/carro.jpg', 'assets/img/carro1.jpg', 'assets/img/carro2.jpg']
let index = 0

const slideShow = () => {
    if (index === imgs.length) index = 0 
    imgElement.src = imgs[index]
    index++

    setTimeout('slideShow()', 2000)
}

slideShow()