const popupElem = document.querySelector('.overlay')
const popupImg = document.querySelector('.popup_img')

function openPopup(src) {
  popupImg.src = src;
  popupElem.style = 'display: flex';
}

function closePopup () {
  popupElem.style = 'display: none';
}