document.getElementsByClassName('slider_left').onclick = sliderLeft;

function sliderLeft() {
    var polosa = document.getElementsByClassName('polosa');
    polosa.style.left = -250 + 'px';
}
