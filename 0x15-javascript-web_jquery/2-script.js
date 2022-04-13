
function changeColor () {
  document.querySelector('header').style.color = '#FF0000';
}

const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', changeColor);

// $('div#red_header').click(function () {
//   $('header').css({ color: '#FF0000' });
// });
