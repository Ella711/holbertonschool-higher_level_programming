function changeColor () {
  document.querySelector('header').classList.add('red');
}

const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', changeColor);
