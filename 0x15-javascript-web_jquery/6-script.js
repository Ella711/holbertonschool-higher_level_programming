const upHeader = document.querySelector('#update_header');
upHeader.addEventListener('click', updateHeader);

function updateHeader () {
  const header = document.querySelector('header');
  header.innerText = 'New Header!!!';
}
