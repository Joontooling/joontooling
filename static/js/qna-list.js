// contentItemDropdwon
const contentItems = document.querySelectorAll('.contents .items .item');

contentItems.forEach((activeItem) => {
  const activeItemDropdown = activeItem.querySelector('.item-dropdown');
  const itemBtn = activeItem.querySelector('.item-btn');

  itemBtn.addEventListener('click', () => {
    contentItems.forEach((item) => {
      const itemDropdown = item.querySelector('.item-dropdown');
      if (item !== activeItem) {
        itemDropdown.classList.remove('show');
      }
    });
    activeItemDropdown.classList.toggle('show');
  });
});
