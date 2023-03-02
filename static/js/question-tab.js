const tabChoices = document.querySelector('.question__choices');
const tabContainers = document.querySelectorAll('.question-tab');

tabChoices.addEventListener('click', (event) => {
  if (!event.target.classList.contains('tab-button')) {
    return;
  }

  const activeTabId = event.target.dataset.tabId;

  tabContainers.forEach((tab) => {
    if (tab.id === activeTabId) {
      tab.removeAttribute('hidden');
    } else {
      tab.setAttribute('hidden', true);
    }
  });
});
