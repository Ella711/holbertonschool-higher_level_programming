window.onload = () => {
  const $listItems = document.querySelector('.my_list');
  const $addItem = document.querySelector('#add_item');
  $addItem.onclick = addItem($listItems);
};

const addItem = ($listItems) => () => {
  const $newItem = document.createElement('LI');
  $newItem.textContent = 'Item';
  $listItems.appendChild($newItem);
};
