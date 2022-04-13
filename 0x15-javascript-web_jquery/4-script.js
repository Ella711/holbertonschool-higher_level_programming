function changeStyle () {
  const header = document.querySelector('header');
  if (header.classList == 'red') {
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList == 'green') {
    header.classList.remove('green');
    header.classList.add('red');
  }
}

const toggleHeader = document.getElementById('toggle_header');
toggleHeader.addEventListener('click', changeStyle);
