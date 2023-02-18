const header = document.querySelector('.header');
const navFix = document.querySelector('#nav--fixed');
const headerHeight = header.offsetHeight;
const navHeight = 63;

const categoryMenuIcons = document.querySelectorAll('.inner__menu__icon');
const category = document.querySelector('.category__wrap');

window.addEventListener('scroll', () => {
  let scrollLocation = document.documentElement.scrollTop;
  if (scrollLocation > headerHeight - navHeight) {
    navFix.style.display = 'block';
  } else {
    navFix.style.display = 'none';
  }
});

categoryMenuIcons.forEach((categoryMenuIcon) => {
  categoryMenuIcon.addEventListener('click', () => {
    category.classList.toggle('active');
  });
});
