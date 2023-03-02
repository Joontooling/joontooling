// tapControl
const tabChoices = document.querySelector('.question__choices');
const tabBtns = document.querySelectorAll('.tab-button');
const tabContainers = document.querySelectorAll('.question-tab');

tabChoices.addEventListener('click', (e) => {
  if (!e.target.classList.contains('tab-button')) {
    return;
  }

  tabBtns.forEach((btn) => {
    if (btn.classList.contains('active')) {
      btn.classList.remove('active');
    }
  });

  const activeTabId = e.target.dataset.tabId;

  tabContainers.forEach((tab) => {
    if (tab.id === activeTabId) {
      tab.removeAttribute('hidden');
      e.target.classList.add('active');
    } else {
      tab.setAttribute('hidden', true);
    }
  });
});

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
