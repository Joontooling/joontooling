const header = document.querySelector('.header');
const navFix = document.querySelector('#nav--fixed');
const headerHeight = header.offsetHeight;
const navHeight = 63;

window.addEventListener('scroll', () => {
  let scrollLocation = document.documentElement.scrollTop;
  if (scrollLocation > headerHeight - navHeight) {
    navFix.style.display = 'block';
  } else {
    navFix.style.display = 'none';
  }
});
